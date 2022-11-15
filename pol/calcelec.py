#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:10:14 2022

Brit Senate - Fourth iteration (2022-11-14)

@author: e.mcgill

This is the newest extant version - elecalculator.py is deprecated

Function map:
    <COMPLETE THIS>

"""

from iteround import saferound
import pandas as pd
import sys

class CalcElec:

    def __init__(self, infile, sixparty=False, elec_system="HW", seat_total=250):
        self.infile = infile
        self.data = pd.read_csv(infile,delimiter=';')
        self.sixparty = sixparty
        self.elec_system = elec_system
        self.seat_total = seat_total

    def regional_seats(self):
        elec_ni = self.data.loc[self.data['Area'] == 1, 'Electorate'].sum()
        elec_sc = self.data.loc[self.data['Area'] == 2, 'Electorate'].sum()
        elec_ne = self.data.loc[self.data['Area'] == 3, 'Electorate'].sum()
        elec_nw = self.data.loc[self.data['Area'] == 4, 'Electorate'].sum()
        elec_yh = self.data.loc[self.data['Area'] == 5, 'Electorate'].sum()
        elec_cy = self.data.loc[self.data['Area'] == 6, 'Electorate'].sum()
        elec_wm = self.data.loc[self.data['Area'] == 7, 'Electorate'].sum()
        elec_em = self.data.loc[self.data['Area'] == 8, 'Electorate'].sum()
        elec_ea = self.data.loc[self.data['Area'] == 9, 'Electorate'].sum()
        elec_sw = self.data.loc[self.data['Area'] == 10, 'Electorate'].sum()
        elec_ld = self.data.loc[self.data['Area'] == 11, 'Electorate'].sum()
        elec_se = self.data.loc[self.data['Area'] == 12, 'Electorate'].sum()
        elec_tot = int(elec_ni + elec_sc + elec_ne + elec_nw + elec_yh + elec_cy +
                           elec_wm + elec_em + elec_ea + elec_sw + elec_ld + elec_se)

        raw_seats = [float((elec_ni/elec_tot)*self.seat_total), float((elec_sc/elec_tot)*self.seat_total),
                          float((elec_ne/elec_tot)*self.seat_total), float((elec_nw/elec_tot)*self.seat_total),
                          float((elec_yh/elec_tot)*self.seat_total), float((elec_cy/elec_tot)*self.seat_total),
                          float((elec_wm/elec_tot)*self.seat_total), float((elec_em/elec_tot)*self.seat_total),
                          float((elec_ea/elec_tot)*self.seat_total), float((elec_sw/elec_tot)*self.seat_total),
                          float((elec_ld/elec_tot)*self.seat_total), float((elec_se/elec_tot)*self.seat_total)]

        # Seat numbers for each region
        rnd_seats = saferound(raw_seats, places=0)
        return rnd_seats

    def votes_per_party(self):
        if self.sixparty:
            # 1 = Northern Ireland
            uup_ni = self.data.loc[self.data['Area'] == 1, 'CON'].sum()
            sdl_ni = self.data.loc[self.data['Area'] == 1, 'LAB'].sum()
            dup_ni = self.data.loc[self.data['Area'] == 1, 'LIB'].sum()
            sif_ni = self.data.loc[self.data['Area'] == 1, 'NAT'].sum()
            mnr_ni = self.data.loc[self.data['Area'] == 1, 'MIN'].sum()
            oth_ni = self.data.loc[self.data['Area'] == 1, 'OTH'].sum()
            ni_votes = [uup_ni, sdl_ni, dup_ni, sif_ni, mnr_ni, oth_ni]
            # 2 = Scotland
            con_sc = self.data.loc[self.data['Area'] == 2, 'CON'].sum()
            lab_sc = self.data.loc[self.data['Area'] == 2, 'LAB'].sum()
            lib_sc = self.data.loc[self.data['Area'] == 2, 'LIB'].sum()
            nat_sc = self.data.loc[self.data['Area'] == 2, 'NAT'].sum()
            mnr_sc = self.data.loc[self.data['Area'] == 2, 'MIN'].sum()
            oth_sc = self.data.loc[self.data['Area'] == 2, 'OTH'].sum()
            sc_votes = [con_sc, lab_sc, lib_sc, nat_sc, mnr_sc, oth_sc]
            # 3 = North East
            con_ne = self.data.loc[self.data['Area'] == 3, 'CON'].sum()
            lab_ne = self.data.loc[self.data['Area'] == 3, 'LAB'].sum()
            lib_ne = self.data.loc[self.data['Area'] == 3, 'LIB'].sum()
            nat_ne = self.data.loc[self.data['Area'] == 3, 'NAT'].sum()
            mnr_ne = self.data.loc[self.data['Area'] == 3, 'MIN'].sum()
            oth_ne = self.data.loc[self.data['Area'] == 3, 'OTH'].sum()
            ne_votes = [con_ne, lab_ne, lib_ne, nat_ne, mnr_ne, oth_ne]
            # 4 = North West
            con_nw = self.data.loc[self.data['Area'] == 4, 'CON'].sum()
            lab_nw = self.data.loc[self.data['Area'] == 4, 'LAB'].sum()
            lib_nw = self.data.loc[self.data['Area'] == 4, 'LIB'].sum()
            nat_nw = self.data.loc[self.data['Area'] == 4, 'NAT'].sum()
            mnr_nw = self.data.loc[self.data['Area'] == 4, 'MIN'].sum()
            oth_nw = self.data.loc[self.data['Area'] == 4, 'OTH'].sum()
            nw_votes = [con_nw, lab_nw, lib_nw, nat_nw, mnr_nw, oth_nw]
            # 5 = Yorkshire and Humber
            con_yh = self.data.loc[self.data['Area'] == 5, 'CON'].sum()
            lab_yh = self.data.loc[self.data['Area'] == 5, 'LAB'].sum()
            lib_yh = self.data.loc[self.data['Area'] == 5, 'LIB'].sum()
            nat_yh = self.data.loc[self.data['Area'] == 5, 'NAT'].sum()
            mnr_yh = self.data.loc[self.data['Area'] == 5, 'MIN'].sum()
            oth_yh = self.data.loc[self.data['Area'] == 5, 'OTH'].sum()
            yh_votes = [con_yh, lab_yh, lib_yh, nat_yh, mnr_yh, oth_yh]
            # 6 = Cymru
            con_cy = self.data.loc[self.data['Area'] == 6, 'CON'].sum()
            lab_cy = self.data.loc[self.data['Area'] == 6, 'LAB'].sum()
            lib_cy = self.data.loc[self.data['Area'] == 6, 'LIB'].sum()
            nat_cy = self.data.loc[self.data['Area'] == 6, 'NAT'].sum()
            mnr_cy = self.data.loc[self.data['Area'] == 6, 'MIN'].sum()
            oth_cy = self.data.loc[self.data['Area'] == 6, 'OTH'].sum()
            cy_votes = [con_cy, lab_cy, lib_cy, nat_cy, mnr_cy, oth_cy]
            # 7 = West Midlands
            con_wm = self.data.loc[self.data['Area'] == 7, 'CON'].sum()
            lab_wm = self.data.loc[self.data['Area'] == 7, 'LAB'].sum()
            lib_wm = self.data.loc[self.data['Area'] == 7, 'LIB'].sum()
            nat_wm = self.data.loc[self.data['Area'] == 7, 'NAT'].sum()
            mnr_wm = self.data.loc[self.data['Area'] == 7, 'MIN'].sum()
            oth_wm = self.data.loc[self.data['Area'] == 7, 'OTH'].sum()
            wm_votes = [con_wm, lab_wm, lib_wm, nat_wm, mnr_wm, oth_wm]
            # 8 = East Midlands
            con_em = self.data.loc[self.data['Area'] == 8, 'CON'].sum()
            lab_em = self.data.loc[self.data['Area'] == 8, 'LAB'].sum()
            lib_em = self.data.loc[self.data['Area'] == 8, 'LIB'].sum()
            nat_em = self.data.loc[self.data['Area'] == 8, 'NAT'].sum()
            mnr_em = self.data.loc[self.data['Area'] == 8, 'MIN'].sum()
            oth_em = self.data.loc[self.data['Area'] == 8, 'OTH'].sum()
            em_votes = [con_em, lab_em, lib_em, nat_em, mnr_em, oth_em]
            # 9 = East Anglia
            con_ea = self.data.loc[self.data['Area'] == 9, 'CON'].sum()
            lab_ea = self.data.loc[self.data['Area'] == 9, 'LAB'].sum()
            lib_ea = self.data.loc[self.data['Area'] == 9, 'LIB'].sum()
            nat_ea = self.data.loc[self.data['Area'] == 9, 'NAT'].sum()
            mnr_ea = self.data.loc[self.data['Area'] == 9, 'MIN'].sum()
            oth_ea = self.data.loc[self.data['Area'] == 9, 'OTH'].sum()
            ea_votes = [con_ea, lab_ea, lib_ea, nat_ea, mnr_ea, oth_ea]
            # 10 = South West
            con_sw = self.data.loc[self.data['Area'] == 10, 'CON'].sum()
            lab_sw = self.data.loc[self.data['Area'] == 10, 'LAB'].sum()
            lib_sw = self.data.loc[self.data['Area'] == 10, 'LIB'].sum()
            nat_sw = self.data.loc[self.data['Area'] == 10, 'NAT'].sum()
            mnr_sw = self.data.loc[self.data['Area'] == 10, 'MIN'].sum()
            oth_sw = self.data.loc[self.data['Area'] == 10, 'OTH'].sum()
            sw_votes = [con_sw, lab_sw, lib_sw, nat_sw, mnr_sw, oth_sw]
            # 11 = London
            con_ld = self.data.loc[self.data['Area'] == 11, 'CON'].sum()
            lab_ld = self.data.loc[self.data['Area'] == 11, 'LAB'].sum()
            lib_ld = self.data.loc[self.data['Area'] == 11, 'LIB'].sum()
            nat_ld = self.data.loc[self.data['Area'] == 11, 'NAT'].sum()
            mnr_ld = self.data.loc[self.data['Area'] == 11, 'MIN'].sum()
            oth_ld = self.data.loc[self.data['Area'] == 11, 'OTH'].sum()
            ld_votes = [con_ld, lab_ld, lib_ld, nat_ld, mnr_ld, oth_ld]
            # 12 = South East
            con_se = self.data.loc[self.data['Area'] == 12, 'CON'].sum()
            lab_se = self.data.loc[self.data['Area'] == 12, 'LAB'].sum()
            lib_se = self.data.loc[self.data['Area'] == 12, 'LIB'].sum()
            nat_se = self.data.loc[self.data['Area'] == 12, 'NAT'].sum()
            mnr_se = self.data.loc[self.data['Area'] == 12, 'MIN'].sum()
            oth_se = self.data.loc[self.data['Area'] == 12, 'OTH'].sum()
            se_votes = [con_se, lab_se, lib_se, nat_se, mnr_se, oth_se]

            party_matrix = [ni_votes, sc_votes, ne_votes, nw_votes, yh_votes,
                            cy_votes, wm_votes, em_votes, ea_votes, sw_votes,
                            ld_votes, se_votes]
            return party_matrix

        elif self.sixparty == False:
            # 1 = Northern Ireland
            uup_ni = self.data.loc[self.data['Area'] == 1, 'CON'].sum() # NI not yet done
            sdl_ni = self.data.loc[self.data['Area'] == 1, 'LAB'].sum()
            dup_ni = self.data.loc[self.data['Area'] == 1, 'LIB'].sum()
            sif_ni = self.data.loc[self.data['Area'] == 1, 'NAT'].sum()
            mnr_ni = self.data.loc[self.data['Area'] == 1, 'MIN'].sum()
            oth_ni = self.data.loc[self.data['Area'] == 1, 'OTH'].sum()
            ni_votes = [uup_ni, sdl_ni, dup_ni, sif_ni, mnr_ni, oth_ni]
            # 2 = Scotland
            con_sc = self.data.loc[self.data['Area'] == 2, 'CON'].sum()
            lab_sc = self.data.loc[self.data['Area'] == 2, 'LAB'].sum()
            lib_sc = self.data.loc[self.data['Area'] == 2, 'LIB'].sum()
            brx_sc = self.data.loc[self.data['Area'] == 2, 'UKIP'].sum()
            grn_sc = self.data.loc[self.data['Area'] == 2, 'Green'].sum()
            nat_sc = self.data.loc[self.data['Area'] == 2, 'NAT'].sum()
            mnr_sc = self.data.loc[self.data['Area'] == 2, 'MIN'].sum()
            oth_sc = self.data.loc[self.data['Area'] == 2, 'OTH'].sum()
            sc_votes = [con_sc, lab_sc, lib_sc, brx_sc, grn_sc, nat_sc, mnr_sc, oth_sc] # eight party progress so far
            # 3 = North East
            con_ne = self.data.loc[self.data['Area'] == 3, 'CON'].sum()
            lab_ne = self.data.loc[self.data['Area'] == 3, 'LAB'].sum()
            lib_ne = self.data.loc[self.data['Area'] == 3, 'LIB'].sum()
            nat_ne = self.data.loc[self.data['Area'] == 3, 'NAT'].sum()
            mnr_ne = self.data.loc[self.data['Area'] == 3, 'MIN'].sum()
            oth_ne = self.data.loc[self.data['Area'] == 3, 'OTH'].sum()
            ne_votes = [con_ne, lab_ne, lib_ne, nat_ne, mnr_ne, oth_ne]
            # 4 = North West
            con_nw = self.data.loc[self.data['Area'] == 4, 'CON'].sum()
            lab_nw = self.data.loc[self.data['Area'] == 4, 'LAB'].sum()
            lib_nw = self.data.loc[self.data['Area'] == 4, 'LIB'].sum()
            nat_nw = self.data.loc[self.data['Area'] == 4, 'NAT'].sum()
            mnr_nw = self.data.loc[self.data['Area'] == 4, 'MIN'].sum()
            oth_nw = self.data.loc[self.data['Area'] == 4, 'OTH'].sum()
            nw_votes = [con_nw, lab_nw, lib_nw, nat_nw, mnr_nw, oth_nw]
            # 5 = Yorkshire and Humber
            con_yh = self.data.loc[self.data['Area'] == 5, 'CON'].sum()
            lab_yh = self.data.loc[self.data['Area'] == 5, 'LAB'].sum()
            lib_yh = self.data.loc[self.data['Area'] == 5, 'LIB'].sum()
            nat_yh = self.data.loc[self.data['Area'] == 5, 'NAT'].sum()
            mnr_yh = self.data.loc[self.data['Area'] == 5, 'MIN'].sum()
            oth_yh = self.data.loc[self.data['Area'] == 5, 'OTH'].sum()
            yh_votes = [con_yh, lab_yh, lib_yh, nat_yh, mnr_yh, oth_yh]
            # 6 = Cymru
            con_cy = self.data.loc[self.data['Area'] == 6, 'CON'].sum()
            lab_cy = self.data.loc[self.data['Area'] == 6, 'LAB'].sum()
            lib_cy = self.data.loc[self.data['Area'] == 6, 'LIB'].sum()
            nat_cy = self.data.loc[self.data['Area'] == 6, 'NAT'].sum()
            mnr_cy = self.data.loc[self.data['Area'] == 6, 'MIN'].sum()
            oth_cy = self.data.loc[self.data['Area'] == 6, 'OTH'].sum()
            cy_votes = [con_cy, lab_cy, lib_cy, nat_cy, mnr_cy, oth_cy]
            # 7 = West Midlands
            con_wm = self.data.loc[self.data['Area'] == 7, 'CON'].sum()
            lab_wm = self.data.loc[self.data['Area'] == 7, 'LAB'].sum()
            lib_wm = self.data.loc[self.data['Area'] == 7, 'LIB'].sum()
            nat_wm = self.data.loc[self.data['Area'] == 7, 'NAT'].sum()
            mnr_wm = self.data.loc[self.data['Area'] == 7, 'MIN'].sum()
            oth_wm = self.data.loc[self.data['Area'] == 7, 'OTH'].sum()
            wm_votes = [con_wm, lab_wm, lib_wm, nat_wm, mnr_wm, oth_wm]
            # 8 = East Midlands
            con_em = self.data.loc[self.data['Area'] == 8, 'CON'].sum()
            lab_em = self.data.loc[self.data['Area'] == 8, 'LAB'].sum()
            lib_em = self.data.loc[self.data['Area'] == 8, 'LIB'].sum()
            nat_em = self.data.loc[self.data['Area'] == 8, 'NAT'].sum()
            mnr_em = self.data.loc[self.data['Area'] == 8, 'MIN'].sum()
            oth_em = self.data.loc[self.data['Area'] == 8, 'OTH'].sum()
            em_votes = [con_em, lab_em, lib_em, nat_em, mnr_em, oth_em]
            # 9 = East Anglia
            con_ea = self.data.loc[self.data['Area'] == 9, 'CON'].sum()
            lab_ea = self.data.loc[self.data['Area'] == 9, 'LAB'].sum()
            lib_ea = self.data.loc[self.data['Area'] == 9, 'LIB'].sum()
            nat_ea = self.data.loc[self.data['Area'] == 9, 'NAT'].sum()
            mnr_ea = self.data.loc[self.data['Area'] == 9, 'MIN'].sum()
            oth_ea = self.data.loc[self.data['Area'] == 9, 'OTH'].sum()
            ea_votes = [con_ea, lab_ea, lib_ea, nat_ea, mnr_ea, oth_ea]
            # 10 = South West
            con_sw = self.data.loc[self.data['Area'] == 10, 'CON'].sum()
            lab_sw = self.data.loc[self.data['Area'] == 10, 'LAB'].sum()
            lib_sw = self.data.loc[self.data['Area'] == 10, 'LIB'].sum()
            nat_sw = self.data.loc[self.data['Area'] == 10, 'NAT'].sum()
            mnr_sw = self.data.loc[self.data['Area'] == 10, 'MIN'].sum()
            oth_sw = self.data.loc[self.data['Area'] == 10, 'OTH'].sum()
            sw_votes = [con_sw, lab_sw, lib_sw, nat_sw, mnr_sw, oth_sw]
            # 11 = London
            con_ld = self.data.loc[self.data['Area'] == 11, 'CON'].sum()
            lab_ld = self.data.loc[self.data['Area'] == 11, 'LAB'].sum()
            lib_ld = self.data.loc[self.data['Area'] == 11, 'LIB'].sum()
            nat_ld = self.data.loc[self.data['Area'] == 11, 'NAT'].sum()
            mnr_ld = self.data.loc[self.data['Area'] == 11, 'MIN'].sum()
            oth_ld = self.data.loc[self.data['Area'] == 11, 'OTH'].sum()
            ld_votes = [con_ld, lab_ld, lib_ld, nat_ld, mnr_ld, oth_ld]
            # 12 = South East
            con_se = self.data.loc[self.data['Area'] == 12, 'CON'].sum()
            lab_se = self.data.loc[self.data['Area'] == 12, 'LAB'].sum()
            lib_se = self.data.loc[self.data['Area'] == 12, 'LIB'].sum()
            nat_se = self.data.loc[self.data['Area'] == 12, 'NAT'].sum()
            mnr_se = self.data.loc[self.data['Area'] == 12, 'MIN'].sum()
            oth_se = self.data.loc[self.data['Area'] == 12, 'OTH'].sum()
            se_votes = [con_se, lab_se, lib_se, nat_se, mnr_se, oth_se]

            party_matrix = [ni_votes, sc_votes, ne_votes, nw_votes, yh_votes,
                            cy_votes, wm_votes, em_votes, ea_votes, sw_votes,
                            ld_votes, se_votes]
            return party_matrix
        
        else:
            print("Please specify whether analysis is 6 party or 8 party: \n (6 party = pre-2010)")
            sys.exit()

    def electorate(self):
        total_votes = self.votes_per_party()
        electorate_array = [sum(total_votes[0]), sum(total_votes[1]), sum(total_votes[2]),
                            sum(total_votes[3]), sum(total_votes[4]), sum(total_votes[5]),
                            sum(total_votes[6]), sum(total_votes[7]), sum(total_votes[8]),
                            sum(total_votes[9]), sum(total_votes[10]), sum(total_votes[11])]
        return electorate_array

    def hamilton(self):
        rnd_seats = self.regional_seats()
        party_totals = self.votes_per_party()
        vote_totals = self.electorate()
        if sum(rnd_seats)  == self.seat_total:
            print("Seat total valid \n\n\n")
        else:
            print("Seat total does not equal seat_total")

        if self.sixparty:
            ni = saferound([(party_totals[0][0]/vote_totals[0]) * rnd_seats[0], (party_totals[0][1]/vote_totals[0]) * rnd_seats[0],
                            (party_totals[0][2]/vote_totals[0]) * rnd_seats[0], (party_totals[0][3]/vote_totals[0]) * rnd_seats[0],
                            (party_totals[0][4]/vote_totals[0]) * rnd_seats[0], (party_totals[0][5]/vote_totals[0]) * rnd_seats[0],
                            ],places=0)
            sc = saferound([(party_totals[1][0]/vote_totals[1]) * rnd_seats[1], (party_totals[1][1]/vote_totals[1]) * rnd_seats[1],
                            (party_totals[1][2]/vote_totals[1]) * rnd_seats[1], (party_totals[1][3]/vote_totals[1]) * rnd_seats[1],
                            (party_totals[1][4]/vote_totals[1]) * rnd_seats[1], (party_totals[1][5]/vote_totals[1]) * rnd_seats[1],
                            ],places=0)
            ne = saferound([(party_totals[2][0]/vote_totals[2]) * rnd_seats[2], (party_totals[2][1]/vote_totals[2]) * rnd_seats[2],
                            (party_totals[2][2]/vote_totals[2]) * rnd_seats[2], (party_totals[2][3]/vote_totals[2]) * rnd_seats[2],
                            (party_totals[2][4]/vote_totals[2]) * rnd_seats[2], (party_totals[2][5]/vote_totals[2]) * rnd_seats[2],
                            ],places=0)
            nw = saferound([(party_totals[3][0]/vote_totals[3]) * rnd_seats[3], (party_totals[3][1]/vote_totals[3]) * rnd_seats[3],
                            (party_totals[3][2]/vote_totals[3]) * rnd_seats[3], (party_totals[3][3]/vote_totals[3]) * rnd_seats[3],
                            (party_totals[3][4]/vote_totals[3]) * rnd_seats[3], (party_totals[3][5]/vote_totals[3]) * rnd_seats[3],
                            ],places=0)
            yh = saferound([(party_totals[4][0]/vote_totals[4]) * rnd_seats[4], (party_totals[4][1]/vote_totals[4]) * rnd_seats[4],
                            (party_totals[4][2]/vote_totals[4]) * rnd_seats[4], (party_totals[4][3]/vote_totals[4]) * rnd_seats[4],
                            (party_totals[4][4]/vote_totals[4]) * rnd_seats[4], (party_totals[4][5]/vote_totals[4]) * rnd_seats[4],
                            ],places=0)
            cy = saferound([(party_totals[5][0]/vote_totals[5]) * rnd_seats[5], (party_totals[5][1]/vote_totals[5]) * rnd_seats[5],
                            (party_totals[5][2]/vote_totals[5]) * rnd_seats[5], (party_totals[5][3]/vote_totals[5]) * rnd_seats[5],
                            (party_totals[5][4]/vote_totals[5]) * rnd_seats[5], (party_totals[5][5]/vote_totals[5]) * rnd_seats[5],
                            ],places=0)
            wm = saferound([(party_totals[6][0]/vote_totals[6]) * rnd_seats[6], (party_totals[6][1]/vote_totals[6]) * rnd_seats[6],
                            (party_totals[6][2]/vote_totals[6]) * rnd_seats[6], (party_totals[6][3]/vote_totals[6]) * rnd_seats[6],
                            (party_totals[6][4]/vote_totals[6]) * rnd_seats[6], (party_totals[6][5]/vote_totals[6]) * rnd_seats[6],
                            ],places=0)
            em = saferound([(party_totals[7][0]/vote_totals[7]) * rnd_seats[7], (party_totals[7][1]/vote_totals[7]) * rnd_seats[7],
                            (party_totals[7][2]/vote_totals[7]) * rnd_seats[7], (party_totals[7][3]/vote_totals[7]) * rnd_seats[7],
                            (party_totals[7][4]/vote_totals[7]) * rnd_seats[7], (party_totals[7][5]/vote_totals[7]) * rnd_seats[7],
                            ],places=0)
            ea = saferound([(party_totals[8][0]/vote_totals[8]) * rnd_seats[8], (party_totals[8][1]/vote_totals[8]) * rnd_seats[8],
                            (party_totals[8][2]/vote_totals[8]) * rnd_seats[8], (party_totals[8][3]/vote_totals[8]) * rnd_seats[8],
                            (party_totals[8][4]/vote_totals[8]) * rnd_seats[8], (party_totals[8][5]/vote_totals[8]) * rnd_seats[8],
                            ],places=0)
            sw = saferound([(party_totals[9][0]/vote_totals[9]) * rnd_seats[9], (party_totals[9][1]/vote_totals[9]) * rnd_seats[9],
                            (party_totals[9][2]/vote_totals[9]) * rnd_seats[9], (party_totals[9][3]/vote_totals[9]) * rnd_seats[9],
                            (party_totals[9][4]/vote_totals[9]) * rnd_seats[9], (party_totals[9][5]/vote_totals[9]) * rnd_seats[9],
                            ],places=0)
            ld = saferound([(party_totals[10][0]/vote_totals[10]) * rnd_seats[10], (party_totals[10][1]/vote_totals[10]) * rnd_seats[10],
                            (party_totals[10][2]/vote_totals[10]) * rnd_seats[10], (party_totals[10][3]/vote_totals[10]) * rnd_seats[10],
                            (party_totals[10][4]/vote_totals[10]) * rnd_seats[10], (party_totals[10][5]/vote_totals[10]) * rnd_seats[10],
                            ],places=0)
            se = saferound([(party_totals[11][0]/vote_totals[11]) * rnd_seats[11], (party_totals[11][1]/vote_totals[11]) * rnd_seats[11],
                            (party_totals[11][2]/vote_totals[11]) * rnd_seats[11], (party_totals[11][3]/vote_totals[11]) * rnd_seats[11],
                            (party_totals[11][4]/vote_totals[11]) * rnd_seats[11], (party_totals[11][5]/vote_totals[11]) * rnd_seats[11],
                            ],places=0)

            con = int(sc[0]+ne[0]+nw[0]+yh[0]+cy[0]+wm[0]+em[0]+ea[0]+sw[0]+ld[0]+se[0])
            lab = int(sc[1]+ne[1]+nw[1]+yh[1]+cy[1]+wm[1]+em[1]+ea[1]+sw[1]+ld[1]+se[1])
            lib = int(sc[2]+ne[2]+nw[2]+yh[2]+cy[2]+wm[2]+em[2]+ea[2]+sw[2]+ld[2]+se[2])
            nat = int(sc[3]+ne[3]+nw[3]+yh[3]+cy[3]+wm[3]+em[3]+ea[3]+sw[3]+ld[3]+se[3])
            snp = int(sc[3])
            pcy = int(cy[3])
            oth = int(sc[5]+ne[5]+nw[5]+yh[5]+cy[5]+wm[5]+em[5]+ea[5]+sw[5]+ld[5]+se[5]+ni[5])
            mnr = int(sc[4]+ne[4]+nw[4]+yh[4]+cy[4]+wm[4]+em[4]+ea[4]+sw[4]+ld[4]+se[4]+ni[4])
            uup = int(ni[0])
            sdl = int(ni[1])
            sif = int(ni[2])
            dup = int(ni[3])

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
            reg_raw = [sc,ne,nw,yh,cy,wm,em,ea,sw,ld,se,ni]
            reg = pd.DataFrame(
            reg_raw,columns=["Con","Lab","Lib","Nat","Min","Oth"],
                    index=['SC','NE','NW','YH','CY','WM','EM','EA','SW','LD','SE','NI'],dtype=int)

            return reg

        elif self.sixparty == False:
            pass
        
        else:
            print("Please specify whether analysis is 6 party or 8 party: \n (6 party = pre-2010)")


    def dhondt(self, nSeats, votes, verbose=False):
        """
        Author: https://gist.github.com/brunosan
        nSeats is the number of seats
        votes is a dictionary with the key:value {'party':votes}
        verbose is an option to print designation info
        """
        t_votes=votes.copy()
        seats={}
        for key in votes: seats[key]=0
        while sum(seats.values()) < nSeats:
            max_v= max(t_votes.values())
            next_seat=list(t_votes.keys())[list(t_votes.values()).index(max_v)]
            if next_seat in seats:
                seats[next_seat]+=1
            else:
                seats[next_seat]=1

            if verbose:
                print("Round {}: {}".format(sum(seats.values()),next_seat))
                for key in t_votes:
                    print("\t{} [{}]: {:.1f}".format(key,seats[key],t_votes[key]))
                print("\b")
            t_votes[next_seat]=votes[next_seat]/(seats[next_seat]+1)
        return seats

    def dhondt_calc(self):
        vpp = self.votes_per_party()
        seats = self.regional_seats()
        result = []

        if self.sixparty:
            ni_dh = {'UUP': vpp[0][0], 'SDLP':vpp[0][1], 'DUP': vpp[0][2], 'SF':  vpp[0][3], 'Min': vpp[0][4], 'Oth': vpp[0][5]}
            sc_dh = {'Con': vpp[1][0], 'Lab': vpp[1][1], 'Lib': vpp[1][2], 'SNP': vpp[1][3], 'Min': vpp[1][4], 'Oth': vpp[1][5]}
            ne_dh = {'Con': vpp[2][0], 'Lab': vpp[2][1], 'Lib': vpp[2][2], 'Nat': vpp[2][3], 'Min': vpp[2][4], 'Oth': vpp[2][5]}
            nw_dh = {'Con': vpp[3][0], 'Lab': vpp[3][1], 'Lib': vpp[3][2], 'Nat': vpp[3][3], 'Min': vpp[3][4], 'Oth': vpp[3][5]}
            yh_dh = {'Con': vpp[4][0], 'Lab': vpp[4][1], 'Lib': vpp[4][2], 'Nat': vpp[4][3], 'Min': vpp[4][4], 'Oth': vpp[4][5]}
            cy_dh = {'Con': vpp[5][0], 'Lab': vpp[5][1], 'Lib': vpp[5][2], 'PC':  vpp[5][3], 'Min': vpp[5][4], 'Oth': vpp[5][5]}
            wm_dh = {'Con': vpp[6][0], 'Lab': vpp[6][1], 'Lib': vpp[6][2], 'Nat': vpp[6][3], 'Min': vpp[6][4], 'Oth': vpp[6][5]}
            em_dh = {'Con': vpp[7][0], 'Lab': vpp[7][1], 'Lib': vpp[7][2], 'Nat': vpp[7][3], 'Min': vpp[7][4], 'Oth': vpp[7][5]}
            ea_dh = {'Con': vpp[8][0], 'Lab': vpp[8][1], 'Lib': vpp[8][2], 'Nat': vpp[8][3], 'Min': vpp[8][4], 'Oth': vpp[8][5]}
            sw_dh = {'Con': vpp[9][0], 'Lab': vpp[9][1], 'Lib': vpp[9][2], 'Nat': vpp[9][3], 'Min': vpp[9][4], 'Oth': vpp[9][5]}
            ld_dh = {'Con': vpp[10][0], 'Lab': vpp[10][1], 'Lib': vpp[10][2], 'Nat': vpp[10][3], 'Min': vpp[10][4], 'Oth': vpp[10][5]}
            se_dh = {'Con': vpp[11][0], 'Lab': vpp[11][1], 'Lib': vpp[11][2], 'Nat': vpp[11][3], 'Min': vpp[11][4], 'Oth': vpp[11][5]}

            dh_list = [ni_dh, sc_dh, ne_dh, nw_dh, yh_dh, cy_dh, wm_dh, em_dh, ea_dh, sw_dh, ld_dh, se_dh]

            for i in range(0, len(dh_list)):
                result.append(self.dhondt(seats[i], dh_list[i]))

            con = int(result[1]['Con']+result[2]['Con']+result[3]['Con']+result[4]['Con']+result[5]['Con']+result[6]['Con']+result[7]['Con']+result[8]['Con']+result[9]['Con']+result[10]['Con']+result[11]['Con'])
            lab = int(result[1]['Lab']+result[2]['Lab']+result[3]['Lab']+result[4]['Lab']+result[5]['Lab']+result[6]['Lab']+result[7]['Lab']+result[8]['Lab']+result[9]['Lab']+result[10]['Lab']+result[11]['Lab'])
            lib = int(result[1]['Lib']+result[2]['Lib']+result[3]['Lib']+result[4]['Lib']+result[5]['Lib']+result[6]['Lib']+result[7]['Lib']+result[8]['Lib']+result[9]['Lib']+result[10]['Lib']+result[11]['Lib'])
            nat = int(result[1]['SNP']+result[2]['Nat']+result[3]['Nat']+result[4]['Nat']+result[5]['PC']+result[6]['Nat']+result[7]['Nat']+result[8]['Nat']+result[9]['Nat']+result[10]['Nat']+result[11]['Nat'])
            mnr = int(result[0]['Min']+result[1]['Min']+result[2]['Min']+result[3]['Min']+result[4]['Min']+result[5]['Min']+result[6]['Min']+result[7]['Min']+result[8]['Min']+result[9]['Min']+result[10]['Min']+result[11]['Min'])
            oth = int(result[0]['Oth']+result[1]['Oth']+result[2]['Oth']+result[3]['Oth']+result[4]['Oth']+result[5]['Oth']+result[6]['Oth']+result[7]['Oth']+result[8]['Oth']+result[9]['Oth']+result[10]['Oth']+result[11]['Oth'])
            snp = int(result[1]['SNP'])
            pcy = int(result[5]['PC'])
            uup = int(result[0]['UUP'])
            sdl = int(result[0]['SDLP'])
            sif = int(result[0]['SF'])
            dup = int(result[0]['DUP'])

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

            return result
        
        elif self.sixparty == False:
            pass
        
        else:
            print("Please specify whether analysis is 6 party or 8 party: \n (6 party = pre-2010)")





    def mms(self):
        pass
        # to complete at a later date

    # def reg_party(self): # rejigging whole file by breaking up this function (in progress...)



        '''
    ###############################################################################
        
        if self.sixparty == False:
        # I changed "Brexit" to "UKIP" in the 2019.csv file
            # 1 = Northern Ireland
            uup_ni = data.loc[data['Area'] == 1, 'CON'].sum()
            sdl_ni = data.loc[data['Area'] == 1, 'LAB'].sum()
            dup_ni = data.loc[data['Area'] == 1, 'LIB'].sum()
            all_ni = data.loc[data['Area'] == 1, 'UKIP'].sum()
            grn_ni = data.loc[data['Area'] == 1, 'Green'].sum()
            sif_ni = data.loc[data['Area'] == 1, 'NAT'].sum()
            mnr_ni = data.loc[data['Area'] == 1, 'MIN'].sum()
            oth_ni = data.loc[data['Area'] == 1, 'OTH'].sum()
            tot_votes_ni = uup_ni + sdl_ni + dup_ni + all_ni + grn_ni + sif_ni + mnr_ni + oth_ni
            elec_ni = data.loc[data['Area'] == 1, 'Electorate'].sum()
            
            # 2 = Scotland
            con_sc = data.loc[data['Area'] == 2, 'CON'].sum()
            lab_sc = data.loc[data['Area'] == 2, 'LAB'].sum()
            lib_sc = data.loc[data['Area'] == 2, 'LIB'].sum()
            brx_sc = data.loc[data['Area'] == 2, 'UKIP'].sum()
            grn_sc = data.loc[data['Area'] == 2, 'Green'].sum()
            nat_sc = data.loc[data['Area'] == 2, 'NAT'].sum()
            mnr_sc = data.loc[data['Area'] == 2, 'MIN'].sum()
            oth_sc = data.loc[data['Area'] == 2, 'OTH'].sum()
            tot_votes_sc = con_sc + lab_sc + lib_sc + brx_sc + grn_sc + nat_sc + mnr_sc + oth_sc
            elec_sc = data.loc[data['Area'] == 2, 'Electorate'].sum()
            
            # 3 = North East
            con_ne = data.loc[data['Area'] == 3, 'CON'].sum()
            lab_ne = data.loc[data['Area'] == 3, 'LAB'].sum()
            lib_ne = data.loc[data['Area'] == 3, 'LIB'].sum()
            brx_ne = data.loc[data['Area'] == 3, 'UKIP'].sum()
            grn_ne = data.loc[data['Area'] == 3, 'Green'].sum()
            nat_ne = data.loc[data['Area'] == 3, 'NAT'].sum()
            mnr_ne = data.loc[data['Area'] == 3, 'MIN'].sum()
            oth_ne = data.loc[data['Area'] == 3, 'OTH'].sum()
            tot_votes_ne = con_ne + lab_ne + lib_ne + brx_ne + grn_ne + nat_ne + mnr_ne + oth_ne
            elec_ne = data.loc[data['Area'] == 3, 'Electorate'].sum()
            
            # 4 = North West
            con_nw = data.loc[data['Area'] == 4, 'CON'].sum()
            lab_nw = data.loc[data['Area'] == 4, 'LAB'].sum()
            lib_nw = data.loc[data['Area'] == 4, 'LIB'].sum()
            brx_nw = data.loc[data['Area'] == 4, 'UKIP'].sum()
            grn_nw = data.loc[data['Area'] == 4, 'Green'].sum()
            nat_nw = data.loc[data['Area'] == 4, 'NAT'].sum()
            mnr_nw = data.loc[data['Area'] == 4, 'MIN'].sum()
            oth_nw = data.loc[data['Area'] == 4, 'OTH'].sum()
            tot_votes_nw = con_nw + lab_nw + lib_nw + brx_nw + grn_nw + nat_nw + mnr_nw + oth_nw
            elec_nw = data.loc[data['Area'] == 4, 'Electorate'].sum()
            
            # 5 = Yorkshire and Humber
            con_yh = data.loc[data['Area'] == 5, 'CON'].sum()
            lab_yh = data.loc[data['Area'] == 5, 'LAB'].sum()
            lib_yh = data.loc[data['Area'] == 5, 'LIB'].sum()
            brx_yh = data.loc[data['Area'] == 5, 'UKIP'].sum()
            grn_yh = data.loc[data['Area'] == 5, 'Green'].sum()
            nat_yh = data.loc[data['Area'] == 5, 'NAT'].sum()
            mnr_yh = data.loc[data['Area'] == 5, 'MIN'].sum()
            oth_yh = data.loc[data['Area'] == 5, 'OTH'].sum()
            tot_votes_yh = con_yh + lab_yh + lib_yh + brx_yh + grn_yh + nat_yh + mnr_yh + oth_yh
            elec_yh = data.loc[data['Area'] == 5, 'Electorate'].sum()
            
            # 6 = Cymru
            con_cy = data.loc[data['Area'] == 6, 'CON'].sum()
            lab_cy = data.loc[data['Area'] == 6, 'LAB'].sum()
            lib_cy = data.loc[data['Area'] == 6, 'LIB'].sum()
            brx_cy = data.loc[data['Area'] == 6, 'UKIP'].sum()
            grn_cy = data.loc[data['Area'] == 6, 'Green'].sum()
            nat_cy = data.loc[data['Area'] == 6, 'NAT'].sum()
            mnr_cy = data.loc[data['Area'] == 6, 'MIN'].sum()
            oth_cy = data.loc[data['Area'] == 6, 'OTH'].sum()
            tot_votes_cy = con_cy + lab_cy + lib_cy + brx_cy + grn_cy + nat_cy + mnr_cy + oth_cy
            elec_cy = data.loc[data['Area'] == 6, 'Electorate'].sum()
            
            # 7 = West Midlands
            con_wm = data.loc[data['Area'] == 7, 'CON'].sum()
            lab_wm = data.loc[data['Area'] == 7, 'LAB'].sum()
            lib_wm = data.loc[data['Area'] == 7, 'LIB'].sum()
            brx_wm = data.loc[data['Area'] == 7, 'UKIP'].sum()
            grn_wm = data.loc[data['Area'] == 7, 'Green'].sum()
            nat_wm = data.loc[data['Area'] == 7, 'NAT'].sum()
            mnr_wm = data.loc[data['Area'] == 7, 'MIN'].sum()
            oth_wm = data.loc[data['Area'] == 7, 'OTH'].sum()
            tot_votes_wm = con_wm + lab_wm + lib_wm + brx_wm + grn_wm + nat_wm + mnr_wm + oth_wm
            elec_wm = data.loc[data['Area'] == 7, 'Electorate'].sum()
            
            # 8 = East Midlands
            con_em = data.loc[data['Area'] == 8, 'CON'].sum()
            lab_em = data.loc[data['Area'] == 8, 'LAB'].sum()
            lib_em = data.loc[data['Area'] == 8, 'LIB'].sum()
            brx_em = data.loc[data['Area'] == 8, 'UKIP'].sum()
            grn_em = data.loc[data['Area'] == 8, 'Green'].sum()
            nat_em = data.loc[data['Area'] == 8, 'NAT'].sum()
            mnr_em = data.loc[data['Area'] == 8, 'MIN'].sum()
            oth_em = data.loc[data['Area'] == 8, 'OTH'].sum()
            tot_votes_em = con_em + lab_em + lib_em + brx_em + grn_em + nat_em + mnr_em + oth_em
            elec_em = data.loc[data['Area'] == 8, 'Electorate'].sum()
            
            # 9 = East Anglia
            con_ea = data.loc[data['Area'] == 9, 'CON'].sum()
            lab_ea = data.loc[data['Area'] == 9, 'LAB'].sum()
            lib_ea = data.loc[data['Area'] == 9, 'LIB'].sum()
            brx_ea = data.loc[data['Area'] == 9, 'UKIP'].sum()
            grn_ea = data.loc[data['Area'] == 9, 'Green'].sum()
            nat_ea = data.loc[data['Area'] == 9, 'NAT'].sum()
            mnr_ea = data.loc[data['Area'] == 9, 'MIN'].sum()
            oth_ea = data.loc[data['Area'] == 9, 'OTH'].sum()
            tot_votes_ea = con_ea + lab_ea + lib_ea + brx_ea + grn_ea + nat_ea + mnr_ea + oth_ea
            elec_ea = data.loc[data['Area'] == 9, 'Electorate'].sum()
            
            # 10 = South West
            con_sw = data.loc[data['Area'] == 10, 'CON'].sum()
            lab_sw = data.loc[data['Area'] == 10, 'LAB'].sum()
            lib_sw = data.loc[data['Area'] == 10, 'LIB'].sum()
            brx_sw = data.loc[data['Area'] == 10, 'UKIP'].sum()
            grn_sw = data.loc[data['Area'] == 10, 'Green'].sum()
            nat_sw = data.loc[data['Area'] == 10, 'NAT'].sum()
            mnr_sw = data.loc[data['Area'] == 10, 'MIN'].sum()
            oth_sw = data.loc[data['Area'] == 10, 'OTH'].sum()
            tot_votes_sw = con_sw + lab_sw + lib_sw + brx_sw + grn_sw + nat_sw + mnr_sw + oth_sw
            elec_sw = data.loc[data['Area'] == 10, 'Electorate'].sum()
            
            # 11 = London
            con_ld = data.loc[data['Area'] == 11, 'CON'].sum()
            lab_ld = data.loc[data['Area'] == 11, 'LAB'].sum()
            lib_ld = data.loc[data['Area'] == 11, 'LIB'].sum()
            brx_ld = data.loc[data['Area'] == 11, 'UKIP'].sum()
            grn_ld = data.loc[data['Area'] == 11, 'Green'].sum()
            nat_ld = data.loc[data['Area'] == 11, 'NAT'].sum()
            mnr_ld = data.loc[data['Area'] == 11, 'MIN'].sum()
            oth_ld = data.loc[data['Area'] == 11, 'OTH'].sum()
            tot_votes_ld = con_ld + lab_ld + lib_ld + brx_ld + grn_ld + nat_ld + mnr_ld + oth_ld
            elec_ld = data.loc[data['Area'] == 11, 'Electorate'].sum()
            
            # 12 = South East
            con_se = data.loc[data['Area'] == 12, 'CON'].sum()
            lab_se = data.loc[data['Area'] == 12, 'LAB'].sum()
            lib_se = data.loc[data['Area'] == 12, 'LIB'].sum()
            brx_se = data.loc[data['Area'] == 12, 'UKIP'].sum()
            grn_se = data.loc[data['Area'] == 12, 'Green'].sum()
            nat_se = data.loc[data['Area'] == 12, 'NAT'].sum()
            mnr_se = data.loc[data['Area'] == 12, 'MIN'].sum()
            oth_se = data.loc[data['Area'] == 12, 'OTH'].sum()
            tot_votes_se = con_se + lab_se + lib_se + brx_se + grn_se + nat_se + mnr_se + oth_se
            elec_se = data.loc[data['Area'] == 12, 'Electorate'].sum()
            
            elec_tot = int(elec_ni + elec_sc + elec_ne + elec_nw + elec_yh + elec_cy + 
                           elec_wm + elec_em + elec_ea + elec_sw + elec_ld + elec_se)

            raw_seats = [float((elec_ni/elec_tot)*seat_total), float((elec_sc/elec_tot)*seat_total),
                          float((elec_ne/elec_tot)*seat_total), float((elec_nw/elec_tot)*seat_total),
                          float((elec_yh/elec_tot)*seat_total), float((elec_cy/elec_tot)*seat_total),
                          float((elec_wm/elec_tot)*seat_total), float((elec_em/elec_tot)*seat_total),
                          float((elec_ea/elec_tot)*seat_total), float((elec_sw/elec_tot)*seat_total),
                          float((elec_ld/elec_tot)*seat_total), float((elec_se/elec_tot)*seat_total)]

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

            if seats_cy ++ seats_ea ++ seats_em ++ seats_ld ++ seats_ne ++ seats_ni ++ seats_nw ++ seats_sc ++ seats_se ++ seats_sw ++ seats_wm ++ seats_yh  == seat_total:
                print("Seat total valid \n\n\n")
            else:
                print("Seat total does not equal seat_total")
                
            ni = saferound([(uup_ni/tot_votes_ni) * seats_ni, (sdl_ni/tot_votes_ni) * seats_ni,
                            (dup_ni/tot_votes_ni) * seats_ni, (sif_ni/tot_votes_ni) * seats_ni,
                            (grn_ni/tot_votes_ni) * seats_ni, (all_ni/tot_votes_ni) * seats_ni,
                            (mnr_ni/tot_votes_ni) * seats_ni, (oth_ni/tot_votes_ni) * seats_ni,
                            ],places=0)

            sc = saferound([(con_sc/tot_votes_sc) * seats_sc, (lab_sc/tot_votes_sc) * seats_sc,
                      (lib_sc/tot_votes_sc) * seats_sc, (nat_sc/tot_votes_sc) * seats_sc,
                      (grn_sc/tot_votes_sc) * seats_sc, (brx_sc/tot_votes_sc) * seats_sc,
                      (mnr_sc/tot_votes_sc) * seats_sc, (oth_sc/tot_votes_sc) * seats_sc],places=0)

            ne = saferound([(con_ne/tot_votes_ne) * seats_ne, (lab_ne/tot_votes_ne) * seats_ne,
                      (lib_ne/tot_votes_ne) * seats_ne, (nat_ne/tot_votes_ne) * seats_ne,
                      (grn_ne/tot_votes_ne) * seats_ne, (brx_ne/tot_votes_ne) * seats_ne,
                      (mnr_ne/tot_votes_ne) * seats_ne, (oth_ne/tot_votes_ne) * seats_ne],places=0)

            nw = saferound([(con_nw/tot_votes_nw) * seats_nw, (lab_nw/tot_votes_nw) * seats_nw,
                      (lib_nw/tot_votes_nw) * seats_nw, (nat_nw/tot_votes_nw) * seats_nw,
                      (grn_nw/tot_votes_nw) * seats_nw, (brx_nw/tot_votes_nw) * seats_nw,
                      (mnr_nw/tot_votes_nw) * seats_nw, (oth_nw/tot_votes_nw) * seats_nw],places=0)

            yh = saferound([(con_yh/tot_votes_yh) * seats_yh, (lab_yh/tot_votes_yh) * seats_yh,
                      (lib_yh/tot_votes_yh) * seats_yh, (nat_yh/tot_votes_yh) * seats_yh,
                      (grn_yh/tot_votes_yh) * seats_yh, (brx_yh/tot_votes_yh) * seats_yh,
                      (mnr_yh/tot_votes_yh) * seats_yh, (oth_yh/tot_votes_yh) * seats_yh],places=0)

            cy = saferound([(con_cy/tot_votes_cy) * seats_cy, (lab_cy/tot_votes_cy) * seats_cy,
                      (lib_cy/tot_votes_cy) * seats_cy, (nat_cy/tot_votes_cy) * seats_cy,
                      (grn_cy/tot_votes_cy) * seats_cy, (brx_cy/tot_votes_cy) * seats_cy,
                      (mnr_cy/tot_votes_cy) * seats_cy, (oth_cy/tot_votes_cy) * seats_cy],places=0)

            wm = saferound([(con_wm/tot_votes_wm) * seats_wm, (lab_wm/tot_votes_wm) * seats_wm,
                      (lib_wm/tot_votes_wm) * seats_wm, (nat_wm/tot_votes_wm) * seats_wm,
                      (grn_wm/tot_votes_wm) * seats_wm, (brx_wm/tot_votes_wm) * seats_wm,
                      (mnr_wm/tot_votes_wm) * seats_wm, (oth_wm/tot_votes_wm) * seats_wm],places=0)

            em = saferound([(con_em/tot_votes_em) * seats_em, (lab_em/tot_votes_em) * seats_em,
                      (lib_em/tot_votes_em) * seats_em, (nat_em/tot_votes_em) * seats_em,
                      (grn_em/tot_votes_em) * seats_em, (brx_em/tot_votes_em) * seats_em,
                      (mnr_em/tot_votes_em) * seats_em, (oth_em/tot_votes_em) * seats_em],places=0)

            ea = saferound([(con_ea/tot_votes_ea) * seats_ea, (lab_ea/tot_votes_ea) * seats_ea,
                      (lib_ea/tot_votes_ea) * seats_ea, (nat_ea/tot_votes_ea) * seats_ea,
                      (grn_ea/tot_votes_ea) * seats_ea, (brx_ea/tot_votes_ea) * seats_ea,
                      (mnr_ea/tot_votes_ea) * seats_ea, (oth_ea/tot_votes_ea) * seats_ea],places=0)

            sw = saferound([(con_sw/tot_votes_sw) * seats_sw, (lab_sw/tot_votes_sw) * seats_sw,
                      (lib_sw/tot_votes_sw) * seats_sw, (nat_sw/tot_votes_sw) * seats_sw,
                      (grn_sw/tot_votes_sw) * seats_sw, (brx_sw/tot_votes_sw) * seats_sw,
                      (mnr_sw/tot_votes_sw) * seats_sw, (oth_sw/tot_votes_sw) * seats_sw],places=0)

            ld = saferound([(con_ld/tot_votes_ld) * seats_ld, (lab_ld/tot_votes_ld) * seats_ld,
                      (lib_ld/tot_votes_ld) * seats_ld, (nat_ld/tot_votes_ld) * seats_ld,
                      (grn_ld/tot_votes_ld) * seats_ld, (brx_ld/tot_votes_ld) * seats_ld,
                      (mnr_ld/tot_votes_ld) * seats_ld, (oth_ld/tot_votes_ld) * seats_ld],places=0)

            se = saferound([(con_se/tot_votes_se) * seats_se, (lab_se/tot_votes_se) * seats_se,
                      (lib_se/tot_votes_se) * seats_se, (nat_se/tot_votes_se) * seats_se,
                      (grn_se/tot_votes_se) * seats_se, (brx_se/tot_votes_se) * seats_se,
                      (mnr_se/tot_votes_se) * seats_se, (oth_se/tot_votes_se) * seats_se],places=0)
            
            con = int(sc[0]+ne[0]+nw[0]+yh[0]+cy[0]+wm[0]+em[0]+ea[0]+sw[0]+ld[0]+se[0])

            lab = int(sc[1]+ne[1]+nw[1]+yh[1]+cy[1]+wm[1]+em[1]+ea[1]+sw[1]+ld[1]+se[1])

            lib = int(sc[2]+ne[2]+nw[2]+yh[2]+cy[2]+wm[2]+em[2]+ea[2]+sw[2]+ld[2]+se[2])
            
            grn = int(ni[4]+sc[4]+ne[4]+nw[4]+yh[4]+cy[4]+wm[4]+em[4]+ea[4]+sw[4]+ld[4]+se[4])
            
            brx = int(sc[5]+ne[5]+nw[5]+yh[5]+cy[5]+wm[5]+em[5]+ea[5]+sw[5]+ld[5]+se[5])

            nat = int(sc[3]+ne[3]+nw[3]+yh[3]+cy[3]+wm[3]+em[3]+ea[3]+sw[3]+ld[3]+se[3])

            snp = int(sc[3])

            pcy = int(cy[3])

            oth = int(sc[7]+ne[7]+nw[7]+yh[7]+cy[7]+wm[7]+em[7]+ea[7]+sw[7]+ld[7]+se[7]+ni[7])

            mnr = int(sc[6]+ne[6]+nw[6]+yh[6]+cy[6]+wm[6]+em[6]+ea[6]+sw[6]+ld[6]+se[6]+ni[6])

            uup = int(ni[0])

            sdl = int(ni[1])

            sif = int(ni[3])

            dup = int(ni[2])

            ali = int(ni[5])

            print("Election result:\nConservative:",con,
                                  "\nLabour:",lab,
                                  "\nLiberal:",lib,
                                  "\nUKIP/Brex./Reform:",brx,
                                  "\nGreen:",grn,
                                  "\nSNP",snp,
                                  "\nPlaid Cymru", pcy,
                                  "\nUUP",uup,
                                  "\nSDLP",sdl,
                                  "\nSinn Féin",sif,
                                  "\nDUP",dup,
                                  "\nAlliance:",ali,
                                  "\nOthers",oth,
                                  "\nMinority Parties",mnr,
                    '\n\nTotal seats:', con+lab+lib+nat+oth+mnr+uup+sdl+sif+dup+grn+ali+brx)

            reg_seats = [seats_ni,seats_sc,seats_ne,seats_nw,seats_yh,seats_cy,
                         seats_wm,seats_em,seats_ea,seats_sw,seats_ld,seats_se]

            reg_raw = [sc,ne,nw,yh,cy,wm,em,ea,sw,ld,se,ni]
            reg = pd.DataFrame(
                reg_raw,columns=["Con","Lab","Lib","Nat","Grn","Brx","Min","Oth"],
                index=['SC','NE','NW','YH','CY','WM','EM','EA','SW','LD','SE','NI'],dtype=int)

            return reg

        else:
            print("Please specify whether analysis is 6 party or 8 party: \n (6 party = pre-2010)")

        '''

    def scot_senate(self, infile):
        # only eight party version available for now
        data = pd.read_csv(infile,delimiter=';')

        # Highland and Island
        con_hi = data.loc[data['County'] == 'Highland', 'CON'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'CON'].sum() ++ data.loc[data['County'] == 'Western Isles', 'CON'].sum()
        lab_hi = data.loc[data['County'] == 'Highland', 'LAB'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'LAB'].sum() ++ data.loc[data['County'] == 'Western Isles', 'LAB'].sum()
        lib_hi = data.loc[data['County'] == 'Highland', 'LIB'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'LIB'].sum() ++ data.loc[data['County'] == 'Western Isles', 'LIB'].sum()
        brx_hi = data.loc[data['County'] == 'Highland', 'UKIP'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'UKIP'].sum() ++ data.loc[data['County'] == 'Western Isles', 'UKIP'].sum()
        grn_hi = data.loc[data['County'] == 'Highland', 'Green'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'Green'].sum() ++ data.loc[data['County'] == 'Western Isles', 'Green'].sum()
        nat_hi = data.loc[data['County'] == 'Highland', 'NAT'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'NAT'].sum() ++ data.loc[data['County'] == 'Western Isles', 'NAT'].sum()
        mnr_hi = data.loc[data['County'] == 'Highland', 'MIN'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'MIN'].sum() ++ data.loc[data['County'] == 'Western Isles', 'MIN'].sum()
        oth_hi = data.loc[data['County'] == 'Highland', 'OTH'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'OTH'].sum() ++ data.loc[data['County'] == 'Western Isles', 'OTH'].sum()
        tot_votes_hi = con_hi + lab_hi + lib_hi + brx_hi + grn_hi + nat_hi + mnr_hi + oth_hi
        elec_hi = data.loc[data['County'] == 'Highland', 'Electorate'].sum() ++ data.loc[data['County'] == 'Argyll and Bute', 'Electorate'].sum() ++ data.loc[data['County'] == 'Western Isles', 'Electorate'].sum()
