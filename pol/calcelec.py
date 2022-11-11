#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:10:14 2022

Brit Senate - Third iteration

@author: e.mcgill

This is the newest extant version - elecalculator.py is deprecated
"""

from iteround import saferound
import pandas as pd
# import sys

class CalcElec:
    
    def __init__(self, infile, sixparty=False, elec_system="HW", seat_total=250):
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

    def votes_per_party(self): # will need a 3D array
        if self.sixparty:
            # 1 = Northern Ireland
            ni = []
            uup_ni = self.data.loc[self.data['Area'] == 1, 'CON'].sum()
            sdl_ni = self.data.loc[self.data['Area'] == 1, 'LAB'].sum()
            dup_ni = self.data.loc[self.data['Area'] == 1, 'LIB'].sum()
            sif_ni = self.data.loc[self.data['Area'] == 1, 'NAT'].sum()
            mnr_ni = self.data.loc[self.data['Area'] == 1, 'MIN'].sum()
            oth_ni = self.data.loc[self.data['Area'] == 1, 'OTH'].sum()
            ni_votes = ni.append(uup_ni, sdl_ni, dup_ni, sif_ni, mnr_ni, oth_ni)
            # 2 = Scotland
            sc = []
            con_sc = self.data.loc[self.data['Area'] == 2, 'CON'].sum()
            lab_sc = self.data.loc[self.data['Area'] == 2, 'LAB'].sum()
            lib_sc = self.data.loc[self.data['Area'] == 2, 'LIB'].sum()
            nat_sc = self.data.loc[self.data['Area'] == 2, 'NAT'].sum()
            mnr_sc = self.data.loc[self.data['Area'] == 2, 'MIN'].sum()
            oth_sc = self.data.loc[self.data['Area'] == 2, 'OTH'].sum()
            sc_votes = sc.append(con_sc, lab_sc, lib_sc, nat_sc, mnr_sc, oth_sc)
            # 3 = North East
            ne = []
            con_ne = self.data.loc[self.data['Area'] == 3, 'CON'].sum()
            lab_ne = self.data.loc[self.data['Area'] == 3, 'LAB'].sum()
            lib_ne = self.data.loc[self.data['Area'] == 3, 'LIB'].sum()
            nat_ne = self.data.loc[self.data['Area'] == 3, 'NAT'].sum()
            mnr_ne = self.data.loc[self.data['Area'] == 3, 'MIN'].sum()
            oth_ne = self.data.loc[self.data['Area'] == 3, 'OTH'].sum()
            ne_votes = ne.append(con_ne, lab_ne, lib_ne, nat_ne, mnr_ne, oth_ne)
            # 4 = North West
            nw = []
            con_nw = self.data.loc[self.data['Area'] == 4, 'CON'].sum()
            lab_nw = self.data.loc[self.data['Area'] == 4, 'LAB'].sum()
            lib_nw = self.data.loc[self.data['Area'] == 4, 'LIB'].sum()
            nat_nw = self.data.loc[self.data['Area'] == 4, 'NAT'].sum()
            mnr_nw = self.data.loc[self.data['Area'] == 4, 'MIN'].sum()
            oth_nw = self.data.loc[self.data['Area'] == 4, 'OTH'].sum()
            nw_votes = nw.append(con_nw, lab_nw, lib_nw, nat_nw, mnr_nw, oth_nw)
            # 5 = Yorkshire and Humber
            yh = []
            con_yh = self.data.loc[self.data['Area'] == 5, 'CON'].sum()
            lab_yh = self.data.loc[self.data['Area'] == 5, 'LAB'].sum()
            lib_yh = self.data.loc[self.data['Area'] == 5, 'LIB'].sum()
            nat_yh = self.data.loc[self.data['Area'] == 5, 'NAT'].sum()
            mnr_yh = self.data.loc[self.data['Area'] == 5, 'MIN'].sum()
            oth_yh = self.data.loc[self.data['Area'] == 5, 'OTH'].sum()
            yh_votes = yh.append(con_yh, lab_yh, lib_yh, nat_yh, mnr_yh, oth_yh)
            # 6 = Cymru
            cy = []
            con_cy = self.data.loc[self.data['Area'] == 6, 'CON'].sum()
            lab_cy = self.data.loc[self.data['Area'] == 6, 'LAB'].sum()
            lib_cy = self.data.loc[self.data['Area'] == 6, 'LIB'].sum()
            nat_cy = self.data.loc[self.data['Area'] == 6, 'NAT'].sum()
            mnr_cy = self.data.loc[self.data['Area'] == 6, 'MIN'].sum()
            oth_cy = self.data.loc[self.data['Area'] == 6, 'OTH'].sum()
            cy_votes = cy.append(con_cy, lab_cy, lib_cy, nat_cy, mnr_cy, oth_cy)
            # 7 = West Midlands
            wm = []
            con_wm = self.data.loc[self.data['Area'] == 7, 'CON'].sum()
            lab_wm = self.data.loc[self.data['Area'] == 7, 'LAB'].sum()
            lib_wm = self.data.loc[self.data['Area'] == 7, 'LIB'].sum()
            nat_wm = self.data.loc[self.data['Area'] == 7, 'NAT'].sum()
            mnr_wm = self.data.loc[self.data['Area'] == 7, 'MIN'].sum()
            oth_wm = self.data.loc[self.data['Area'] == 7, 'OTH'].sum()
            wm_votes = wm.append(con_wm, lab_wm, lib_wm, nat_wm, mnr_wm, oth_wm)
            # 8 = East Midlands
            em = []
            con_em = self.data.loc[self.data['Area'] == 8, 'CON'].sum()
            lab_em = self.data.loc[self.data['Area'] == 8, 'LAB'].sum()
            lib_em = self.data.loc[self.data['Area'] == 8, 'LIB'].sum()
            nat_em = self.data.loc[self.data['Area'] == 8, 'NAT'].sum()
            mnr_em = self.data.loc[self.data['Area'] == 8, 'MIN'].sum()
            oth_em = self.data.loc[self.data['Area'] == 8, 'OTH'].sum()
            em_votes = em.append(con_em, lab_em, lib_em, nat_em, mnr_em, oth_em)
            # 9 = East Anglia
            ea = []
            con_ea = self.data.loc[self.data['Area'] == 9, 'CON'].sum()
            lab_ea = self.data.loc[self.data['Area'] == 9, 'LAB'].sum()
            lib_ea = self.data.loc[self.data['Area'] == 9, 'LIB'].sum()
            nat_ea = self.data.loc[self.data['Area'] == 9, 'NAT'].sum()
            mnr_ea = self.data.loc[self.data['Area'] == 9, 'MIN'].sum()
            oth_ea = self.data.loc[self.data['Area'] == 9, 'OTH'].sum()
            ea_votes = ea.append(con_ea, lab_ea, lib_ea, nat_ea, mnr_ea, oth_ea)
            # 10 = South West
            sw = []
            con_sw = self.data.loc[self.data['Area'] == 10, 'CON'].sum()
            lab_sw = self.data.loc[self.data['Area'] == 10, 'LAB'].sum()
            lib_sw = self.data.loc[self.data['Area'] == 10, 'LIB'].sum()
            nat_sw = self.data.loc[self.data['Area'] == 10, 'NAT'].sum()
            mnr_sw = self.data.loc[self.data['Area'] == 10, 'MIN'].sum()
            oth_sw = self.data.loc[self.data['Area'] == 10, 'OTH'].sum()
            sw_votes = sw.append(con_sw, lab_sw, lib_sw, nat_sw, mnr_sw, oth_sw)
            # 11 = London
            ld = []
            con_ld = self.data.loc[self.data['Area'] == 11, 'CON'].sum()
            lab_ld = self.data.loc[self.data['Area'] == 11, 'LAB'].sum()
            lib_ld = self.data.loc[self.data['Area'] == 11, 'LIB'].sum()
            nat_ld = self.data.loc[self.data['Area'] == 11, 'NAT'].sum()
            mnr_ld = self.data.loc[self.data['Area'] == 11, 'MIN'].sum()
            oth_ld = self.data.loc[self.data['Area'] == 11, 'OTH'].sum()
            ld_votes = ld.append(con_ld, lab_ld, lib_ld, nat_ld, mnr_ld, oth_ld)
            # 12 = South East
            se = []
            con_se = self.data.loc[self.data['Area'] == 12, 'CON'].sum()
            lab_se = self.data.loc[self.data['Area'] == 12, 'LAB'].sum()
            lib_se = self.data.loc[self.data['Area'] == 12, 'LIB'].sum()
            nat_se = self.data.loc[self.data['Area'] == 12, 'NAT'].sum()
            mnr_se = self.data.loc[self.data['Area'] == 12, 'MIN'].sum()
            oth_se = self.data.loc[self.data['Area'] == 12, 'OTH'].sum()
            se_votes = sw.append(con_sw, lab_sw, lib_sw, nat_sw, mnr_sw, oth_sw)

            votes = []
            party_matrix = votes.append(ni_votes, sc_votes, ne_votes, nw_votes, yh_votes,
                                        cy_votes, wm_votes, em_votes, ea_votes, sw_votes,
                                        ld_votes, se_votes)
            return party_matrix

        elif not self.sixparty:
            pass

    def electorate(self):
        total_votes = self.votes_per_party()
        electorate = []
        electorate_array = electorate.append(total_votes[0], total_votes[1], total_votes[2],
                                             total_votes[3], total_votes[4], total_votes[5],
                                             total_votes[6], total_votes[7], total_votes[8],
                                             total_votes[9], total_votes[10], total_votes[11])
        return electorate_array
        # this will take in regional arrays and output the tot_vote_reg variables

    def hamilton(self):
        rnd_seats = self.regional_seats()
        party_totals = self.votes_per_party()
        vote_totals = self.electorate()

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

        if seats_cy ++ seats_ea ++ seats_em ++ seats_ld ++ seats_ne ++ seats_ni ++ seats_nw ++ seats_sc ++ seats_se ++ seats_sw ++ seats_wm ++ seats_yh  == self.seat_total:
            print("Seat total valid \n\n\n")
        else:
            print("Seat total does not equal seat_total")

        # copy from if loop below

    def dhondt(self, votes, verbose=False):
        """
        Author: https://gist.github.com/brunosan
        nSeats is the number of seats
        votes is a dictionary with the key:value {'party':votes}
        verbose is an option to print designation info
        """
        t_votes=votes.copy()
        seats={}
        for key in votes: seats[key]=0
        while sum(seats.values()) < self.seat_total: # should be regional not national seat values
            max_v= max(t_votes.values())
            next_seat=list(t_votes.keys())[list(t_votes.values()).index(max_v)]
            if next_seat in seats:
                seats[next_seat]+=1
            else:
                seats[next_seat]=1

            if verbose:
                print("{} Escaño: {}".format(sum(seats.values()),next_seat))
                for key in t_votes:
                    print("\t{} [{}]: {:.1f}".format(key,seats[key],t_votes[key]))
                print("\b")
            t_votes[next_seat]=votes[next_seat]/(seats[next_seat]+1)
        return seats

    def mms(self):
        pass
        # to complete at a later date

    def reg_party(self): # rejigging whole file by breaking up this function (in progress...)
        if self.sixparty:

            tot_votes_ni = uup_ni + sdl_ni + dup_ni + sif_ni + mnr_ni + oth_ni

            tot_votes_sc = con_sc + lab_sc + lib_sc + nat_sc + mnr_sc + oth_sc

            tot_votes_ne = con_ne + lab_ne + lib_ne + nat_ne + mnr_ne + oth_ne

            tot_votes_nw = con_nw + lab_nw + lib_nw + nat_nw + mnr_nw + oth_nw

            tot_votes_yh = con_yh + lab_yh + lib_yh + nat_yh + mnr_yh + oth_yh

            tot_votes_cy = con_cy + lab_cy + lib_cy + nat_cy + mnr_cy + oth_cy

            tot_votes_wm = con_wm + lab_wm + lib_wm + nat_wm + mnr_wm + oth_wm

            tot_votes_em = con_em + lab_em + lib_em + nat_em + mnr_em + oth_em

            tot_votes_ea = con_ea + lab_ea + lib_ea + nat_ea + mnr_ea + oth_ea

            tot_votes_sw = con_sw + lab_sw + lib_sw + nat_sw + mnr_sw + oth_sw

            tot_votes_ld = con_ld + lab_ld + lib_ld + nat_ld + mnr_ld + oth_ld

            tot_votes_se = con_se + lab_se + lib_se + nat_se + mnr_se + oth_se


            if self.elec_system == "HW": # new function for this
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

                reg_seats = [seats_ni,seats_sc,seats_ne,seats_nw,seats_yh,seats_cy,
                         seats_wm,seats_em,seats_ea,seats_sw,seats_ld,seats_se]

                reg_raw = [sc,ne,nw,yh,cy,wm,em,ea,sw,ld,se,ni]
                reg = pd.DataFrame(
                    reg_raw,columns=["Con","Lab","Lib","Nat","Min","Oth"],
                    index=['SC','NE','NW','YH','CY','WM','EM','EA','SW','LD','SE','NI'],dtype=int)

                return reg

            elif self.elec_system == "DH":
                ni_dh = {'UUP': uup_ni, 'SDLP':sdl_ni, 'DUP': dup_ni, 'SF':  sif_ni, 'Min': mnr_ni, 'Oth': oth_ni}
                sc_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'SNP': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                ne_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                nw_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                yh_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                cy_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'PC':  nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                wm_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                em_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                ea_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                sw_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                ld_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}
                se_dh = {'Con': con_ne, 'Lab': lab_ne, 'Lib': lib_ne, 'Nat': nat_ne, 'Min': mnr_ne, 'Oth': oth_ne}

            else:
                print("Enter a valid electoral system")

    ###############################################################################
        
        elif sixparty == False:
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
