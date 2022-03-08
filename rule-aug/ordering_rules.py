#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:48:58 2022

@author: euan.mcgill@upf.edu
"""

from model_init import importLM
import re
import spacy as sp

model_load = importLM()
doc = model_load.to_doc("el denei debe renovarse cada cinco años")

#%%

'''
NPs: NOUN + DEMONSTRATIVE + POSSESSIVE + NUMERAL + INDEFINITE
    NOUN = nsubj NOUN
         = ROOT NOUN
         = obl NOUN
         = obj NOUN
    DEMONSTRATIVE = det DET
    POSSESSIVE = det DET
    NUMERAL = nummod NUM
            = compound NUM
    INDEFINITE = det DET
    det nsubj -> nsubj det
    nummod nsubj -> nsubj nummod
    det nummod nsubj -> nsubj det nummod (DEM and POSS)
    det nummod nsubj ->  nsubj nummod det (INDEF)
    https://universaldependencies.org/treebanks/es_pud/index.html
'''

def np_ord(doc): # split into noun chunks first and then reorder?
    listag = []
    deptag = []
    lemtag = []
    for token in doc:
        # get tuples of spaCy tags (combined and individual)
        tagged = (token.lemma_,token.dep_)
        tags_only = (token.dep_)
        lemmas_only = (token.lemma_)
        # merge lemma and dep tag together as one lexical item
        combine = '_'.join(tagged)
        # list each type of transcription, then convert to string for analysis
        listag.append(combine)
        deptag.append(tags_only)
        lemtag.append(lemmas_only)
        tagstring = ' '.join(listag)
        depstring = ' '.join(deptag)
        lemstring = ' '.join(lemtag)
# order is very important (if loops seem a little messy or unstable)
    if "nummod obl" in depstring:
        num = re.sub(r'(\S+_nummod)(\s)(\S+_obl)',r'\3\2\1',tagstring)
    elif "nummod obj" in depstring:
        num = re.sub(r'(\S+_nummod)(\s)(\S+_obj)',r'\3\2\1',tagstring)
    elif "nummod nsubj" in depstring:
        num = re.sub(r'(\S+_nummod)(\s)(\S+_nsubj)',r'\3\2\1',tagstring)
    return num

'''
Possessive constructions (might be able to include in np_ord)
'''
def possessive_const():
    pass

def compulsory_subj(doc):
    morphtag = []
    for token in doc:
        tagged = (token.text,token.morph)





