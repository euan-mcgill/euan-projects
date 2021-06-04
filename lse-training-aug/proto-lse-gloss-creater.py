#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import spacy as sp
# import stanza
import time

def stripandsearch(corpus,writefile):
    '''
Grab sentences between 3 and 12 words in length, remove stage directions in brackets
    '''
    with open(corpus, 'r') as corp, open(writefile, 'w') as out:
        for line in corp:
            brackline = re.sub(r'\(.*\)', '', line) # Remove everything between, and, the brackets
            strline = re.sub(r'[^\w\s]','',brackline) # Remove all punctuation
            res = len(re.findall(r'\w+', strline)) # Get a word count for each line
            if res <= 12 and res >= 3: # Word length between 3-12 exactly
                out.write(strline) # .upper()) # write all lines which meet criteria (in upper case)

def processor(writefile,nlp,glossfile):
    '''
    Language-agnostic gloss rules
    Isolate valid POS and then lemmatise, word order
    permute,randomly remove 1/5, to uppercase
    '''
    with open(writefile, 'r') as wds, open(glossfile, 'w') as out:
        doc = nlp(wds.read())
        # Takes 14 minutes with 27000 line file, full command for reference
        # print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
        '''
        spaCy method:
            Returns a lemmatised version of a token in the file if the POS is from a valid stated category.
            SPACE is included because it carries the \n marker which we will split the list on. Maybe also
            return an aligned list of POS? So can align and do word-order permutation.
        '''
        # We should probably keep proper nouns? Leaves -s endings though for plurals (ignore instead or further postprocessing)
        pos_restrict = ([token.text for token in doc if token.pos_ == 'NOUN' or token.pos_ == 'PROPN' or token.pos_ == 'VERB' or token.pos_ == 'ADJ' or token.pos_ == 'ADV' or token.pos_ == 'NUM' or token.pos_ == 'SPACE'])
        pos_pos = ([token.pos_ for token in doc if token.pos_ == 'NOUN' or token.pos_ == 'PROPN' or token.pos_ == 'VERB' or token.pos_ == 'ADJ' or token.pos_ == 'ADV' or token.pos_ == 'NUM' or token.pos_ == 'SPACE'])
        pos_lemma = ([token.lemma_ for token in doc if token.pos_ == 'NOUN' or token.pos_ == 'PROPN' or token.pos_ == 'VERB' or token.pos_ == 'ADJ' or token.pos_ == 'ADV' or token.pos_ == 'NUM' or token.pos_ == 'SPACE'])
        # Change word order (either verbs to the right or permute up to 4)
        # print(pos_lemma,pos_pos,pos_restrict)
        '''
        To accommodate verbs, we could grab them separately and append to the end of each line in order
        to get SOV word order - also negative particles?
        '''
        for line in pos_lemma:
            out.write(line.upper() + ' ')

### PERMUTATION ###

def wordorder(glossfile, orderfile):
    '''
    Can capture verbs with the regex '\w+[eai]r ' - now need to work positional movement
    (\w+[eai]r )(.*) capture groups then sub \1\2?
    '''
    with open(glossfile, 'r') as gls, open(orderfile, 'w') as lse:
        for line in gls:
            print(re.sub(r'(\w+[EAI]R )(.*)', r'\2\1', line))


def main():
    tick = time.perf_counter() / 60
    corpus = '/Users/e.mcgill/Documents/upf/corpora/TEDtalk-ESCA-MOSES/TED-es-subset.txt'
    writefile = 'TED-es_ES.txt'
    glossfile = 'temp.txt'
    orderfile = 'TED-lse_ES.txt'
    stripandsearch(corpus,writefile)

    # stanza.download('es')
    # nlp = stanza.Pipeline('es', processors='tokenize,mwt,pos,lemma,depparse')
    nlp = sp.load("es_dep_news_trf")
    processor(writefile,nlp,glossfile)

    wordorder(glossfile, orderfile)

    tock = time.perf_counter() / 60
    print(f"\n\n\nGlosses created in {tock - tick:0.0f} minutes\n\n\n")

if __name__ == '__main__':
    main()


