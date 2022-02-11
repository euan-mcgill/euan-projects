#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:10:14 2022

@author: e.mcgill
"""

from iteround import saferound
import pandas as pd
import sys

def calc_elec(data,sixparty=False):
    if sixparty == True:
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
        tot_votes_se = con_se + lab_se + lib_se + nat_se + mnr_se + oth
