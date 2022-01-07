#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import spacy as sp
# from spacy import displacy

# user_lang = input("Language for processing is:")

# if user_lang == "English" or "english":
#     nlp = sp.load("en_core_web_md")

nlp = sp.load("es_core_news_md")
infile = '/Users/e.mcgill/Documents/upf/corpora/ID-DL-textonly/frases_test.txt'
outfile = 'test.txt'
lexicon = '/Users/e.mcgill/Documents/upf/corpora/lse-sign/LSE-sign-All-Gloss-LSE-sign-linguistic.tsv'

'''
Rules: https://docs.google.com/spreadsheets/d/1rqENxqKFLp4ej3RJFbZBjBi_bMWDmGaaaQJJfCLC7Ec/edit#gid=0
[x]      1) Derivation rule (deriv)
[x]      2) Ser/estar deletion (delatt)
[ ]      3) Proper nouns (propn)
[x]      4) Preposition deletion (delpr)
[ ]      5) NP reordering (np_ord)
[ ]      6) Compulsory subject (subj)
[ ]      7) Compound verbs (compv)
[ ]      8) Time complement with WHEN (cpltime)
[ ]      9) Mode complement with HOW (cplmode)
[ ]     10) Unknown words which don't correspond with lexicon entry (oov_check)
[ ]     11) Emphasis reduplication (rdemph)
[ ]     12) Plural reduplication (rdpl) - in ID/DL marked PLURAL + GLOSS
[ ]     13) Possessive structure with PROPIO (poss)
[ ]    14a) Negation syntax (neg_)
[ ]    14b) Negation syntax (neg_)
[ ]     15) Topic-comment structure (topic)
[x]     16) Gloss capitalisation (caps)
[ ]     17) No articles (art)
[ ]     18) Future tense marking with FUTURO+INF (fut)
[ ]     19) 'General rules' for gloss augmentation from Amit's paper (gen_0)
[ ]     20) Synonym finder, closest word in something like WordNet if OOV flags a synthesised gloss as not existing (syn)
'''

# XPOS not available for any Spanish models for fine grained POS tags
# effect on rule (17)
#%%
def do_rules():
    doc = nlp('los grandes inválidos y enfermos psiquiátricos no están obligados a renovar el denei')
    '''
    Here is the best place to do the syntactic, semantic role and word order rules. Using spacy's
    dep and morph functionalities before you filter by pos_. Must also all be in the same loop
    '''

    deriv = [token.lemma_ for token in doc                        # covers rule (1)
                                           if token.pos_ == 'ADJ' # Adjective
                                           # or token.pos_ == 'ADP' # Preposition # covers rule (4)
                                           or token.pos_ == 'ADV' # Adverb
                                           or token.pos_ == 'AUX' # Auxiliary verb
                                           or token.pos_ == 'CCONJ' # Coordinating conjunction
                                           or token.pos_ == 'DET' # Determiner # too broad for articles rule
                                           or token.pos_ == 'INTJ' # Interjection
                                           or token.pos_ == 'NOUN' # Noun
                                           or token.pos_ == 'NUM' # Numeral
                                           or token.pos_ == 'PART' # Particle
                                           or token.pos_ == 'PRON' # Pronoun
                                           or token.pos_ == 'PROPN' # Proper Noun
                                           or token.pos_ == 'PUNCT' # Punctuation
                                           or token.pos_ == 'SCONJ' # Subordinating conjunction
                                           or token.pos_ == 'SYM' # Symbols
                                           or token.pos_ == 'VERB' # Verbs
                                           or token.pos_ == 'X'] # Other
    for token in deriv:
        delatt = re.sub(r'\b(ser|estar)\b','',token) # covers rule (2)
        '''
        Now remove lemmatised aritcles, just 'el' for definite (check he/his is accented still)
        '''
        print(delatt.upper()) # covers rule (16)
    
    # print("Run control+C to close\n\n")
    # displacy.serve(doc, style="dep")
#%%
def do_rules():
    doc = nlp('está mi padre')
    
    labelled = [token.dep_ for token in doc]
    print(labelled)
#%%
'''
OOV checker and synonym finder with Word2Vec
'''
# find unique dict items
def oov_check():
    pass

# last rule - convert to .upper()
# run in cmd line with > .txt file for file output

#%%
do_rules()


