#!/bin/bash

echo "Experiment Starts"

echo "Threshold: 0"

python segment.py -t 0 -e ./data/easy
python segment.py -n 2 -t 0 -e ./data/medium
python segment.py -n 2 -t 0 -e ./data/hard

echo "Threshold: 0.25"
python segment.py -t 0.25 -e ./data/easy
python segment.py -n 2 -t 0.25 -e ./data/medium
python segment.py -n 2 -t 0.25 -e ./data/hard

echo "Threshold: 0.5"
python segment.py -t 0.5 -e ./data/easy
python segment.py -n 2 -t 0.5 -e ./data/medium
python segment.py -n 2 -t 0.5 -e ./data/hard

echo "Threshold: 0.75"
python segment.py -t 0.75 -e ./data/easy
python segment.py -n 2 -t 0.75 -e ./data/medium
python segment.py -n 2 -t 0.75 -e ./data/hard

echo "Threshold: 1"
python segment.py -t 1 -e ./data/easy
python segment.py -n 2 -t 1 -e ./data/medium
python segment.py -n 2 -t 1 -e ./data/hard

echo "Threshold: 1.1"
python segment.py -t 1.1 -e ./data/easy
python segment.py -n 2 -t 1.1 -e ./data/medium
python segment.py -n 2 -t 1.1 -e ./data/hard

echo "Threshold: 1.2"
python segment.py -t 1.2 -e ./data/easy
python segment.py -n 2 -t 1.2 -e ./data/medium
python segment.py -n 2 -t 1.2 -e ./data/hard
