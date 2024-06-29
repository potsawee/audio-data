from datasets import load_dataset
from tqdm import tqdm
import shutil
import sys
import json

lang = sys.argv[1]
print("lang:", lang)

# langs = ['fr_en', 'de_en', 'es_en', 'ca_en', 'it_en', 'ru_en', 'zh-CN_en', 'pt_en', 'fa_en', 'et_en', 'mn_en', 'nl_en', 'tr_en', 'ar_en', 'sv-SE_en', 'lv_en', 'sl_en', 'ta_en', 'ja_en', 'id_en', 'cy_en']

# ["fr", "de", "es", "ca", "it", "ru", "zh-CN", "pt", "fa", "et", "mn", "nl", "tr", "ar", "sv-SE", "lv", "sl", "ta", "ja", "id", "cy"]

lang0 = lang.split("_")[0]
ds = load_dataset("facebook/covost2", data_dir=f"/dataset/audio-data/covost2/{lang0}", name=lang)

for split in ['train', 'validation', 'test']:
    print("split:", split)
    new_ds = []
    count_bad = 0
    for i in tqdm(range(len(ds[split]))):
        try:
            x = ds[split][i]
        except:
            count_bad += 1
            print("cound_bad:", count_bad)
        original_path = x['file']
        file_name = original_path.split("/")[-1]

        # if file_name == "common_voice_de_19411969.mp3":
            # continue

        new_path = f"/dataset/audio-data/covost2/mp3_16kHz/{file_name}"

        sentence = x['sentence']
        translation = x['translation']
        shutil.copy(original_path, new_path)
        item = {
            'path': new_path,
            'sentence': sentence,
            'translation': translation,
        }
        new_ds.append(item)

    with open(f"/dataset/audio-data/covost2/text/{lang}.{split}.json", "w") as f:
        json.dump(new_ds, f, indent=4, ensure_ascii=False)


print("hello")