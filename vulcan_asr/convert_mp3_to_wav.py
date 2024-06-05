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
    mp3_files = sorted(glob(f"{input_dir}/*.mp3"))
    print("len_files:", len(mp3_files))
    for mp3_file in tqdm(mp3_files):
        file_name = mp3_file.split("/")[-1].replace(".mp3", "")
        wav_file = f"{output_dir}/{file_name}.wav"

        # Load the MP3 file
        audio = AudioSegment.from_mp3(mp3_file)
        # Set the frame rate (sampling rate) to 16 kHz
        audio = audio.set_frame_rate(target_sampling_rate)
        # Export the audio in WAV format
        audio.export(wav_file, format="wav")


if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    convert(input_dir, output_dir)