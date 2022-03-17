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
doc = model_load.to_doc("con tu denei puedes viajar a estos países")

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

def ord_prep(doc):
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
        depstring = ' '.join(deptag) # only return this one in prep?
        lemstring = ' '.join(lemtag)
    return tagstring, depstring, lemstring

def np_ord_rules(depstring,tagstring): # split into noun chunks first and then reorder?
#
# order is very important (if loops seem a little messy or unstable)
# why not remove all det=articles first? And use pos
#
    ### N + NUM + INDEF ###
    if ("det nummod obl" in depstring and "cada_det" in tagstring or
        "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
        tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
        or "varios_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_obl)',r'\5\4\3\2\1',tagstring)
    elif ("det nummod nsubj" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_nsubj)',r'\5\4\3\2\1',tagstring)
    elif ("det nummod obj" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_obj)',r'\5\4\3\2\1',tagstring)
    ### N + DEM + NUM ###
    elif ("det nummod obl" in depstring and "este_det" in tagstring or "ese_det" in
          tagstring or "aquel_det" in tagstring or "alguno_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_obl)',r'\5\4\1\2\3',tagstring)
    ### N + POSS + INDEF ### (amod det obj, det det obl)
    ### N + INDEF ###
    elif ("det obl" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_obl)',r'\3\2\1',tagstring)
    elif ("det ROOT" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_ROOT)',r'\3\2\1',tagstring)
    ### N + DEM ###
    elif ("det nsubj" in depstring and "este_det" in tagstring or "ese_det" in
          tagstring or "aquel_det" in tagstring or "alguno_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_nsubj)',r'\3\2\1',tagstring)
    elif ("det obl" in depstring and "este_det" in tagstring or "ese_det" in
          tagstring or "aquel_det" in tagstring or "alguno_det" in tagstring):
        num = re.sub(r'(\S+_det)(\s)(\S+_obl)',r'\3\2\1',tagstring)
    ### N + NUM ###
    elif "nummod obl" in depstring:
        num = re.sub(r'(\S+_nummod)(\s)(\S+_obl)',r'\3\2\1',tagstring)
    elif "nummod obj" in depstring:
        num = re.sub(r'(\S+_nummod)(\s)(\S+_obj)',r'\3\2\1',tagstring)
    elif "nummod nsubj" in depstring:
        num = re.sub(r'(\S+_nummod)(\s)(\S+_nsubj)',r'\3\2\1',tagstring)
    return num, depstring

# NOW, remove all the rest of the dets

def np_ord_cascade():
    # change to loop/iter for multiple lines
    pre_deps = ord_prep(doc)[1]
    pre_tags = ord_prep(doc)[0] # lemstring avail. if you need to retain full word forms
    tagstring = np_ord_rules(pre_deps,pre_tags)[0]
    depstring = re.sub(r'\S+_',r'',tagstring)
    # x = np_ord_rules(deps_again,tags_again) # UnboundLocalError: local variable 'num' referenced before assignment
    # return x
    # now repeat rule loop here (maybe a third time if nec.)
    ### N + NUM + INDEF ###
    if ("det nummod obl" in depstring and "cada_det" in tagstring or
        "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
        tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
        or "varios_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_obl)',r'\5\4\3\2\1',tagstring)
    elif ("det nummod nsubj" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_nsubj)',r'\5\4\3\2\1',tagstring)
    elif ("det nummod obj" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_obj)',r'\5\4\3\2\1',tagstring)
    ### N + DEM + NUM ###
    elif ("det nummod obl" in depstring and "este_det" in tagstring or "ese_det" in
          tagstring or "aquel_det" in tagstring or "alguno_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_nummod)(\s)(\S+_obl)',r'\5\4\1\2\3',tagstring)
    ### N + POSS + INDEF ### (amod det obj, det det obl)
    ### N + INDEF ###
    elif ("det obl" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_obl)',r'\3\2\1',tagstring)
    elif ("det ROOT" in depstring and "cada_det" in tagstring or
          "todo_det" in tagstring or "mismo_det" in tagstring or "otro_det" in
          tagstring or "mucho_det" in tagstring or "tanto_det" in tagstring
          or "varios_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_ROOT)',r'\3\2\1',tagstring)
    ### N + DEM ###
    elif ("det nsubj" in depstring and "este_det" in tagstring or "ese_det" in
          tagstring or "aquel_det" in tagstring or "alguno_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_nsubj)',r'\3\2\1',tagstring)
    elif ("det obl" in depstring and "este_det" in tagstring or "ese_det" in
          tagstring or "aquel_det" in tagstring or "alguno_det" in tagstring):
        sec = re.sub(r'(\S+_det)(\s)(\S+_obl)',r'\3\2\1',tagstring)
    ### N + NUM ###
    elif "nummod obl" in depstring:
        sec = re.sub(r'(\S+_nummod)(\s)(\S+_obl)',r'\3\2\1',tagstring)
    elif "nummod obj" in depstring:
        sec = re.sub(r'(\S+_nummod)(\s)(\S+_obj)',r'\3\2\1',tagstring)
    elif "nummod nsubj" in depstring:
        sec = re.sub(r'(\S+_nummod)(\s)(\S+_nsubj)',r'\3\2\1',tagstring)
    return sec, depstring

'''
Possessive constructions (might be able to include in np_ord)
'''
def possessive_const():
    pass
    # DET (subset, but could combine with set of rules above) + nsubj/obl/obj
    # case nmod
    # output = N + PROPIO + PRON
    ### incorporate removing all DETs here? ###

def compulsory_subj(doc):
    # this should come before reordering rules
    morphtag = []
    for token in doc:
        tagged = (token.text,token.morph)

def plural_constructions(doc):
    # this should come before reordering rules
    pass


#%%
'''
Alternative algorithm (a la Vegas Cañas):
    Collect all words in a dict
    Label
    If they match conditional word order, plug them into sentence
'''







