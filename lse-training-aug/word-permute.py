#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import choice, random

with open('/Users/e.mcgill/Documents/upf/corpora/UPM-LSE/BD/TEXTOS/signos_train.txt', 'r') as f:
    glosses = f.read().split('\n')[:10]


def permute_words(sentence, probability = .5, window_size = 4):

    tokens = glosses[0].split(' ')
    new_tokens = [t for t in tokens]
    
    
    for i in range(0, len(tokens)-window_size):
        if random() < probability: 
            t = tokens[i:window_size*(i+1)]
            word1 = choice(t)
            word2 = choice(t) 
            
            t = ' '.join(t).replace(word1, '[W_1]').replace(word2, '[W_2]')
            t = t.replace('[W_1]', word2).replace('[W_2]', word1).split(' ')
            new_tokens[i:window_size*(i+1)] = t
            
    return ' '.join(new_tokens)

input_sentence = glosses[0]

print(input_sentence)
print(permute_words(input_sentence))