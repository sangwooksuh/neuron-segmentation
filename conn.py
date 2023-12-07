import numpy as np


def locInBounds(loc, dims):
    return all([0<=loc[0], loc[0]<dims[0], 0<=loc[1], loc[1]<dims[1]])


def flood(img, mask, flags, loc, dims):
        
    if locInBounds(loc, dims):
    
        if img[loc] and not flags[loc]:
            
            mask[loc] = True
            flags[loc] = True
            i, j = loc
            
            flood(img, mask, flags, (i+1, j), dims)
            flood(img, mask, flags, (i-1, j), dims)
            flood(img, mask, flags, (i, j+1), dims)
            flood(img, mask, flags, (i, j-1), dims)
            
    return mask


def labelCC(img):
    # Get n largest 4-connected components of a binary image as a binary mask
    
    dims = img.shape
    flags = np.full(dims, False)
    comps = np.zeros(dims)
    label = 0
    
    # For each pixel
    for i in range(dims[0]):
        for j in range(dims[1]):
            
            # If pixel is object and not labeled yet
            if img[i, j] and not comps[i, j]: 
                
                # Flood pixel and label the flooded component
                label += 1
                comps += label * flood(img, np.full(dims, False), flags, (i,j), dims)
                
    return comps


def nLargestCC(img, n=1):
    
    comps = labelCC(img)
        
    labels, counts = np.unique(comps, return_counts = True)
    largest = labels[1:][np.argsort(counts[1:])[::-1][:n]]    

    return np.logical_or.reduce([comps == part for part in largest])


def fillHoles(img):
    
    return np.logical_not(nLargestCC(np.logical_not(img)))