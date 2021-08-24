#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("the fat cat sat on the mat")
displacy.serve(doc, style="dep")

# to close process:
# ctrl+C, or...
# sudo lsof -i:5000
# kill $PID
