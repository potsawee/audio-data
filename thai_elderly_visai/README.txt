- download from https://github.com/VISAI-DATAWOW/Thai-Elderly-Speech-dataset/releases/tag/v1.0.0
- 17 hours 11 minutes
wget https://github.com/VISAI-DATAWOW/Thai-Elderly-Speech-dataset/releases/download/v1.0.0/Dataset.zip.001
wget https://github.com/VISAI-DATAWOW/Thai-Elderly-Speech-dataset/releases/download/v1.0.0/Dataset.zip.002
wget https://github.com/VISAI-DATAWOW/Thai-Elderly-Speech-dataset/releases/download/v1.0.0/Dataset.zip.003

cat Dataset.zip.001 Dataset.zip.002 Dataset.zip.003 > Dataset.zip
unzip Dataset.zip

Dataset/ -> original wav files at 48kHz
wav_16k/ -> resampled wav files at 16kHz

data.json is the combined healthcare + smarthome data