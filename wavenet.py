# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:09:15 2021

@author: prajw
"""

from keras.layers import *
from keras.models import *
from keras.callbacks import *
import keras.backend as K

K.clear_session()
def wavenet(size, size_y):
    model = Sequential()
        
    #embedding layer
    model.add(Embedding(size, 100, input_length=32,trainable=True)) 
    
    model.add(Conv1D(64,3, padding='causal',activation='relu'))
    model.add(Dropout(0.2))
    model.add(MaxPool1D(2))
        
    model.add(Conv1D(128,3,activation='relu',dilation_rate=2,padding='causal'))
    model.add(Dropout(0.2))
    model.add(MaxPool1D(2))
    
    model.add(Conv1D(256,3,activation='relu',dilation_rate=4,padding='causal'))
    model.add(Dropout(0.2))
    model.add(MaxPool1D(2))
              
    #model.add(Conv1D(256,5,activation='relu'))    
    model.add(GlobalMaxPool1D())
        
    model.add(Dense(256, activation='relu'))
    model.add(Dense(size_y, activation='softmax'))
        
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
    
    model.summary()
    
    return model