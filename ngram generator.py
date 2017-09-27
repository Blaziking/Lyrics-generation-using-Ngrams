import nltk
import numpy as np
from collections import Counter, defaultdict
import random

import string

f = open("Dylan, Bob Lyrics, 1962-2001 - preprocessed.txt", 'r',encoding="utf8")
	
lines = []	
for lyric in f:
        
        lyric = lyric.lower()
        lines.extend(lyric.split('\n'))

    
lyrics = ' '.join(lines)

order = int(input('Enter character-level n-gram order: '))




def train_char_lm(data, order=4):
    lm = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in range(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        lm[history][char]+=1
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.items()]
    outlm = {hist:normalize(chars) for hist, chars in lm.items()}
    return outlm



def generate_text(lm, order, nletters=1000):
    history = random.choice(list(lm.items()))[0]
    out = []
    for i in range(nletters):
        c = generate_letter(lm, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)



def generate_letter(lm, history, order):
    history = history[-order:]
    dist = lm[history]
    x = random.random()
    for c,v in dist:
        x = x - v
        if x <= 0: return c



lm = train_char_lm(lyrics, order)
print (generate_text(lm, order))

		
