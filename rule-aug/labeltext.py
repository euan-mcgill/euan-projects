#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:28:47 2022

@author: upf
"""

import re
import spacy as sp

class augrules:
    
    def __init__(self,doc,nlp,conll_dict):
        self.nlp = sp.load("es_core_news_lg")
        self.doc = nlp("con tu denei puedes viajar a estos países")
        self.conll_dict = {'ID':[], 'FORM':[], 
                      'LEMMA':[], 'UPOSTAG':[],
                      'XPOSTAG':[], 'FEATS':[],
                      'HEAD':[], 'DEPREL':[],
                      'DEPS':[], 'MISC':[]}

    def labelit(self):
        
        for i,token in enumerate(self.doc): # now output to JSON with CoNLL-U column order
            self.conll_dict['ID'].append(i+1)
            self.conll_dict['FORM'].append(str(token))
            self.conll_dict['LEMMA'].append(str(token.lemma_))
            self.conll_dict['UPOSTAG'].append(str(token.pos_))
            self.conll_dict['XPOSTAG'].append(str(token.tag_))
            self.conll_dict['FEATS'].append(str(token.morph))
            self.conll_dict['HEAD'].append(token.head.i+1) # this may need more processing, check output manually
            self.conll_dict['DEPREL'].append(token.dep_)
            self.conll_dict['DEPS'].append(None)
            self.conll_dict['MISC'].append(None)
            # jsondict = [dict(zip(conll_dict.keys(),i)) for i in zip(*conll_dict.values())]
            outdict = self.conll_dict
            
            # return outdict
                        
    