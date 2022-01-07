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


''' 
Extracts timestamp references and transcriptions for right-
hand glosses, left-hand glosses and English text

This recreates View>Annotation Spreadsheet inside of ELAN
'''

for child in root.findall("TIER"):
    # print(child.attrib["TIER_ID"])
    if child.attrib["TIER_ID"] == "RH-IDgloss":
        for tier in child.findall('ANNOTATION'):
            for t in tier:
                rightgloss.append([t.attrib["TIME_SLOT_REF1"], t.attrib["TIME_SLOT_REF2"], [x.text for x in t]])
    elif child.attrib["TIER_ID"] == "LH-IDgloss":
        for tier in child.findall('ANNOTATION'):
            for t in tier:
                leftgloss.append([t.attrib["TIME_SLOT_REF1"], t.attrib["TIME_SLOT_REF2"], [x.text for x in t]])
    elif child.attrib["TIER_ID"] == "Free Translation":
        for tier in child.findall('ANNOTATION'):
            for t in tier:
                english.append([t.attrib["TIME_SLOT_REF1"], t.attrib["TIME_SLOT_REF2"], [x.text for x in t]])
    else:
        continue

# Now we need to retrieve the realtime values
# for left,right,eng in zip(leftgloss,rightgloss,english):
#     print(left,'\t',right,'\t',eng)
print(len(leftgloss),len(rightgloss),len(english))