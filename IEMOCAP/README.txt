The dataset is downloaded from HuggingFace (~1.4 GB)
```
from datasets import load_dataset
ds = load_dataset("Ar4ikov/iemocap_audio_text")
```
- 10039 rows
- files are saved to parquet format
- save them as .wav `array_to_wav.py`
- there are 4290 unique WAV files in OpenASQA --> wav/ => 607 MB