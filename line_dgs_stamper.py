#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:57:38 2022

@author: upf
"""
import re

dgs_lh = '/home/upf/Downloads/testleft.txt'
dgs_rh = '/home/upf/Downloads/testright.txt'

def preprocess(dgs_lh,dgs_rh):
    with open(dgs_lh,'r') as lh:
        flat_list_l = [re.sub('\n','NEWLINE',line) for line in lh]
    with open(dgs_rh,'r+') as rh:
        flat_list_r = [re.sub('\n',' _SENTENCETAG_',line) for line in rh]
        rh.seek(0)
        for line in flat_list_r:
            for seq in line.split():
                y = re.sub(r'(.+[\^\*])(?=<\d+;\d+>)',r' VOID_\1',seq)
                z = re.sub(r'_SENTENCETAG_',r'_SENTENCETAG_ ',y)
                rh.write(z)
                rh.truncate()
    
    with open('test.txt','r+') as test: # CHANGE NAMES
        for line in test:
            print(line.split())
    
    
    
    
    # work "newline" processing into here
    # with open(dgs_rh,'r') as rh, open('test.txt','w') as out:
    #     for line in rh:
    #         for seq in line.split():
    #             y = re.sub(r'(.+[\^\*])(?=<\d+;\d+>)',r'VOID_\1',seq)
    #             out.write(y)