Download from https://zenodo.org/records/4783391
Repo: https://github.com/audio-captioning/clotho-dataset

wget https://zenodo.org/records/4783391/files/clotho_audio_development.7z
wget https://zenodo.org/records/4783391/files/clotho_audio_validation.7z
wget https://zenodo.org/records/4783391/files/clotho_audio_evaluation.7z


wget https://zenodo.org/records/4783391/files/clotho_metadata_development.csv
wget https://zenodo.org/records/4783391/files/clotho_metadata_validation.csv
wget https://zenodo.org/records/4783391/files/clotho_metadata_evaluation.csv

7z x clotho_audio_development.7z
7z x clotho_audio_validation.7z
7z x clotho_audio_evaluation.7z

Originally the sampling rate is 44.1 kHz: wav_original_44.1k
To convert to 16kHz:
python sampling_16k.py wav_original_44.1k/development/ wav_16k/development/
python sampling_16k.py wav_original_44.1k/validation/ wav_16k/validation/
python sampling_16k.py wav_original_44.1k/evaluation/ wav_16k/evaluation/

rename development -> train
rename validation -> val
rename evaluation -> test