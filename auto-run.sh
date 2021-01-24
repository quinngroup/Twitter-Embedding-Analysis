#!/bin/bash

echo "=====Started Auto Run===="
echo "1- Organizing Data by time(/opt/data/twitter/data/twitterdata)"
echo "   our time starts Jan 1 2014 and ends Dec 31 2016"
mkdir ../reorganized_data
python preprocessing/cluster_creator.py

echo "Attempting to create output.csv(all preprocessed tweets in a cluster)"
python preprocessing/restructure_data.py


