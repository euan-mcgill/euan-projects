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
    '''
    Lang2Vec uses ISO 639-3 codes
    '''
    # lse_features = l2v.get_features("ssp", "syntax_knn")
    # es_features = l2v.get_features("spa", "syntax_knn")
    cosine = l2v.distance("syntactic","ase","eng")
    # print(l2v.syntactic_distance("spa","ssp")) # same as cmd above
    print(f'syntactic distance is: {l2v.syntactic_distance("spa","ssp")},\ngeographic distance is: {l2v.geographic_distance("spa","ssp")},\nphonological distance is: {l2v.phonological_distance("spa","ssp")},\ngenetic distance is: {l2v.genetic_distance("spa","ssp")},\ninventory distance is: {l2v.inventory_distance("spa","ssp")},\nfeatural distance is: {l2v.featural_distance("spa","ssp")}')
    # return(cosine)
    print(cosine)

syntactic_sim()