from pydub import AudioSegment
from pydub.playback import play
from glob import glob
from tqdm import tqdm
import sys

lang = sys.argv[1]
print("lang:", lang)

# Set the desired sample rate (16kHz = 16000Hz)
target_sample_rate = 16000

input_files = sorted(glob(f"./mp3_original/common_voice_{lang}*.mp3"))
input_files = input_files[:60000]

for input_file in tqdm(input_files):

    # Load your MP3 file
    audio = AudioSegment.from_file(input_file)

    # Convert to the target sample rate
    audio = audio.set_frame_rate(target_sample_rate)

    # Export the converted audio to a new file
    file_name = input_file.split("/")[-1]
    output_file = f"mp3_16kHz/{file_name}"
    audio.export(output_file, format="mp3")

print(f"Conversion complete.")