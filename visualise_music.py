# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 14:51:32 2021

@author: prajw
"""

from music21 import converter

# Define data directory
data_dir = 'data/'

# Parse MIDI file and convert notes to chords
score = converter.parse(data_dir+"Black Sabbath - Bassically.mid").chordify()

# Display as sheet music - requires MuseScore 3 to be installed
try:
    print(score.show())
except:
    print('Check your MuseScore 3 installation')

#dispaly as text in console
print(score.show('text'))


print(score.elements[10].duration)

