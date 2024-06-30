#!/bin/bash
#$ -S /bin/bash

# Set up your working dir here
export HF_DATASETS_CACHE=/cache/.cache/huggingface/datasets
export HF_HOME=/cache/.cache/huggingface
export HF_HUB_CACHE=/cache/.cache/huggingface/hub

# python download_filter_resample.py bal_train00
python download_filter_resample.py bal_train01
python download_filter_resample.py bal_train02
python download_filter_resample.py bal_train03
python download_filter_resample.py bal_train04
python download_filter_resample.py bal_train05
python download_filter_resample.py bal_train06
python download_filter_resample.py bal_train07
python download_filter_resample.py bal_train08
python download_filter_resample.py bal_train09
