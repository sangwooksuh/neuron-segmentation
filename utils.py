import os
import numpy as np
from PIL import Image
from natsort import natsorted


def scale(arr):

    return (arr - np.mean(arr)) / np.std(arr)


def load_video(path): 
    
    return np.array([
        np.asarray(Image.open(path+file)) \
         for file in natsorted(os.listdir(path)) \
         if file.endswith('.png')
    ])


def crop(img):
    
    return img[40:200,114:274]


def sumChannels(img):
    
    return np.sum(img, axis=2)


def getChannel(img, channel):
    
    return img[:,:,channel]


def load_data(path, threshold=1):
    
    print("Loading data ...")
            
    intensity = [scale(sumChannels(crop(img))) >= threshold 
                 for img in load_video(os.path.join(path,'intensities/'))]
    
    lifetime = load_video(os.path.join(path, 'lifetimes/'))
    gray = [scale(sumChannels(crop(img))) >= threshold for img in lifetime]
    red = [scale(crop(img)[:,:,0]) >= threshold for img in lifetime]
    green = [scale(crop(img)[:,:,1]) >= threshold for img in lifetime]
    blue = [scale(crop(img)[:,:,2]) >= threshold for img in lifetime]
    
    print("Loading complete!")
    
    return intensity, gray, red, green, blue


def save_video(path, video):
        
    i = 0
    save_path = os.path.join(path,'solutions/')
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    
    for frame in video:
        i += 1
        Image.fromarray(frame).save(save_path+str(i)+'.png')
        
    # print('Solution saved at '+save_path)
    
    
    