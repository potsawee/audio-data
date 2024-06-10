from tqdm import tqdm
import sys
import json
from datasets import load_dataset

special = {
    "<COMMA>", "<QUESTIONMARK>","<PERIOD>", "<EXCLAMATIONPOINT>", "<MUSIC>", "<SIL>", "<OTHER>", "<NOISE>"
}

# original information
# {'segment_id': 'YOU0000000315_S0000660',
#  'speaker': 'N/A',
#  'text': "AS THEY'RE LEAVING <COMMA> CAN KASH PULL ZAHRA ASIDE REALLY QUICKLY <QUESTIONMARK>",
#  'audio': {'path': '/workspace2/data-audio/cache/downloads/extracted/42f19a447fabdff8fa42fea876222e05c6bf532239ff8170094bc20cc5b600c3/xs_chunks_0000/YOU0000000315_S0000660.wav',
#   'array': array([0.0005188 , 0.00085449, 0.00012207, ..., 0.00125122, 0.00076294,
#          0.00036621]),
#   'sampling_rate': 16000},
#  'begin_time': 2941.889892578125,
#  'end_time': 2945.070068359375,
#  'audio_id': 'YOU0000000315',
#  'title': 'Return to Vasselheim | Critical Role: VOX MACHINA | Episode 43',
#  'url': 'https://www.youtube.com/watch?v=zr2n1fLVasU',
#  'source': 2,
#  'category': 24,
#  'original_full_path': 'audio/youtube/P0004/YOU0000000315.opus'}

def text_processing(text):
    text = text.lower()

def process(split):
    print("split:", split)

    # If the dataset is gated/private, make sure you have run huggingface-cli login
    dataset = load_dataset("speechcolab/gigaspeech", "m", trust_remote_code=True)
    dataset = dataset[split]
    print("len_dataset:", len(dataset))
    json_data = []
    count_empty = 0
    for i, x in tqdm(enumerate(dataset)):
        text = x['text']
        words = []
        for y in text.split():
            if y in special:
                continue
            if "<" in y or ">" in y:
                import ipdb; ipdb.set_trace()
            words.append(y)
        processed = " ".join(words).lower().capitalize().strip()
        path = x['audio']['path'].replace("/workspace2/data-audio/cache/downloads", "/workspace2/data-audio/gigaspeech_hf_data")

        if processed == "":
            count_empty += 1
            print(f"count_empty: {count_empty}/{i+1}")
            continue

        json_data.append({
            'text': processed,
            'path': path
        })
    with open(f"./{split}.json", "w") as f:
        json.dump(json_data, f, indent=4)

if __name__ == "__main__":
    split = sys.argv[1]
    process(split)