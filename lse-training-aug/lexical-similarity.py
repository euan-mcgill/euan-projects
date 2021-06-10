#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

'''
I used find+replace in the original versions of these files to put 
all words on one line for ease of processing
'''

# Remove all puncutation, and then create a unique set
def setoverlap(lse_corpus,spanish_corpus):
    with open(lse_corpus,'r') as lse:
        for line in lse:
            lse_wordonly = re.sub(r'[^\w\s]','',line.lower())
            lse_wordlist = lse_wordonly.split()
            lse_unique = set(lse_wordlist)

    with open(spanish_corpus,'r') as esp:
        for line in esp:
            esp_wordonly = re.sub(r'[^\w\s]','',line)
            esp_wordlist = esp_wordonly.split()
            esp_unique = set(esp_wordlist)

    # print(len(esp_unique))
    # print(len(esp_unique.intersection(lse_unique)))
    print(f"\nLexical similarity of LSE to Spanish in BD dataset: {len(esp_unique.intersection(lse_unique))/len(esp_unique)*100:0.2f}%") #(N= {len(esp_unique)})")
    # print(f"Lexical similarity of Spanish to LSE in BD dataset: {len(lse_unique.intersection(esp_unique))/len(lse_unique)*100:0.2f}% (N= {len(lse_unique)})")
    print(f"Spanish corpus size: {len(esp_wordlist)}, LSE corpus size: {len(lse_wordlist)}\n") # crosschecked with 'wc -w' on the command line

def main():
    lse_corpus = '/Users/e.mcgill/Documents/upf/corpora/UPM-LSE/BD/TEXTOS/signos-allwords.txt'
    # maybe use .lower() with this
    spanish_corpus = '/Users/e.mcgill/Documents/upf/corpora/UPM-LSE/BD/TEXTOS/frases-allwords.txt'

    setoverlap(lse_corpus,spanish_corpus)

if __name__ == '__main__':
    main()