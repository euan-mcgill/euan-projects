#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contextualSpellCheck
import json
import re
import spacy as sp

def load_data(infile, plainfile):
    with open(infile, 'r') as asr_output, open(plainfile, 'w') as out:
        data = json.load(asr_output)
        for utt in data:
            #print(utt['Utterance']) # plain text of the utterances
            out.write(utt['Utterance']+'\n')

def pipeline(plainfile,nlp):
    with open(plainfile,'r') as wds:
        doc = nlp(wds.read())
        doc._.performed_spellCheck #Should be True
        print(doc._.outcome_spellCheck)
        for token in doc:
            print(token.text,token.tag_,token.dep_)

def main():
    '''
    '''
    infile = 'test-nlp.json'
    plainfile = 'test-nlp.txt'
#    nlp = sp.load("en_core_web_trf") # English only
    # if input()
    nlp = sp.load("en_core_web_lg") # English only -large
#    nlp = sp.load("xx_sent_ud_sm") # multi-language
#    nlp = sp.load("xx_ent_wiki_sm") # multi-language
    contextualSpellCheck.add_to_pipe(nlp) # size 436MB w/ en_core_web_lg
                                          # must occur before tok and other p'line elements
                                          # see also https://spacy.io/universe/project/spacy_hunspell
                                          # for spelling suggestions
    load_data(infile,plainfile)
    pipeline(plainfile,nlp)

if __name__ == '__main__':
    main()