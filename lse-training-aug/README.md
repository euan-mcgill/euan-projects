# Project design
    Designing a rule-based data augmentation routine which creates LSE training data from Spanish corpus data, based on the process outlined in a study where DGT data is drawn from German corpus data (Moryossef et al., 2021).
    Plenty of free corpora (including parallel) avialable at OPUS project https://opus.nlpl.eu/index.php
    Extant grammars, lexica, and info about the structure of Lengua de Señas Española at Glottolog https://glottolog.org/resource/languoid/id/span1263

## 1) Spanish plain text corpus
    Preprocessing:
        - Ensure utterances are <= 9 words
        - Special symbols etc.
        - to uppercase

## 2) General gloss rules (language-agnostic)
    - Remove 1/5 of the training data at random (done first to reduce computing time)
    - POS-filter to {NOUN, VERB, ADJECTIVE, ADVERB, NUMERAL}
    - Lemmatise all words
    - Random word permutation (max distance = 4)

## 3) LSE specific rules
    - (S)OV word order
    - Question and negation particles
    - Synonym mapping
    - Verification of existing sign^

## X) ^LSE grammar and lexicon lookup resources
    - 

## Y) Calculate lexical and syntactic similarity
    -

