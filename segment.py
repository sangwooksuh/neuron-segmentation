import sys
import argparse
import itertools
import numpy as np
from conn import *
from morph import *
from utils import *


def get_args():
    
    parser = argparse.ArgumentParser(
        description='Neuron segmentations in 2pFLIM as binary masks'
    )
    parser.add_argument( 
        "path", type=str,
        help="path to directory that contains 'intensity' and 'lifetime'"
    )
    parser.add_argument(
        "-n", "--neurons", default=1, type=int, required=False,
        help="number of neurons in video, default 1",
        metavar=''
    )
    parser.add_argument(
        "-t", "--threshold", default=1, type=float, required=False,
        help="threshold value for loading frames as binary images \
        (default 1: pixel values are scaled to zero mean and unit variance)",
        metavar=''
    )
    parser.add_argument(
        "-e", "--evaluate", action="store_true",
        help="get average intersection over union (IOU) score compared \
        with data from 'ground truth'"
    )
    
    return parser.parse_args()


def solve_kernel(frame, neurons):
    # frame := (intensity[i], gray[i], red[i], green[i], blue[i])
    
    intersections = [ np.logical_and(*pair) for pair in itertools.combinations(frame, 2)]
    union = np.logical_or.reduce(intersections)
    
    # return closing(fillHoles(nLargestCC(erode(union), neurons)))                      #(701, 782, 660)
    # return dilate(fillHoles(nLargestCC(closing(opening(union)), neurons)))            #(754 ,779, 702) ## THIRD
    # return dilate(opening(fillHoles(nLargestCC(closing(opening(union)), neurons))),2) #(771, 699, 729)
    # return closing(fillHoles(nLargestCC(opening(union), neurons)))                    #(755, 805, 639)
    # return opening(closing(fillHoles(nLargestCC(closing(opening(union)), neurons))))  #(716, 803, 647)
    # return dilate(closing(fillHoles(nLargestCC(closing(opening(union,2)), neurons))),2)  #(808,722,740) ## SECOND
    # return closing(fillHoles(nLargestCC(closing(opening(union,2)), neurons)),2)         #(755,828,679)
    
    return dilate(closing(fillHoles(nLargestCC(closing(opening(union,2)), neurons)))) #(785,801,722) ## WINNER

    
def solve(data, neurons):
    
    # print('Segmenting neurons ...')
    solutions = [solve_kernel(frame, neurons) for frame in zip(*data)]
    # print('Segmentation complete!')
    
    return solutions


def evaluate(solutions, path):
    
    if os.path.exists(os.path.join(path, 'ground truth/')):
        
        truths = [sumChannels(crop(img)).astype(bool) \
                  for img in load_video(os.path.join(path,'ground truth/'))]
        score_sum = 0
        for data in zip(truths, solutions):
            score_sum += np.sum(np.logical_and(*data))/np.sum(np.logical_or(*data))
            
        
        print('Average score (IOU): {:0.3f} [END]'.format(score_sum/len(truths)))
    else:
        print("'ground truth' does not exist in path! [END]")


def run(path, neurons, threshold, score):
    
    print('---')
    print(f'Problem: {path}; Neurons: {neurons}; Threshold: {threshold}')

    
    if sys.getrecursionlimit() < 1000000:
        sys.setrecursionlimit(1000000)
        
    data = load_data(path, threshold)
    solutions = solve(data, neurons)
    save_video(path, solutions)
    
    if score:
        evaluate(solutions, path)
    else:
        print('Solution saved at '+os.path.join(path, 'ground truth/ [END]'))
        
    print('---')
    
    
def main():
    
    args = get_args()
    run(args.path, args.neurons, args.threshold, args.evaluate)
    
    
if __name__=="__main__":
    main()
