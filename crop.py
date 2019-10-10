# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 09:18:33 2019

@author: S.S.HARI
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:31:51 2019

@author: S.S.HARI
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 01:16:58 2019

@author: S.S.HARI
"""
from PIL import Image
import numpy as np
import os
cropped_folder = "./cropped_output"

def crop_image(folder,path):
        
    if folder:
        orginal_image = os.path.join(folder,path)
    else:
        orginal_image = path
    rgb=Image.open(orginal_image)
    image=Image.open(os.path.join("saliency_output",path))
    
    image.load()
    width, height = image.size
    print(width,height)
    image_data = np.asarray(image)
#print(image_data)
#print(image_data.shape)
    max = 0
    pos=0 
    flag = 0
    if width > height :
        for i in range(0,width-height,10):
            im = image_data[:,i:i+height]
            current=np.count_nonzero(im>150)
            if(current>max):
                pos=i
                max=current
        im = image_data[:,width-height:width]
        current = np.count_nonzero(im>150)
        print(current,width-height)
        if(current>max):
            pos=width-height
            max=current
        print(max,pos)
        left = pos
        top = 0
        bottom = height
        right = pos+height
    elif height > width :
        for i in range(0,height-width,10):
            im = image_data[i:i+width,:]
            current=np.count_nonzero(im>150)
            if(current>max):
                pos=i
                max=current
        im = image_data[height-width:height,:]
        current = np.count_nonzero(im>150)
        if(current>max):
            pos=height-width
            max=current
        left = 0
        top = pos
        bottom = pos+width
        right = width
    else:
        flag = 1
    if(flag==0):                                              
        cropped = rgb.crop((left,top,right,bottom))
        cropped.save(os.path.join(cropped_folder,path))
