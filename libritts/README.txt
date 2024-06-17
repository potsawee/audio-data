wget https://us.openslr.org/resources/60/train-clean-100.tar.gz
wget https://us.openslr.org/resources/60/train-clean-360.tar.gz
wget https://us.openslr.org/resources/60/train-other-500.tar.gz
wget https://us.openslr.org/resources/60/dev-clean.tar.gz
wget https://us.openslr.org/resources/60/dev-other.tar.gz

tar -xzvf file.tar.gz

Step1: Load all the files and uncompress them as above (wav in 24 kHz)
Step2: Resample and keep only the files in Open-ASQA
Step3: Delete LibriTTS to save space
    - train-other-500.tar.gz
    - train-clean-360.tar.gz
    - train-clean-100.tar.gz
    - dev-other.tar.gz
    - dev-clean.tar.gz
    - LibriTTS