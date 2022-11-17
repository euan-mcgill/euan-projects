#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:04:42 2022

@author: e.mcgill
"""

from calcelec import CalcElec
import matplotlib.pyplot as plt
import numpy as np

six_election = ['electoral_calculus_data/1955.csv', 'electoral_calculus_data/1959.csv', 
                 'electoral_calculus_data/1964.csv', 'electoral_calculus_data/1966.csv', 
                 'electoral_calculus_data/1970.csv', 'electoral_calculus_data/1974f.csv', 
                 'electoral_calculus_data/1974o.csv', 'electoral_calculus_data/1979.csv', 
                 'electoral_calculus_data/1983.csv', 'electoral_calculus_data/1987.csv', 
                 'electoral_calculus_data/1992.csv', 'electoral_calculus_data/1997.csv', 
                 'electoral_calculus_data/2001.csv', 'electoral_calculus_data/2005.csv', ]

eight_election = [ 'electoral_calculus_data/2010.csv', 'electoral_calculus_data/2015.csv', 
                   'electoral_calculus_data/2017.csv', 'electoral_calculus_data/2019.csv', ]

#%%
six_frames = []

eight_frames = []

# ham = CalcElec(infile='electoral_calculus_data/2019.csv', sixparty=False).hamilton()
# dhon = CalcElec(infile='electoral_calculus_data/2019.csv', sixparty=False).dhondt_calc()

for elec in six_election:
    result = CalcElec(infile=elec, sixparty=True).dhondt_calc()
    six_frames.append(result)

for elec in eight_election:
    result = CalcElec(infile=elec, sixparty=False).dhondt_calc(plot=True)
    eight_frames.append(result)

# print(eight_frames[0][0]) # array indices as follows: [con,lab,lib,snp,brx,grn,pcy,uup,sdl,sif,dup,oth,mnr]
print(len(six_frames))

labels = ['2010', '2015', '2017', '2019']
con = np.array([(eight_frames[0][0]),(eight_frames[1][0]),(eight_frames[2][0]),(eight_frames[3][0])])
lab = np.array([(eight_frames[0][1]),(eight_frames[1][1]),(eight_frames[2][1]),(eight_frames[3][1])])
lib = np.array([(eight_frames[0][2]),(eight_frames[1][2]),(eight_frames[2][2]),(eight_frames[3][2])])
brx = np.array([(eight_frames[0][4]),(eight_frames[1][4]),(eight_frames[2][4]),(eight_frames[3][4])])
grn = np.array([(eight_frames[0][5]),(eight_frames[1][5]),(eight_frames[2][5]),(eight_frames[3][5])])
nat = np.array([(eight_frames[0][3])+(eight_frames[0][6]),(eight_frames[1][3])+(eight_frames[1][6]),
       (eight_frames[2][3])+(eight_frames[2][6]),(eight_frames[3][3])+(eight_frames[3][6])])
ni = np.array([(250-con[0]-lab[0]-lib[0]-brx[0]-grn[0]-nat[0]), (250-con[1]-lab[1]-lib[1]-brx[1]-grn[1]-nat[1]),
       (250-con[2]-lab[2]-lib[2]-brx[2]-grn[2]-nat[2]), (250-con[3]-lab[3]-lib[3]-brx[3]-grn[3]-nat[3])])
#width = 0.5
fig, ax = plt.subplots()
ax.bar(labels, con, color='blue')
ax.bar(labels, lib, bottom=con, color='gold')
ax.bar(labels, brx, bottom=con+lib, color='cyan')
ax.bar(labels, grn, bottom=con+lib+brx, color='lime')
ax.bar(labels, nat, bottom=con+lib+brx+grn, color='forestgreen')
ax.bar(labels, ni, bottom=con+lib+brx+grn+nat, color='dimgrey')
ax.bar(labels, lab, bottom=con+lib+brx+grn+nat+ni, color='red')
ax.legend()
plt.axhline(y=125, color='black')
plt.show()
