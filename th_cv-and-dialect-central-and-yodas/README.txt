download this dataset using:
```
from datasets import load_dataset
dataset = load_dataset("scb10x/th_cv-and-dialect-central-and-yodas")
```

- The data is already in numpy array (but in arrow format)
- run `array_to_wav.py` to save them as separate .wav files for the SALMONN training code

Data statistics
- train: 436504 (wav), 436031 (.json)
- valid: 11039  (wav), 11038  (.json)
- test:  11039  (wav), 11038  (.json)