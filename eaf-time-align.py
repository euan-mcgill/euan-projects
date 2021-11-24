#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EAF extracter timealign

Created on Wed Nov 24 13:56:10 2021

@author: Euan McGill
"""

import sys
import xml.etree.ElementTree as et

# infile = sys.argv[1] # Uncomment this once dev is done
infile = '/home/upf/Documents/resources/corpora/BSLCP/BF10n.eaf'
rightgloss = []
leftgloss = []
english = []

tree = et.parse(infile)
root = tree.getroot() # ANNOTATION_DOCUMENT

# for child in root:
#     # print(child.tag, child.attrib)
#     for tier in child.findall('ANNOTATION'):
#         for t in tier:
#             print(t.attrib["TIME_SLOT_REF1"], t.attrib["TIME_SLOT_REF2"], [x.text for x in t])

# 
for child in root:
    print(child.tag)