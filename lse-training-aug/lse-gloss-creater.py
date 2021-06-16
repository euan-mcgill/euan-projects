#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import spacy as sp
import sys
import time

'''
Create training data through rule-based DATA AUGMENTATION for sign language 
glosses (Lengua de Señas Española). Spanish language data is stripped of punc-
tuation and non-speech transcription. Next, it is restricted by POS tags and 
lemmatised. Then verbs are moved to the end of an utterance iteratively for up
to three verbs per sentence.

Running instructions: 'python3 lse-gloss-creater.py <INPUT-CORPUS-FILE>'
'''

def stripandsearch(corpus,writefile):
    '''
Grab sentences between 3 and 12 words in length,
remove stage directions in brackets
    '''
    with open(corpus, 'r') as corp, open(writefile, 'w') as out:
        for line in corp:
            brackline = re.sub(r'\(.*\)', '', line)
            strline = re.sub(r'[^\w\s]','',brackline)
            res = len(re.findall(r'\w+', strline))
            if res <= 12 and res >= 3:
                out.write(strline)

def processor(writefile,nlp,glossfile):
    '''
    Language-agnostic gloss rules
    Isolate valid POS and then lemmatise, word order
    permute,randomly remove 1/5, to uppercase
    '''
    with open(writefile, 'r') as wds, open(glossfile, 'w') as out:
        doc = nlp(wds.read())
        pos_lemma = ([token.lemma_ for token in doc if token.pos_ == 'NOUN' 
                                                    or token.pos_ == 'PROPN' 
                                                    or token.pos_ == 'PRON'
                                                    or token.pos_ == 'VERB' 
                                                    or token.pos_ == 'ADJ' 
                                                    or token.pos_ == 'ADV' 
                                                    or token.pos_ == 'CCONJ´'
                                                    or token.pos_ == 'NUM' 
                                                    or token.pos_ == 'SPACE'])
        for line in pos_lemma:
            out.write(line.upper() + ' ')

def wordorder(glossfile, orderfile):
    '''
    Using a capture group to place verbs at the end of the sentence
    '''
    with open(glossfile, 'r') as gls, open(orderfile, 'w') as lse:
        for line in gls:
            switchline = re.sub(r'(\w+[EAI]R )(.*)', r'\2\1', line)
            res = len(re.findall(r'\w+', switchline))
            if res >= 3:
                lse.write(switchline)

def main():
    tick = time.perf_counter() / 60
    corpus = '/home/upf/Documents/resources/corpora/TED-talks-2020/ca-ES-es-ES/TED-es-subset.txt' # sys.argv[1]
    writefile = 'temp1-ES.txt'
    glossfile = 'temp2-glosses.txt'
    orderfile = 'temp3-word-order.txt'

    stripandsearch(corpus,writefile)

    nlp = sp.load("es_dep_news_trf")
    processor(writefile,nlp,glossfile)
    wordorder(glossfile, orderfile)

    tock = time.perf_counter() / 60
    print(f"\n\n\nGlosses created in {tock - tick:0.0f} minutes\n\n\n")

if __name__ == '__main__':
    main()

