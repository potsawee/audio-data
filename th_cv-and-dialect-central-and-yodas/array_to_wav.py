import sys
import numpy as np
import json
from tqdm import tqdm
from datasets import load_dataset
from scipy.io.wavfile import write

def array_to_wav(split):
    dataset = load_dataset("scb10x/th_cv-and-dialect-central-and-yodas")
    dataset = dataset[split]
    json_data = []
    for i in tqdm(range(len(dataset))):
        x = dataset[i]

        text = x['sentence']
        # extra = x['extra']

        # array path
        # path = f"/dataset/audio-data/th_cv-and-dialect-central-and-yodas/array/{split}/{i}.npy"
        # with open(path, "wb") as f:
        #     np.save(f, x['audio']['array'])

        # wav path
        path = f"/dataset/audio-data/th_cv-and-dialect-central-and-yodas/wav/{split}/{i}.wav"
        sampling_rate = 16000
        try:
            scaled = np.int16(x['audio']['array'] / np.max(np.abs(x['audio']['array'])) * 32767)
        except ValueError:
            print("ValueError... skipping:", i)
            continue
        write(path, sampling_rate, scaled)

        text = "".join(text.split(" "))
        text = text.replace("[ดนตรี]", "")
        text = text.replace("[เสียงปรบมือ]", "")
        text = text.strip()
        if "[" in text or "<" in text or text == "": 
            print("skipping:", text)
            continue

        json_data.append({
            'text': text,
            'path': path,
            # 'extra': extra,
        })

    with open(f"./{split}.json", "w") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    split = sys.argv[1]
    array_to_wav(split)