#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OOV-checker

Created on Fri Jan  7 16:26:43 2022

@author: upf
"""

import re
# import spacy as sp

def oov_check():
    wordbank = []
    with open('arasaac_lexicon.txt') as lex:
        for line in lex:
            wordbank.append(line)
    return wordbank
            
