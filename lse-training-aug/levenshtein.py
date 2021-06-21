#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk

ref_file = '/Users/e.mcgill/Documents/upf/corpora/UPM-LSE/BD/TEXTOS/signos_total.txt'
gen_file = '/Users/e.mcgill/Documents/git/euan-projects/lse-training-aug/temp2-glosses.txt'

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