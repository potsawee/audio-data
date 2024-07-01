Use huggingface to download
```
from huggingface_hub import snapshot_download
snapshot_download(repo_id="Fhrozen/FSD50k", allow_patterns="clips/dev/*", repo_type="dataset", local_dir="./FSD50k/")
```

