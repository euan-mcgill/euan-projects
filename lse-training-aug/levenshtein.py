#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk

ref_file = '/Users/e.mcgill/Documents/upf/corpora/Phoenix_Text_Glosses/spoken_test.txt'
gen_file = '/Users/e.mcgill/Documents/upf/corpora/Phoenix_Text_Glosses/glosses_test.txt'

def edit_dist(ref_file,gen_file):
    '''
    Calculates Levenshtein distance for two files given that they're the same length
    '''
    ref = []
    gen = []
    levenshtein = 0
    with open(ref_file,'r') as r, open(gen_file,'r') as g, open('levenshtein.tsv','w') as w:
        for line in r:
            ref.append(line.lower())
        for line in g:
            gen.append(line.lower())
        # print(len(ref),len(gen))
        for lr,lg in zip(ref,gen):
            # print(lr,'\t',lg,'\t',nltk.edit_distance(lr.split(),lg.split()))
            levenshtein += nltk.edit_distance(lr.split(),lg.split())
        print(f"Mean edit distance: {levenshtein/len(ref):0.3f}")

edit_dist(ref_file,gen_file)