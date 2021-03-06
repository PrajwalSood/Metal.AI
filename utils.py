# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:53:16 2021

@author: prajw
"""


from music21 import *
import numpy as np
from collections import Counter



def read_midi(file, ins = 'Piano'):
    
    print("Loading Music File:",file)
    
    notes=[]
    notes_to_parse = None
    
    #parsing a midi file
    midi = converter.parse(file)
  
    #grouping based on different instruments
    s2 = instrument.partitionByInstrument(midi)

    #Looping over all the instruments
    for part in s2.parts:
    
        #select elements of only piano
        if ins in str(part): 
        
            notes_to_parse = part.recurse() 
      
            #finding whether a particular element is note or a chord
            for element in notes_to_parse:
                
                #note
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                
                #chord
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))

    return np.array(notes)

def flatten(arr):
    notes_ = [element for note_ in arr for element in note_]

    #No. of unique notes
    unique_notes = list(set(notes_))
    print(len(unique_notes))
    
def note_freq_hist(arr, c = 50):
    notes_ = [element for note_ in arr for element in note_]
    
    #computing frequency of each note
    freq = dict(Counter(notes_))
    
    #library for visualiation
    import matplotlib.pyplot as plt
    
    #consider only the frequencies
    no=[count for _,count in freq.items()]
    
    #set the figure size
    plt.figure(figsize=(5,5))
    
    #plot
    plt.hist(no)
    frequent_notes = [note_ for note_, count in freq.items() if count>=c]
    print(len(frequent_notes))
    return frequent_notes

def convert_to_midi_Piano(prediction_output):
   
    offset = 0
    output_notes = []

    # create note and chord objects based on the values generated by the model
    for pattern in prediction_output:
        
        # pattern is a chord
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                
                cn=int(current_note)
                new_note = note.Note(cn)
                new_note.storedInstrument = instrument.Piano()
                notes.append(new_note)
                
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
            
        # pattern is a note
        else:
            
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)

        # increase offset each iteration so that notes do not stack
        offset += 1
    midi_stream = stream.Stream(output_notes)
    midi_stream.write('midi', fp='music.mid')