import os
import sys
import numpy as np
from utils import *


def getScore(a, b):
    
    return np.sum(np.logical_and(a,b))/np.sum(np.logical_or(a,b))


def evaluate(path, k=5):
    
    print('Evaluation:')
    truths = [sumChannels(crop(img)).astype(bool) \
              for img in load_video(os.path.join(path,'ground truth/'))]     
    solutions = load_video(os.path.join(path,'solutions/'))
    
    scores = 0
    i = 0
    
    for truth, solution in zip(truths, solutions):
        
        i += 1
        scores += (score := getScore(truth, solution))
        
        if i%k==1 or i==len(solutions):
            print('\tFrame {:2}: {:0.3f}'.format(i, score))
                 
    print('Average Accuracy: {:0.3f}'.format(scores/len(solutions)))


def main():
    args = sys.argv[1:]
    
    if len(args) == 1:
        evaluate(args[0])
    elif len(args) == 2:
        evaluate(args[0], int(args[1]))
    else:
        print("Usage: `python evaluate.py ./easy 5`")
    

if __name__=="__main__":
    main()