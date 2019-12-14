# -*- coding: utf-8 -*-
"""readimagefiles

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z0kfUp-z0OxHuj6mFbl7ENoIV8MvxUKo
"""

import glob
import torch
import os
from PIL import Image
from matplotlib import pyplot as plt
import torchvision.transforms as transforms
import numpy as np
def read_single_cell_image(image_data_path, mask_data_path):
  data_path=os.path.join(image_data_path, '*.tif')
  data_path1=os.path.join(mask_data_path, '*.tif')
  files=glob.glob(data_path)
  files1=glob.glob(data_path1)
  files.sort()
  files1.sort()
  sample_data = torch.zeros([1,3,256,512]).type(torch.FloatTensor)
  temp=torch.zeros([1,3,256,512]).type(torch.FloatTensor)
  counter=0
  for f1 in files:
    img=Image.open(f1)
    img=img-np.mean(img)
    imgTensor=transforms.ToTensor()(img).type(torch.FloatTensor)
    temp=torch.cat((temp, imgTensor[None,:,:,:]),0) 
    counter +=1 
    if counter%100==0:
      print(counter) 
    if temp.shape[0]>17:
      sample_data=torch.cat((sample_data,temp[1:,:,:,:]),0)
      temp = torch.zeros([1,3,256,512]).type(torch.FloatTensor)
  sample_data=sample_data[1:,:,:,:]
  

  mask = torch.zeros([1,1,256,512]).type(torch.float)
  temp = torch.zeros([1,1,256,512]).type(torch.float)
  for f1 in files1:
    img=Image.open(f1)
    img=img.convert('1')
    imgTensor=transforms.ToTensor()(img).type(torch.float)
    for i in range(17):
      temp=torch.cat((temp,imgTensor[None,:,:,:]),0)
      counter +=1
    
    mask=torch.cat((mask,temp[1:,:,:,:]),0)
    temp = torch.zeros([1,1,256,512]).type(torch.float)
    if counter%100==0:
      print(counter)
  mask=mask[1:,:,:,:]
  
  plt.imshow(mask[0][0,:,:])
  plt.imshow(sample_data[0][0,:,:])
  return sample_data, mask
