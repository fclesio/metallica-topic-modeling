#!/bin/bash

export LC_ALL=en_US.utf-8 &&
export LANG=en_US.utf-8 &&
pip install -U pip &&
pip install -r requirements.txt &&
python -m spacy download en_core_web_sm &&
jupyter notebook
