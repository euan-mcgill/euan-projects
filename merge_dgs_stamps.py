#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:28:51 2022

@author: euan.mcgill@upf.edu
"""

import re

#%%

# dgs_lh = '/home/upf/Downloads/GebxE4rde_l.txt'
# dgs_rh = '/home/upf/Downloads/GebxE4rde_r.txt'
# dgs_both = 'test.txt'
# leftlist = []
# ritelist = []

# with open(dgs_lh, 'r') as lh, open(dgs_rh, 'r') as rh, open(dgs_both, 'w') as out:
#     for line in lh:
#         leftlist.append(line.split())
#     for line in rh:
#         ritelist.append(line.split())
#     # list lens are equal

# #%%

# testleft = leftlist[0:10]
# testright = ritelist[0:10]
# testleft.append()
# testright.append()

#%%

'''
Current prototype starts here

Preprocess empty lines and end of lines to retain sentence structure
'''

# input files
dgs_lh = '/home/upf/Downloads/testleft.txt'
dgs_rh = '/home/upf/Downloads/testright.txt'

# flatten structure and add tags from newline characters so we can reconstruct
with open(dgs_lh, 'r') as lef, open(dgs_rh, 'r') as rih:
    lhlong =" ".join(re.sub('\n',' _SENTENCETAG_',line) for line in lef)
    rhlong =" ".join(re.sub('\n',' _SENTENCETAG_',line) for line in rih)

# split on the word level
leftlist = lhlong.split()
ritelist = rhlong.split()

# z = []
# for line in leftlist:
#     z.append((int(re.search('([0-9]+(?=;))',line).group())))
    


#%%

# lh = []
# rh = []

# for line in leftlist:
#     # this line finds the start time and converts match object to integer
#     lh.append(((int(re.search('([0-9]+(?=;))',line).group())),line))
# for line in ritelist:
#     rh.append(((int(re.search('([0-9]+(?=;))',line).group())),line))


#%%

'''
Convert data to dict format via Regexes accounting for NoneType objects
'''

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
    

'''
Assign NoneType objects a timestamp which is one higher than the previous value
'''

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

#%%

'''
Alignment
'''

for lf,rg in zip(dgs_data['LeftStart'],dgs_data['RightStart']):
    print(lf,rg)

