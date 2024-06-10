from pydub import AudioSegment
from tqdm import tqdm
from glob import glob
import sys


def convert(
    input_dir,
    output_dir,
    target_sampling_rate=16000
):
    print("input_dir:", input_dir)
    print("output_dir:", output_dir)
    print("target_sampling_rate:", target_sampling_rate)
    input_files = sorted(glob(f"{input_dir}/*.wav"))
    print("len_files:", len(input_files))
    for input_file in tqdm(input_files):
        file_name = input_file.split("/")[-1]
        output_file = f"{output_dir}/{file_name}"

        # Load the audio file
        audio = AudioSegment.from_file(input_file)

        # Set the frame rate (sampling rate) to 16 kHz
        audio = audio.set_frame_rate(target_sampling_rate)
        # Export the audio in WAV format
        audio.export(output_file, format="wav")


if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    convert(input_dir, output_dir)