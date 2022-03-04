#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:48:58 2022

@author: euan.mcgill@upf.edu
"""

import re
import spacy as sp

nlp = sp.load("es_dep_news_trf")

doc = nlp("Esas cinco personas son españolas")
#%%

'''
ALGORITHM
Split into sentences then rearrange the noun chunks
'''
for chunk in doc.noun_chunks:
    for token in chunk:
        print(token.dep_,token.pos_)
