#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:48:58 2022

@author: euan.mcgill@upf.edu


Rules covered:
    NP order
    Compulsory subject
    Movement of ADVs after the verb
    No articles
    No adpositions (might need to alter to accept 'para')
    Possessive constructions
    Mark plurals with "PLURAL" marker
"""

from model_init import importLM
import re
import spacy as sp
import sys

# model_load = importLM()
# doc = model_load.to_doc("de los treinta a los setenta años se renovará cada diez años")
# testprondoc = model_load.to_doc("debes recoger el denei en el mismo sitio donde tú lo solicistaste")
# doc = model_load.to_doc("una fotocopia del denei también vale si no tienes el original")
# doc = model_load.to_doc("una fotocopia del denei ya no vale si tú no tienes el original")

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
    mortag = []
    for token in doc:
        # get tuples of spaCy tags (combined and individual)
        tagged = (token.lemma_,token.pos_)
        tags_only = (token.dep_)
        lemmas_only = (token.lemma_)
        pos_only = (token.pos_)
        pernum = (token.lemma_, token.pos_,
                  ' '.join(token.morph.get("Person")),
                  ' '.join(token.morph.get("Number")),
                  ' '.join(token.morph.get("Case")))
        # merge lemma and pos tag together as one lexical item, merge verb inflection info
        combine = '_'.join(tagged)
        inflect = '_'.join(pernum)
        # list each type of transcription, then convert to string for analysis
        listag.append(combine)
        deptag.append(tags_only)
        lemtag.append(lemmas_only)
        postag.append(pos_only)
        mortag.append(inflect)
        tagstring = ' '.join(listag)
        depstring = ' '.join(deptag) # only return this one in prep?
        lemstring = ' '.join(lemtag)
        posstring = ' '.join(postag)
        morstring = ' '.join(mortag)
    return tagstring, depstring, lemstring, posstring, morstring

def compulsory_subj(mor):
    # delete ser/estar before or after this stage
    # must also consider negatives w/in the word order
    # tienes que -> necesitar
    # another edge case - reflexive verbs (check)
    # mor = ord_prep(doc)[4]
    # Adverbs go after the verb apart from "no" or "ya no". Move other adverbs
    alpha = re.sub(r'ya_ADV___', r'ya_YA___',mor)
    bravo = re.sub(r'no_ADV___', r'no_NEG___',alpha)
    bc = re.sub(r' Dat\b',r'',bravo)
    charlie = re.sub(r'(\S+_ADV\S+)(\s)(\S+_(VERB|AUX)\S+)',r'\3\2\1',bc)
    # now to the pronouns
    delta = re.sub(r'(\S+(VERB|AUX)_1_Sing_)',r'yo_PRON_1_Sing_Nom \1',charlie)
    echo = re.sub(r'(\S+(VERB|AUX)_2_Sing_)',r'tú_PRON_2_Sing_Nom \1',delta)
    # something to deal with ella, ellas
    foxtrot = re.sub(r'(\S+(VERB|AUX)_3_(Sing|Plur)_)',r'él_PRON_3_Sing_Nom \1',echo)
    golf = re.sub(r'(\S+(VERB|AUX)_1_Plur_)',r'nuestro_PRON_1_Sing_Nom \1',foxtrot)
    hotel = re.sub(r'(\S+(VERB|AUX)_2_Plur_)',r'vuestro_PRON_2_Sing_Nom \1',golf)
    # now move pron before ya no then no
    india = re.sub(r'(\S+NEG\S+)(\s)(\S+PRON\S+)',r'\3\2\1',hotel)
    juliett = re.sub(r'(\S+YA\S+)(\s)(\S+PRON\S+)',r'\3\2\1',india)
    # double prons, get rid of acc prons
    kilo = re.sub(r'(\S+PRON\S+_Acc)',r'',juliett)
    lima = re.sub(r'(\S+PRON\S+_Nom)(\s+)(\S+PRON\S+_Nom)',r'\1',kilo)
    # future/past tense also here
    # what should we do with accusative prons? It'd happen here
    # plurals
    mike = re.sub(r'(\S+NOUN\S+Plur\S+)',r'PLURAL_ADJ___ \1',lima)
    # POSTPROCESSING
    november = re.sub(r'(\S+_\S+)(_\S*_\S*_\S*)',r'\1',mike)
    return november

def np_ord(tag):
    # tag = compulsory_subj(ord_prep(doc)[4])
    #
    # first remove DETs which are (in)definite articles
    a = re.sub(r'(el|uno)_DET ',r'',tag) # ,flags=re.MULTILINE
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
    i = re.sub(r'(\S+_ADP) ',r'',h) # "para" seems to be used in glosses
    # fingerspell proper nouns (or include in OOV checker)
    # POSTPROCESSING
    j = re.sub(r'(\S+)(_\S+)',r'\1',i) # omit j if you want to pass POS to other functions
    k = re.sub(r'_SPACE_',r'',j)
    return k.upper()

def oov_check():
    pass

#%%
'''
Alternative algorithm (a la Vegas Cañas):
    Collect all words in a dict
    Label
    If they match conditional word order, plug them into sentence
'''

#%%


#%%
def main():
    model_load = importLM()
    # infile = '/Users/e.mcgill/Downloads/resignontasknluoverspanish/frases_train_1.txt'
    infile = sys.argv[1]
    # outfile = 'test_output.txt'
    outfile = sys.argv[2]
    with open(infile, 'r', encoding='utf-8') as f, open(outfile, 'w') as w:
        docs = []
        preps = []
        tags = []
        outs = []
        for line in f:
            docs.append(model_load.to_doc(line))
        for doc in docs:
            preps.append(ord_prep(doc)[4])
        for tag in preps:
            tags.append(compulsory_subj(tag))
        for item in tags:
            outs.append(np_ord(item))
        for line in outs:
            w.write(line)

if __name__ == '__main__':
    main()







