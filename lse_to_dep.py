#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:10:17 2022

@author: euan.mcgill@upf.edu
"""

import re
import spacy as sp
import sys

def lse_to_dep(file,output,tag):
    nlp = sp.load("es_dep_news_trf")
    lselines = []
    deplines = []
    with open(file,'r') as lse, open(output,'w') as out:
        for line in lse:
            new = re.sub('\n','',line)
            lselines.append(new)
        # docs = list(nlp.pipe(lselines))
        for doc in nlp.pipe(lselines):
            if tag == "pos":
                deplines.append([token.pos_ for token in doc])
            elif tag == "morph":
                deplines.append([token.morph for token in doc])
            elif tag == "tag":
                deplines.append([token.tag_ for token in doc])
            elif tag == "text":
                deplines.append([token.text for token in doc])
            else:
                deplines.append([token.dep_ for token in doc])
        for lst in deplines:
            print(*lst,file=out)

def main():
    print('''
    Running instructions: python lse_to_dep.py <Spanish file> <Output name> <tag type>
          ''')
    file = sys.argv[1]
    output = sys.argv[2]
    tag = sys.argv[3]
    lse_to_dep(file,output,tag)

#%%

if __name__ == '__main__':
    main()
