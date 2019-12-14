# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JxBgWSEqWe63cglskQJJE8RudhMEgrYg
"""
#%load k_cross_data_split.py 
#from k_cross_data_split import k_cross_data_split
%load model_train.py
from model_train import model_train

from torch.utils.data import DataLoader
def cross_val(kf,sample_data,mask_data,model,para):
  for i in range(kf):
    if para['resume']>i:
      continue   
    train_data, test_data= k_cross_data_split(sample_data, mask_data, para['batch_size'],i,kf)
    train_loader=DataLoader(dataset=train_data, batch_size=para['batch_size'], shuffle=True,drop_last=True)
    test_loader=DataLoader(dataset=test_data, batch_size=para['batch_size'], shuffle=False,drop_last=True)
    print('fold:',i)
    model1=model.to(device)
    model_train(model1,train_loader,test_loader,para,i)
  return
