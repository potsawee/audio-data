import numpy as np
import json
from tqdm import tqdm
from datasets import load_dataset
from scipy.io.wavfile import write

def array_to_wav():
    dataset = load_dataset("Ar4ikov/iemocap_audio_text")
    dataset = dataset["train"]

    # the script will save only those files in OpenASQA
    with open("./openasqa_iemocap_ids.json") as f:
        openasqa_ids = set(json.load(f)) # len 4290

    json_data = []
    count = 0
    for i in tqdm(range(len(dataset))):
        x = dataset[i]
        name = x['titre']
        if name not in openasqa_ids:
            continue

        # wav path
        path = f"/dataset/audio-data/IEMOCAP/wav/{name}.wav"
        sampling_rate = 16000
        try:
            scaled = np.int16(x['audio']['array'] / np.max(np.abs(x['audio']['array'])) * 32767)
        except ValueError:
            print("ValueError... skipping:", i)
            continue
        write(path, sampling_rate, scaled)

        count += 1
        print(count, path)



if __name__ == "__main__":
    array_to_wav()