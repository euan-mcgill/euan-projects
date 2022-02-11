#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 18:20:08 2022

@author: e.mcgill
"""

# import numpy as np
from iteround import saferound
import pandas as pd
import sys

data = pd.read_csv('electoral_calculus_data/1955.csv',delimiter=';')
# run on cmd line
# data = pd.read_csv(sys.argv[1],delimiter=';')

#%%
'''
This section grabs total electorate and votes for each specified party in each
of the twelve regions/countries.

This format works for 1955-2005
'''

# 1 = Northern Ireland
uup_ni = data.loc[data['Area'] == 1, 'CON'].sum()
sdl_ni = data.loc[data['Area'] == 1, 'LAB'].sum()
dup_ni = data.loc[data['Area'] == 1, 'LIB'].sum()
sif_ni = data.loc[data['Area'] == 1, 'NAT'].sum()
mnr_ni = data.loc[data['Area'] == 1, 'MIN'].sum()
oth_ni = data.loc[data['Area'] == 1, 'OTH'].sum()
tot_votes_ni = uup_ni + sdl_ni + dup_ni + sif_ni + mnr_ni + oth_ni
elec_ni = data.loc[data['Area'] == 1, 'Electorate'].sum()

# 2 = Scotland
con_sc = data.loc[data['Area'] == 2, 'CON'].sum()
lab_sc = data.loc[data['Area'] == 2, 'LAB'].sum()
lib_sc = data.loc[data['Area'] == 2, 'LIB'].sum()
nat_sc = data.loc[data['Area'] == 2, 'NAT'].sum()
mnr_sc = data.loc[data['Area'] == 2, 'MIN'].sum()
oth_sc = data.loc[data['Area'] == 2, 'OTH'].sum()
tot_votes_sc = con_sc + lab_sc + lib_sc + nat_sc + mnr_sc + oth_sc
elec_sc = data.loc[data['Area'] == 2, 'Electorate'].sum()

# 3 = North East
con_ne = data.loc[data['Area'] == 3, 'CON'].sum()
lab_ne = data.loc[data['Area'] == 3, 'LAB'].sum()
lib_ne = data.loc[data['Area'] == 3, 'LIB'].sum()
nat_ne = data.loc[data['Area'] == 3, 'NAT'].sum()
mnr_ne = data.loc[data['Area'] == 3, 'MIN'].sum()
oth_ne = data.loc[data['Area'] == 3, 'OTH'].sum()
tot_votes_ne = con_ne + lab_ne + lib_ne + nat_ne + mnr_ne + oth_ne
elec_ne = data.loc[data['Area'] == 3, 'Electorate'].sum()

# 4 = North West
con_nw = data.loc[data['Area'] == 4, 'CON'].sum()
lab_nw = data.loc[data['Area'] == 4, 'LAB'].sum()
lib_nw = data.loc[data['Area'] == 4, 'LIB'].sum()
nat_nw = data.loc[data['Area'] == 4, 'NAT'].sum()
mnr_nw = data.loc[data['Area'] == 4, 'MIN'].sum()
oth_nw = data.loc[data['Area'] == 4, 'OTH'].sum()
tot_votes_nw = con_nw + lab_nw + lib_nw + nat_nw + mnr_nw + oth_nw
elec_nw = data.loc[data['Area'] == 4, 'Electorate'].sum()

# 5 = Yorkshire and Humber
con_yh = data.loc[data['Area'] == 5, 'CON'].sum()
lab_yh = data.loc[data['Area'] == 5, 'LAB'].sum()
lib_yh = data.loc[data['Area'] == 5, 'LIB'].sum()
nat_yh = data.loc[data['Area'] == 5, 'NAT'].sum()
mnr_yh = data.loc[data['Area'] == 5, 'MIN'].sum()
oth_yh = data.loc[data['Area'] == 5, 'OTH'].sum()
tot_votes_yh = con_yh + lab_yh + lib_yh + nat_yh + mnr_yh + oth_yh
elec_yh = data.loc[data['Area'] == 5, 'Electorate'].sum()

# 6 = Cymru
con_cy = data.loc[data['Area'] == 6, 'CON'].sum()
lab_cy = data.loc[data['Area'] == 6, 'LAB'].sum()
lib_cy = data.loc[data['Area'] == 6, 'LIB'].sum()
nat_cy = data.loc[data['Area'] == 6, 'NAT'].sum()
mnr_cy = data.loc[data['Area'] == 6, 'MIN'].sum()
oth_cy = data.loc[data['Area'] == 6, 'OTH'].sum()
tot_votes_cy = con_cy + lab_cy + lib_cy + nat_cy + mnr_cy + oth_cy
elec_cy = data.loc[data['Area'] == 6, 'Electorate'].sum()

# 7 = West Midlands
con_wm = data.loc[data['Area'] == 7, 'CON'].sum()
lab_wm = data.loc[data['Area'] == 7, 'LAB'].sum()
lib_wm = data.loc[data['Area'] == 7, 'LIB'].sum()
nat_wm = data.loc[data['Area'] == 7, 'NAT'].sum()
mnr_wm = data.loc[data['Area'] == 7, 'MIN'].sum()
oth_wm = data.loc[data['Area'] == 7, 'OTH'].sum()
tot_votes_wm = con_wm + lab_wm + lib_wm + nat_wm + mnr_wm + oth_wm
elec_wm = data.loc[data['Area'] == 7, 'Electorate'].sum()

# 8 = East Midlands
con_em = data.loc[data['Area'] == 8, 'CON'].sum()
lab_em = data.loc[data['Area'] == 8, 'LAB'].sum()
lib_em = data.loc[data['Area'] == 8, 'LIB'].sum()
nat_em = data.loc[data['Area'] == 8, 'NAT'].sum()
mnr_em = data.loc[data['Area'] == 8, 'MIN'].sum()
oth_em = data.loc[data['Area'] == 8, 'OTH'].sum()
tot_votes_em = con_em + lab_em + lib_em + nat_em + mnr_em + oth_em
elec_em = data.loc[data['Area'] == 8, 'Electorate'].sum()

# 9 = East Anglia
con_ea = data.loc[data['Area'] == 9, 'CON'].sum()
lab_ea = data.loc[data['Area'] == 9, 'LAB'].sum()
lib_ea = data.loc[data['Area'] == 9, 'LIB'].sum()
nat_ea = data.loc[data['Area'] == 9, 'NAT'].sum()
mnr_ea = data.loc[data['Area'] == 9, 'MIN'].sum()
oth_ea = data.loc[data['Area'] == 9, 'OTH'].sum()
tot_votes_ea = con_ea + lab_ea + lib_ea + nat_ea + mnr_ea + oth_ea
elec_ea = data.loc[data['Area'] == 9, 'Electorate'].sum()

# 10 = South West
con_sw = data.loc[data['Area'] == 10, 'CON'].sum()
lab_sw = data.loc[data['Area'] == 10, 'LAB'].sum()
lib_sw = data.loc[data['Area'] == 10, 'LIB'].sum()
nat_sw = data.loc[data['Area'] == 10, 'NAT'].sum()
mnr_sw = data.loc[data['Area'] == 10, 'MIN'].sum()
oth_sw = data.loc[data['Area'] == 10, 'OTH'].sum()
tot_votes_sw = con_sw + lab_sw + lib_sw + nat_sw + mnr_sw + oth_sw
elec_sw = data.loc[data['Area'] == 10, 'Electorate'].sum()

# 11 = London
con_ld = data.loc[data['Area'] == 11, 'CON'].sum()
lab_ld = data.loc[data['Area'] == 11, 'LAB'].sum()
lib_ld = data.loc[data['Area'] == 11, 'LIB'].sum()
nat_ld = data.loc[data['Area'] == 11, 'NAT'].sum()
mnr_ld = data.loc[data['Area'] == 11, 'MIN'].sum()
oth_ld = data.loc[data['Area'] == 11, 'OTH'].sum()
tot_votes_ld = con_ld + lab_ld + lib_ld + nat_ld + mnr_ld + oth_ld
elec_ld = data.loc[data['Area'] == 11, 'Electorate'].sum()

# 12 = South East
con_se = data.loc[data['Area'] == 12, 'CON'].sum()
lab_se = data.loc[data['Area'] == 12, 'LAB'].sum()
lib_se = data.loc[data['Area'] == 12, 'LIB'].sum()
nat_se = data.loc[data['Area'] == 12, 'NAT'].sum()
mnr_se = data.loc[data['Area'] == 12, 'MIN'].sum()
oth_se = data.loc[data['Area'] == 12, 'OTH'].sum()
tot_votes_se = con_se + lab_se + lib_se + nat_se + mnr_se + oth_se
elec_se = data.loc[data['Area'] == 12, 'Electorate'].sum()

#%%

'''
Calculate seats at the given election, given the size of the electorate. Total
must not exceed 250 nationwide. Allocate proportionally to each region.
'''

elec_tot = int(elec_ni + elec_sc + elec_ne + elec_nw + elec_yh + elec_cy + 
               elec_wm + elec_em + elec_ea + elec_sw + elec_ld + elec_se)

raw_seats = [float((elec_ni/elec_tot)*250), float((elec_sc/elec_tot)*250),
              float((elec_ne/elec_tot)*250), float((elec_nw/elec_tot)*250),
              float((elec_yh/elec_tot)*250), float((elec_cy/elec_tot)*250),
              float((elec_wm/elec_tot)*250), float((elec_em/elec_tot)*250),
              float((elec_ea/elec_tot)*250), float((elec_sw/elec_tot)*250),
              float((elec_ld/elec_tot)*250), float((elec_se/elec_tot)*250)]

# Seat numbers for each region
rnd_seats = saferound(raw_seats, places=0)

seats_ni = rnd_seats[0]
seats_sc = rnd_seats[1]
seats_ne = rnd_seats[2]
seats_nw = rnd_seats[3]
seats_yh = rnd_seats[4]
seats_cy = rnd_seats[5]
seats_wm = rnd_seats[6]
seats_em = rnd_seats[7]
seats_ea = rnd_seats[8]
seats_sw = rnd_seats[9]
seats_ld = rnd_seats[10]
seats_se = rnd_seats[11]

if seats_cy ++ seats_ea ++ seats_em ++ seats_ld ++ seats_ne ++ seats_ni ++ seats_nw ++ seats_sc ++ seats_se ++ seats_sw ++ seats_wm ++ seats_yh  == 250:
    print("Seat total valid \n\n\n")
else:
    print("Seat total does not equal 250")

#%%

'''
Or, take seats based on most recent census calculation
'''

pop_seats_ni = {'1931': 8, '1951': 7, '1961': 7, '1971': 0, '1981': 7,
                '1991': 0, '2001': 0, '2011': 0}

pop_seats_sc = {'1931': 31, '1951': 25, '1961': 24, '1971': 0, '1981': 7,
                '1991': 0, '2001': 0, '2011': 0}

#%%

'''
Calculate an election

use seats_xx for electorate-based
OR
use pop_seats_['year'] for census calc (requires editing file for now)


Each region...
'''

ni = saferound([(uup_ni/tot_votes_ni) * seats_ni, (sdl_ni/tot_votes_ni) * seats_ni,
                (dup_ni/tot_votes_ni) * seats_ni, (sif_ni/tot_votes_ni) * seats_ni,
                (mnr_ni/tot_votes_ni) * seats_ni, (oth_ni/tot_votes_ni) * seats_ni,
                ],places=0)

sc = saferound([(con_sc/tot_votes_sc) * seats_sc, (lab_sc/tot_votes_sc) * seats_sc,
          (lib_sc/tot_votes_sc) * seats_sc, (nat_sc/tot_votes_sc) * seats_sc,
          (mnr_sc/tot_votes_sc) * seats_sc, (oth_sc/tot_votes_sc) * seats_sc],places=0)

ne = saferound([(con_ne/tot_votes_ne) * seats_ne, (lab_ne/tot_votes_ne) * seats_ne,
          (lib_ne/tot_votes_ne) * seats_ne, (nat_ne/tot_votes_ne) * seats_ne,
          (mnr_ne/tot_votes_ne) * seats_ne, (oth_ne/tot_votes_ne) * seats_ne],places=0)

nw = saferound([(con_nw/tot_votes_nw) * seats_nw, (lab_nw/tot_votes_nw) * seats_nw,
          (lib_nw/tot_votes_nw) * seats_nw, (nat_nw/tot_votes_nw) * seats_nw,
          (mnr_nw/tot_votes_nw) * seats_nw, (oth_nw/tot_votes_nw) * seats_nw],places=0)

yh = saferound([(con_yh/tot_votes_yh) * seats_yh, (lab_yh/tot_votes_yh) * seats_yh,
          (lib_yh/tot_votes_yh) * seats_yh, (nat_yh/tot_votes_yh) * seats_yh,
          (mnr_yh/tot_votes_yh) * seats_yh, (oth_yh/tot_votes_yh) * seats_yh],places=0)

cy = saferound([(con_cy/tot_votes_cy) * seats_cy, (lab_cy/tot_votes_cy) * seats_cy,
          (lib_cy/tot_votes_cy) * seats_cy, (nat_cy/tot_votes_cy) * seats_cy,
          (mnr_cy/tot_votes_cy) * seats_cy, (oth_cy/tot_votes_cy) * seats_cy],places=0)

wm = saferound([(con_wm/tot_votes_wm) * seats_wm, (lab_wm/tot_votes_wm) * seats_wm,
          (lib_wm/tot_votes_wm) * seats_wm, (nat_wm/tot_votes_wm) * seats_wm,
          (mnr_wm/tot_votes_wm) * seats_wm, (oth_wm/tot_votes_wm) * seats_wm],places=0)

em = saferound([(con_em/tot_votes_em) * seats_em, (lab_em/tot_votes_em) * seats_em,
          (lib_em/tot_votes_em) * seats_em, (nat_em/tot_votes_em) * seats_em,
          (mnr_em/tot_votes_em) * seats_em, (oth_em/tot_votes_em) * seats_em],places=0)

ea = saferound([(con_ea/tot_votes_ea) * seats_ea, (lab_ea/tot_votes_ea) * seats_ea,
          (lib_ea/tot_votes_ea) * seats_ea, (nat_ea/tot_votes_ea) * seats_ea,
          (mnr_ea/tot_votes_ea) * seats_ea, (oth_ea/tot_votes_ea) * seats_ea],places=0)

sw = saferound([(con_sw/tot_votes_sw) * seats_sw, (lab_sw/tot_votes_sw) * seats_sw,
          (lib_sw/tot_votes_sw) * seats_sw, (nat_sw/tot_votes_sw) * seats_sw,
          (mnr_sw/tot_votes_sw) * seats_sw, (oth_sw/tot_votes_sw) * seats_sw],places=0)

ld = saferound([(con_ld/tot_votes_ld) * seats_ld, (lab_ld/tot_votes_ld) * seats_ld,
          (lib_ld/tot_votes_ld) * seats_ld, (nat_ld/tot_votes_ld) * seats_ld,
          (mnr_ld/tot_votes_ld) * seats_ld, (oth_ld/tot_votes_ld) * seats_ld],places=0)

se = saferound([(con_se/tot_votes_se) * seats_se, (lab_se/tot_votes_se) * seats_se,
          (lib_se/tot_votes_se) * seats_se, (nat_se/tot_votes_se) * seats_se,
          (mnr_se/tot_votes_se) * seats_se, (oth_se/tot_votes_se) * seats_se],places=0)

'''
Each party
'''

con = int(sc[0]+ne[0]+nw[0]+yh[0]+cy[0]+wm[0]+em[0]+ea[0]+sw[0]+ld[0]+se[0])

lab = int(sc[1]+ne[1]+nw[1]+yh[1]+cy[1]+wm[1]+em[1]+ea[1]+sw[1]+ld[1]+se[1])

lib = int(sc[2]+ne[2]+nw[2]+yh[2]+cy[2]+wm[2]+em[2]+ea[2]+sw[2]+ld[2]+se[2])

nat = int(sc[3]+ne[3]+nw[3]+yh[3]+cy[3]+wm[3]+em[3]+ea[3]+sw[3]+ld[3]+se[3])

snp = int(sc[3])

pcy = int(cy[3])

oth = int(sc[4]+ne[4]+nw[4]+yh[4]+cy[4]+wm[4]+em[4]+ea[4]+sw[4]+ld[4]+se[4]+ni[4])

mnr = int(sc[5]+ne[5]+nw[5]+yh[5]+cy[5]+wm[5]+em[5]+ea[5]+sw[5]+ld[5]+se[5]+ni[5])

uup = int(ni[0])

sdl = int(ni[1])

sif = int(ni[2])

dup = int(ni[3])

#%%

'''
Display result
'''

print("Election result:\nConservative:",con,
                      "\nLabour:",lab,
                      "\nLiberal:",lib,
                      "\nSNP",snp,
                      "\nPlaid Cymru", pcy,
                      "\nUUP",uup,
                      "\nSDLP",sdl,
                      "\nSinn Féin",sif,
                      "\nDUP",dup,
                      "\nOthers",oth,
                      "\nMinority Parties",mnr,
        '\n\nTotal seats:', con+lab+lib+nat+oth+mnr+uup+sdl+sif+dup)

reg_seats = [seats_ni,seats_sc,seats_ne,seats_nw,seats_yh,seats_cy,
             seats_wm,seats_em,seats_ea,seats_sw,seats_ld,seats_se]

reg_raw = [sc,ne,nw,yh,cy,wm,em,ea,sw,ld,se]
reg = pd.DataFrame(
    reg_raw,columns=["Con","Lab","Lib","Nat","Min","Oth"],
    index=['SC','NE','NW','YH','CY','WM','EM','EA','SW','LD','SE'],dtype=int)



