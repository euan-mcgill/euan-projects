#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spacy
from spacy import displacy

nlp = spacy.load("es_core_news_lg")
doc = nlp("cuando vuelvas a vivir aquí tendrás que traer un certificado del padrón municipal al renovarte el denei")
displacy.serve(doc, style="dep")

# to close process:
# ctrl+C, or...
# sudo lsof -i:5000
# kill $PID
