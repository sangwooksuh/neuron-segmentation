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

### From Repository
0. Open terminal
1. Clone this repo: `$ git clone git@github.com:sangwooksuh/neuron-segmentation.git`
2. Naviagate to repo: `$ cd neuron-segmentation`
3. Try out a demo: `$ ./demo.sh`, you may need to give execute access: `$ chmod +x ./demo/sh`

### From neuron-segmentation.zip file
0. Unzip
1. Navigate to directory: `$ cd neuron-segmentation`
2. Try out a demo: `$ ./demo.sh`, you may need to give execute access: `$ chmod +x ./demo/sh`

### Example Commands

`$ python segment.py ./data/easy`

`$ python evaluate.py ./data/easy`

`$ python segment.py --neurons 2 --threshold 0.5 --evaluate ./data/hard`

`$ python segment.py -n 2 -t 0.5 --evaluate ./data/hard`

## Dependencies
 - Python 3.8+
 - NumPy
 - natsort
 - pillow

The conda environment used to develop and test this tool is provided in `environment.yml`

This tool was developed for use in Mac OS Sonoma 14.1.1 terminal with a python environment with the above dependencies, not tested under other conditions.

## Known Issues & Bugs

### Potential recursion depth limit error with large images

Typically, Mac Terminal has a recursion depth limit of 1000, which leads to a recursion limit exceeded error with the `flood` function in `conn.py`. On Jupyter notebook, this limit is typically set as 3000, which is sufficient for the images provided (160x160). But for higher resolution images, the `flood` algorithm may hit the recursion limit and produce an error.


To mitigate this bug, the program sets the system’s recursion limit to 1,000,000 if it is lower than 1,000,000. 

### Crash when threshold set too high

If a given threshold is so high that there is no object component after thresholding in a given frame, the program crashes because at some point the 2D arrays that represents each frame become flattened, possibly due to some nuances in NumPy default behavior with differing inputs in functions such as bitwise and logical operation related functions. There was not sufficient time to properly identify and address this bug. With given data, thresholds of 1.2 or lower seemed to be safe.

### Border cropping hard-coded

This tool assumes that the image has borders that exactly match the given data, such that the image is contained in rows 40-199 and columns 114-273. The `crop` function in `utils.py` needs to be modified for data with different dimensions or borders than the given data.

### Minimal bad input handeling

This can be easily mitigated by adding input verification. This was done for command line arguments using the `argparse` module for `segment.py`, but there is no bad input handeling for the video themselves or command line arguments for `evaluate.py`



