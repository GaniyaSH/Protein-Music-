# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 18:54:24 2023

@author: Ganu
"""

from scamp import*
import pandas as pd
import numpy as np
import urllib.request 
from Bio import SeqIO





notes= {'C1':24,'D1':26,'E1':28,'F1':29,'G1':31,'A1':33,'B1':35,
       'C2':36,'D2':38,'E2':40,'F2':41,'G2':43,'A2':45,'B2':47,
       'C3':48,'D3':50,'E3':52,'F3':53,'G3':55,'A3':57}

aa={'Y':24,'N':26,'M':28,'L':29,'E':31,'P':33,'W':35,'R':36,'Q':38,
    'H':40,'F':41,'S':43,'K':45,'V':47,'D':48,'T':50,'I':52,
    'C':53,'A':55,'G':57}



amino_acid={'TYR':'Y','ASN':'N','ASP':'D','CYS':'C','GLU':'E','GLN':'Q','GLY':'G','HIS':'H','ILE':'I'
            ,'LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P','SER':'S','THR':'T','TRP':'W','VAL':'V','ALA':'A'}
            
amino_acids=['Y','N','M','L','E','P','W','R','Q','H','F','S','K','V','D','T','I','A','G']





def protein(pdb:str):
    urllib.request.urlretrieve('https://files.rcsb.org/download/{}.pdb'.format(pdb),'{}.pdb'.format(pdb))
    target='C:/Users/Ganu/.spyder-py3/{}.pdb'.format(pdb)
    for record in SeqIO.parse(target, "pdb-atom"):
        sequence = record.seq
        return sequence
        


s=Session(tempo=120)
piano=s.new_part('piano')
s.start_transcribing()

i=0
for char in text:
    while(i<len(text)):
    
    
        if text[i] and df.iloc[1,i]=='E':
            piano.play_note(aa[text[i]], 1, 1)
           
        elif text[i] and df.iloc[1,i]=='H':
            piano.play_note(aa[text[i]], 0.5, 0.5)
        else:
            piano.play_note(aa[text[i]],0.25,2)
        
        i=i+1    

performance = s.stop_transcribing()     
performance.export_to_midi_file('1dc9.midi')

print(type(performance))

