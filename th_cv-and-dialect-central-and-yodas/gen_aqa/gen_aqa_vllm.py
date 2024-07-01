import os
import argparse
import json
from tqdm import tqdm
from openai import OpenAI

openai_api_key = "EMPTY"
openai_api_base = "http://localhost:8906/v1"
client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

def get_translate_body_chatml(model_name: str, text: str):
    return {
        "prompt": f"<|begin_of_text|><|start_header_id|>user<|end_header_id|>\n\n{text}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "model": model_name,
        # "frequency_penalty": 0.45,
        "frequency_penalty": 1.05,
        "max_tokens": 1024,
        "temperature": 0.3,
        "top_p": 0.4,
        "stop": ["<|eot_id|>", "<|end_of_text|>"],
    }
    
def add_arguments(parser):
    '''Build Argument Parser'''
    parser.register("type", bool, lambda v: v.lower() == "true")
    parser.add_argument('--model_path', type=str, default="scb10x/llama-3-typhoon-v1.5-8b-instruct")
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    parser.add_argument('--start_id', type=int, required=True)
    parser.add_argument('--end_id', type=int, required=True)
    return parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = add_arguments(parser)
    kwargs = vars(parser.parse_args())
    model_path = kwargs['model_path']
    data_path = kwargs['data_path']
    output_path = kwargs['output_path']
    start_id = kwargs['start_id']
    end_id = kwargs['end_id']
    for k,v in kwargs.items():
        print(k, v)

    # dataset
    with open(data_path) as f:
        dataset = json.load(f)

    # continue inference if it's been partially done
    output_path = output_path + "/{}_{}.jsonl".format(start_id, end_id)
    if os.path.exists(output_path):
        temp = []
        with open(output_path, "r") as f:
            for line in f:
                temp.append(json.loads(line))
        num_done = start_id + len(temp)
    else:
        num_done = start_id
    print("start from IDX = {}".format(num_done))

    for idx in tqdm(range(num_done, end_id)):
        # step1 -- prompt
        text = dataset[idx]['text'] # str
        if text != "":
            response = client.completions.create(**get_translate_body_chatml(model_path, text))
            response = response.choices[0].text.strip()
        else:
            response = ""

        item = {
            'text': text,
            'response': response,
            'path': dataset[idx]['path'],
        }
        with open(output_path, 'a') as f:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')


    print("finish inference run")
