## Test script for command line args

import sys
import numpy as np
from goodbye import *

def main():
    args = sys.argv
    if len(args) > 1:
        print("Hello, "+sys.argv[1]+"!")
    else:
        print("Hello, World!")
    add()
    bye()

if __name__=="__main__":
    main()
