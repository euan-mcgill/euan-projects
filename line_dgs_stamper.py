#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:57:38 2022

@author: euan.mcgill@upf.edu

WIP: code works run in parts, but not as a whole
"""
import re

# dgs_lh = '/home/upf/Downloads/testleft.txt' # ensure there's an "END_OF_FILE*<9999;9999>" tag on the final line
# dgs_rh = '/home/upf/Downloads/testright.txt'
dgs_lh = '/home/upf/Downloads/GebxE4rde_l.txt' # ensure there's an "END_OF_FILE*<9999;9999>" tag on the final line
dgs_rh = '/home/upf/Downloads/GebxE4rde_r.txt'


def preprocess(dgs_lh,dgs_rh):
    with open(dgs_lh,'r+') as lh:
        flat_list_l = [re.sub('\n',' _SENTENCETAG_',line) for line in lh]
        lh.seek(0)
        for line in flat_list_l:
            for seq in line.split():
                y = re.sub(r'(.+[\^\*])(?=<\d+;\d+>)',r' \1_VOID',seq)
                z = re.sub(r'_SENTENCETAG_',r'_SENTENCETAG_ ',y)
                lh.write(z)
                lh.truncate()
    with open(dgs_rh,'r+') as rh:
        flat_list_r = [re.sub('\n',' _SENTENCETAG_',line) for line in rh]
        rh.seek(0)
        for line in flat_list_r:
            for seq in line.split():
                y = re.sub(r'(.+[\^\*])(?=<\d+;\d+>)',r' VOID_\1',seq)
                z = re.sub(r'_SENTENCETAG_',r'_SENTENCETAG_ ',y)
                rh.write(z)
                rh.truncate()

def joinhands(dgs_lh,dgs_rh):
    preprocess(dgs_lh, dgs_rh)
    with open(dgs_lh,'r+') as lh, open(dgs_rh, 'r+') as rh:
        for line in lh:
            eachline_l = line.split('_SENTENCETAG_')
        for line in rh:
            eachline_r = line.split('_SENTENCETAG_')
    line_by_line = [' '.join(i) for i in zip(eachline_l, eachline_r)]
    list_by_line = [item.split() for item in line_by_line]
    # THIS WORKS! All lines in order by timestamp - now to edit matches
    for line in list_by_line:
        line.sort(key= lambda item: int(re.search('([0-9]+(?=;))',item).group()))
        # consider a try except Attribute error if issues persist
    return list_by_line

def align():
    list_by_line = joinhands(dgs_lh,dgs_rh) # not currently working all in one
    align_file = 'dgs_aligned.txt'
    with open(align_file,'w') as ta:
        for line in list_by_line:
            line.append('ENDOFLINE*<9999999;9999999>') # dummy tag so we can see the last tag on each line
            new_line = []
            for seq,nextseq in zip(line,line[1:]):
                if int(re.search('([0-9]+(?=;))',seq).group()) == int((re.search('([0-9]+(?=;))',nextseq).group())) and int(re.search('(?<=;)([0-9]+)',seq).group()) == int((re.search('(?<=;)([0-9]+)',nextseq).group())):
                    new_line.append(f'{seq}{nextseq}')
                else:
                    new_line.append(seq)
            print(" ".join(new_line),file=ta)

def postproc(aligned_file): 
# aligned_file should be the same as the print command file='' above
    with open(aligned_file, 'r+') as af:
        af.seek(0)
        for line in af:
            merged = re.sub('(_\S+<\d+;\d+>\S+_)','_',line) # ça marche
            af.write(merged)
            af.truncate()


'''
Add main() function so you can run on the command line (align() then postproc())
'''



