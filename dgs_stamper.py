#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:41:15 2022

@author: e.mcgill
"""

import re

def preproc(dgs_lh,dgs_rh):
    # flatten structure and add tags from newline characters so we can reconstruct
    with open(dgs_lh, 'r') as lef, open(dgs_rh, 'r') as rih:
        lhlong =" ".join(re.sub('\n',' _SENTENCETAG_',line) for line in lef)
        rhlong =" ".join(re.sub('\n',' _SENTENCETAG_',line) for line in rih)
    # split on the word level
    leftlist = lhlong.split()
    ritelist = rhlong.split()
    # Convert data to dict format via Regexes accounting for NoneType objects
    dgs_data = {'Left': [], 'Right': [], 'LeftStart': [], 'RightStart': [],
                'LeftEnd': [], 'RightEnd': []}
    for line in leftlist:
        dgs_data['Left'].append(str(re.match('^[^<]+', line).group()))
        try:
            dgs_data['LeftStart'].append(int(re.search('([0-9]+(?=;))',line).group()))
        except AttributeError:
            dgs_data['LeftStart'].append(0)
        try:
            dgs_data['LeftEnd'].append(int(re.search('((?<=;)[0-9]+)',line).group()))
        except:
            dgs_data['LeftEnd'].append(0)
    for line in ritelist:
        dgs_data['Right'].append(str(re.match('^[^<]+', line).group()))
        try:
            dgs_data['RightStart'].append(int(re.search('([0-9]+(?=;))',line).group()))
        except AttributeError:
            dgs_data['RightStart'].append(0)
        try:
            dgs_data['RightEnd'].append(int(re.search('((?<=;)[0-9]+)',line).group()))
        except:
            dgs_data['RightEnd'].append(0)
        prev_line = line
    # Assign NoneType objects a timestamp which is one higher than the previous value
    for i,line in enumerate(dgs_data['LeftStart']):
        if line != 0:
            last_number = line
            last_number_index = i
            continue
        else:
            dgs_data['LeftStart'][i] = last_number + i - last_number_index

    for i,line in enumerate(dgs_data['LeftEnd']):
        if line != 0:
            last_number = line
            last_number_index = i
            continue
        else:
            dgs_data['LeftEnd'][i] = last_number + i - last_number_index

    for i,line in enumerate(dgs_data['RightStart']):
        if line != 0:
            last_number = line
            last_number_index = i
            continue
        else:
            dgs_data['RightStart'][i] = last_number + i - last_number_index

    for i,line in enumerate(dgs_data['RightEnd']):
        if line != 0:
            last_number = line
            last_number_index = i
            continue
        else:
            dgs_data['RightEnd'][i] = last_number + i - last_number_index
    return dgs_data

def timesort():
    x = preproc('/Users/e.mcgill/Downloads/testleft.txt',
                '/Users/e.mcgill/Downloads/testright.txt')
    l_tags = [re.sub(r'([\W\w]+)',r'VOID_\1',line) for line in x['Left']]
    r_tags = [re.sub(r'([\W\w]+)',r'\1_VOID',line) for line in x['Right']]
    tupesl = zip(x['LeftStart'],x['LeftEnd'],l_tags)
    tupesr = zip(x['RightStart'],x['RightEnd'],r_tags)
    tag_times = []
    for line in tupesl:
        tag_times.append(line)
    for line in tupesr:
        tag_times.append(line)
    ordered_tag_times = sorted(tag_times)
    return ordered_tag_times

def align():
    y = timesort()
    for a,b in zip(y,y[1:]): # for list item and list item immediately after
        # print(a[0],b[0])
        if a[0] == b[0] and a[1] == b[1]: # if the start time and end time are the same as the next one's
            print(f'<{a[0]};{a[1]}>{a[2]}{b[2]}')
        else:
            print(f'<{a[0]};{a[1]}>{a[2]}') # add "end of file" line to avoid omission

def postproc():
    pass




