#!/bin/bash

echo "=====Started Auto Run===="
echo "1- Organizing Data by time(/opt/data/twitter/data/twitterdata)"
echo "   our time starts Jan 1 2014 and ends Dec 31 2016"
echo "2- Starting preprocessing phase..."
mkdir ../reorganized_data

echo "moving files to cluster format"
python preprocessing/cluster_creator.py
echo "files moved!"

echo "Attempting to create output.csv(all preprocessed tweets in a cluster)"
python preprocessing/restructure_data.py
echo "Completed preprocessing all tweets!"

echo "Moving on to building vocab for each cluster :)"
python preprocessing/vocab_dict.py
echo "Finished generating vocab for each cluster!"

echo "Creating global vocabulary"
python preprocessing/build_vocab.py
echo "Finished generating global vocabulary!"

echo "Creating empty matrix for co-occurence"
python preprocessing/create_blueprint.py
echo "Finished creating the empty matrix!"

echo "Finished Preprocessing!!"
