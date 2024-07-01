from pydub import AudioSegment
from tqdm import tqdm
from glob import glob
import json


def convert(
    input_dir="clips/dev",
    output_dir="wav_16k",
    target_sampling_rate=16000
):
    print("input_dir:", input_dir)
    print("output_dir:", output_dir)
    print("target_sampling_rate:", target_sampling_rate)

    input_paths = glob(f"{input_dir}/*.wav")
    for input_path in tqdm(input_paths):
        file_name = input_path.split("/")[-1]
        output_file = f"{output_dir}/{file_name}"

        # Load the audio file
        audio = AudioSegment.from_file(input_path)

        # Set the frame rate (sampling rate) to 16 kHz
        audio = audio.set_frame_rate(target_sampling_rate)
        # Export the audio in WAV format
        audio.export(output_file, format="wav")


if __name__ == "__main__":
    input_dir = "clips/dev"
    output_dir = "wav_16k"
    convert(input_dir, output_dir)