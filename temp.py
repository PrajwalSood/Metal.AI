# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 15:07:09 2021

@author: prajw
"""

import os
from music21 import converter, pitch, interval, instrument
import tqdm
import pickle

# Define save directory
save_dir = 'data/'

# Identify list of MIDI files
songList = os.listdir(save_dir)

# Create empty list for scores
originalScores = []

'''
# Load and make list of stream objects
for song in tqdm.tqdm(songList):
    try:
        score = converter.parse(save_dir+song)
        originalScores.append(score)
    except Exception as e:
        print(e)

with open('orginalScores', 'wb') as f:
    pickle.dump(originalScores, f)
'''


with open('orginalScores', 'rb') as f:
    originalScores = pickle.load(f)
    

