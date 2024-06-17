"""
1) only keep those audio files in Open-ASQA
2) resampling fromn 24 kHz to 16 kHz 
"""

from pydub import AudioSegment
from tqdm import tqdm
from glob import glob
import sys
import json


def convert(
    output_dir,
    target_sampling_rate=16000
):
    print("output_dir:", output_dir)
    print("target_sampling_rate:", target_sampling_rate)
    # input_files = sorted(glob(f"{input_dir}/*.wav"))

    # input dir is nested
    path0 = "/workspace2/data-audio/libritts/LibriTTS"
    subdirs = [
        "train-other-500",
        "train-clean-360",
        "train-clean-100",
        "dev-clean",
        "dev-other",
    ]

    with open("./openasqa_libritts_ids.json") as f:
        openasqa_ids = set(json.load(f))

    count0, count1 = 0, 0

    wav_paths_to_be_processed = []
    for subdir in tqdm(subdirs):
        path1s = glob(f"{path0}/{subdir}/*")
        for path1 in path1s:
            path2s = glob(f"{path1}/*")
            for path2 in path2s:
                wav_paths = glob(f"{path2}/*.wav")
                for wav_path in wav_paths:
                    wav_name = wav_path.split("/")[-1].replace(".wav", "")
                    if wav_name not in openasqa_ids:
                        count0 += 1
                    else:
                        count1 += 1
                        wav_paths_to_be_processed.append((wav_path, wav_name))

    # len(wav_paths_to_be_processed) => 21061
    # len(openasqa_ids)              => 21598
    for item in tqdm(wav_paths_to_be_processed):
        wav_path = item[0]
        wav_name = item[1]
        output_file = f"{output_dir}/{wav_name}.wav"

        # Load the audio file
        audio = AudioSegment.from_file(wav_path)

        # Set the frame rate (sampling rate) to 16 kHz
        audio = audio.set_frame_rate(target_sampling_rate)
        # Export the audio in WAV format
        audio.export(output_file, format="wav")


if __name__ == "__main__":
    output_dir = sys.argv[1]
    convert(output_dir)