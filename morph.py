## Morphological Operations for Binary Images
#
# Input:
#    img: binary image: 2D numpy boolean array
#    n: number of times repeat operation (radius)
# Output:
#    Binary image with morphologial operations applied
import numpy as np

# Slow implementation:
# def erode(img, n=1, padding='constant'):
#     for _ in range(n):
#         img = np.array([
#             [np.all(pixel) for pixel in row] 
#             for row \
#             in np.lib.stride_tricks.sliding_window_view(
#                 np.pad(img, 1, mode=padding), 
#                 (3,3)
#             )
#         ])
        
#     return img


# def dilate(img, n=1):
     
#     return np.logical_not(erode(np.logical_not(img), n, padding='edge'))

# Fast:
def erode(img, n=1, padding='constant'):
    
    for _ in range(n):
        img = np.all(np.all(
                np.lib.stride_tricks.sliding_window_view(
                    np.pad(img, 1, mode=padding), 
                    (3,3)
                )
            ,axis=2),axis=2)
        
    return img


def dilate(img, n=1):
     
    return np.logical_not(erode(np.logical_not(img), n, padding='edge'))


def opening(img, n=1):

    return dilate(erode(img, n), n)


def closing(img, n=1):
    
    return np.logical_not(opening(np.logical_not(img), n))