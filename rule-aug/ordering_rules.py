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
# doc = model_load.to_doc("vivo en este país para cada tres días de la semana y tu padre")
doc = model_load.to_doc("si no vives en españa tienes que traer estos documentos")

#%%

'''
NPs: NOUN + DEMONSTRATIVE + POSSESSIVE + NUMERAL + INDEFINITE


https://universaldependencies.org/treebanks/es_pud/index.html
'''

def ord_prep(doc):
    listag = []
    deptag = []
    lemtag = []
    postag = []
    for token in doc:
        # get tuples of spaCy tags (combined and individual)
        tagged = (token.lemma_,token.pos_)
        tags_only = (token.dep_)
        lemmas_only = (token.lemma_)
        pos_only = (token.pos_)
        # merge lemma and dep tag together as one lexical item
        combine = '_'.join(tagged)
        # list each type of transcription, then convert to string for analysis
        listag.append(combine)
        deptag.append(tags_only)
        lemtag.append(lemmas_only)
        postag.append(pos_only)
        tagstring = ' '.join(listag)
        depstring = ' '.join(deptag) # only return this one in prep?
        lemstring = ' '.join(lemtag)
        posstring = ' '.join(postag)
    return tagstring, depstring, lemstring, posstring

# mortag = []
# for token in doc:
#     morphed = (token.lemma_, ' '.join(token.morph.get("Person")), ' '.join(token.morph.get("Number")))
#     together = '_'.join(morphed)
#     mortag.append(together)
#     morstring = ' '.join(mortag)

def compulsory_subj(doc):
    # must also consider negatives w/in the word order
    # tienes que -> necesitar
    pass

def np_ord(tag,pos):
    tag = ord_prep(doc)[0]
    pos = ord_prep(doc)[3]
    #
    # first remove DETs which are (in)definite articles
    a = re.sub(r'el_DET ',r'',tag)
    # move all DETs before NOUNs
    b = re.sub(r'(\S+_DET)(\s+)(\S+_NOUN)',r'\3\2\1',a)
    # modify tags for INDEF, POSS and DEM
    c = re.sub(r'(este|ese|aquel|alguno)(_DET)',r'\1_DEM',b)
    d = re.sub(r'(mi|tu|su|nuestro|vuestro)(_DET)',r'\1_PSS',c)
    e = re.sub(r'(cada|todo|mismo|otro|mucho|tanto|varios)(_DET)',r'\1_IDF',d)
    # all DEM + NOUNs are now flipped, 3 combos only, first DEM NUM NOUN -> NOUN DEM NUM
    f = re.sub(r'(\S+_DEM)(\s)(\S+_NUM)(\s)(\S+_NOUN)',r'\5\4\1\2\3',e)
    # now INDEF NUM NOUN -> NOUN NUM INDEF
    g = re.sub(r'(\S+_IDF)(\s)(\S+_NUM)(\s)(\S+_NOUN)',r'\5\4\3\2\1',f)
    # now possessive constructions
    h = re.sub(r'(\S+_NOUN)(\s)(\S+_PSS)',r'\1\2PROPIO\2\3',g)
    return h

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

#%%

def main():
    pass

if __name__ == '__main__':
    main()







