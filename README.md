# neuron-segmentation
Command line tool for Neuron Image Segmentation in 2pFLIM

## Segmentation Script: `segment.py`

**Usage:** `$ python segment.py [-h] [-n] [-t] [-e] path`

Neuron segmentations in 2pFLIM as binary masks

**Positional Arguments:**

  `path`:               Path to directory that contains `intensity/` and `lifetime/`

**Options:**

  `-h`, `--help`:         Show this help message and exit.
  
  `-n` , `--neurons`:     Number of neurons in video, default 1
  
  `-t` , `--threshold`:   Threshold value for loading frames as binary images (default 1: pixel values are scaled to zero mean and unit variance)
                     
  `-e`, `--evaluate`:     Get average intersection over union (IOU) score of results with data from `path/ground truth`

## Evalutation  Script: `evaluate.py`

**Usage:** `$ python evaluate.py path [step]`

Calculates average intersection over union (IOU) score with data from `path/ground truth` and  `path/solutions`

**Positional Arguments:**

  `path`:               Path to directory that contains 'ground truth' and 'solutions'

**Options:**

  `step`: Controls step of score display output per frame. Score of first and last frame, as well as average score are always displayed.

## Getting Started

0. Open terminal
1. Clone this repo: `$ git clone git@github.com:sangwooksuh/neuron-segmentation.git`
2. Naviagate to repo: `$ cd neuron-segmentation`
3. Try out a demo of the script use: `$ ./demo.sh`

