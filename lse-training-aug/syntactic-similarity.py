#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
c.f. https://pypi.org/project/lang2vec/
'''

import lang2vec.lang2vec as l2v

# get available langs:
# print(l2v.available_uriel_languages())
# print(len(l2v.available_languages()))
# print(len(l2v.available_feature_sets()))

def syntactic_sim():
    print("hello world")
    features = l2v.get_features("lse", "syntax_sswl")
    print(features["lse"])

syntactic_sim()