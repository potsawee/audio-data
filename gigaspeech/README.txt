load the dataset from huggingface: https://huggingface.co/datasets/speechcolab/gigaspeech
```
from datasets import load_dataset
dataset = load_dataset("speechcolab/gigaspeech")
```

note that during the processing stage (for the M split), I encountered an error, please use the modified `gigaspeech.py` to resolve the issue

use this processing to get json {'text': ..., 'path': ...}
python process.py train
python process.py validation
python process.py test