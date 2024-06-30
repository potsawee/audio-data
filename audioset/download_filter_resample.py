from pydub import AudioSegment
from glob import glob
from tqdm import tqdm
from huggingface_hub import snapshot_download
import sys
import os
import tarfile
import shutil

file_name = sys.argv[1] # bal_train00

# Step1: download
print("\n-------------------------\n")
print("Step1: Download...", file_name)
snapshot_download(repo_id="agkphysics/AudioSet", allow_patterns=f"data/{file_name}.tar", local_dir=f"./downloads/", repo_type="dataset")

# Step2: Extract the tarball file
print("Step2: Extract the tarball file")
tarball_file = f'./downloads/data/{file_name}.tar'
extract_to_directory = f'./downloads/extracted/{file_name}'
os.makedirs(extract_to_directory, exist_ok=True)
# Open the tarball file
with tarfile.open(tarball_file) as tar:
    # Extract all contents to the specified directory
    tar.extractall(path=extract_to_directory)

# Step3: Get paths to all extracted flac files
print("Step3: Get paths to all extracted flac files")
flac_paths = glob(f"./downloads/extracted/{file_name}/audio/*/*.flac")
assert len(flac_paths) > 0

# Step4: filter and resample
print("Step4: Filter & Resample")
with open("ltu-audioset-ids.txt") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
ltu_files = set(lines)
for flac_path in tqdm(flac_paths):
    flac_name = flac_path.split("/")[-1]

    # 4.1: filter
    if flac_name not in ltu_files:
        continue

    # 4.2: resample
    audio = AudioSegment.from_file(flac_path, format="flac")
    resampled_audio = audio.set_frame_rate(16000)
    resampled_audio.export(f"./flac_16kHz/{flac_name}", format="flac")

# Step5: delete unnecessary files
print("Step5: deleting...")
os.remove(tarball_file) # tarball
print("deleted:", tarball_file)
shutil.rmtree(extract_to_directory)
print("deleted:", extract_to_directory)
with open(f"./progress_log/{file_name}.log", "w") as f:
    f.write(f"processing {file_name} done!")
