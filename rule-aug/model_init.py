#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:48:58 2022

@author: euan.mcgill@upf.edu
"""

import spacy as sp

class importLM():
    def __init__(self):
        self.nlp = sp.load("es_dep_news_trf")
