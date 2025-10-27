#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:04:42 2022

@author: e.mcgill
"""

from calcelec import CalcElec
import matplotlib.pyplot as plt
import numpy as np
import sys
#import argparse

# ham = CalcElec(infile='electoral_calculus_data/2019.csv', sixparty=False).hamilton()
# dhon = CalcElec(infile='electoral_calculus_data/2019.csv', sixparty=False).dhondt_calc()

def senate_calculate(six_election,eight_election):
    six_frames = []
    eight_frames = []
    for elec in six_election:
        result = CalcElec(infile=elec, sixparty=True).dhondt_calc()
        six_frames.append(result)
    
    for elec in eight_election:
        result = CalcElec(infile=elec, sixparty=False).dhondt_calc()
        eight_frames.append(result)

def plot_dhondt(six_election,eight_election):
    six_frames = []
    eight_frames = []
    seat_prompt = input("Please type in the desired seat total as an integer (>0): ")
    for elec in six_election:
        result = CalcElec(infile=elec, sixparty=True, seat_total=int(seat_prompt)).dhondt_calc(plot=True)
        six_frames.append(result)
    
    for elec in eight_election:
        result = CalcElec(infile=elec, sixparty=False, seat_total=int(seat_prompt)).dhondt_calc(plot=True)
        eight_frames.append(result)
    
    # print(eight_frames[0][0]) # array indices as follows: [con,lab,lib,snp,brx,grn,pcy,uup,sdl,sif,dup,oth,mnr]
    #print(len(six_frames)) # array indices as follows: [con,lab,lib,snp,pcy,uup,sdl,sif,dup,oth,mnr]
    
    labels = ['1955', '1959', '1964', '1966', '1970', '1974f', '1974o', '1979', '1983',
              '1987', '1992', '1997', '2001', '2005', '2010', '2015', '2017', '2019']
    con = np.array([(six_frames[0][0]+six_frames[0][5]), (six_frames[1][0]+six_frames[1][5]), (six_frames[2][0]+six_frames[2][5]),
                    (six_frames[3][0]+six_frames[3][5]), (six_frames[4][0]+six_frames[4][5]), (six_frames[5][0]),
                    (six_frames[6][0]), (six_frames[7][0]), (six_frames[8][0]), (six_frames[9][0]),
                    (six_frames[10][0]), (six_frames[11][0]), (six_frames[12][0]), (six_frames[13][0]),
                    (eight_frames[0][0]),(eight_frames[1][0]),(eight_frames[2][0]),(eight_frames[3][0])])
    lab = np.array([(six_frames[0][1]), (six_frames[1][1]), (six_frames[2][1]), (six_frames[3][1]), (six_frames[4][1]), (six_frames[5][1]),
                    (six_frames[6][1]), (six_frames[7][1]), (six_frames[8][1]), (six_frames[9][1]),
                    (six_frames[10][1]), (six_frames[11][1]), (six_frames[12][1]), (six_frames[13][1]),
                    (eight_frames[0][1]),(eight_frames[1][1]),(eight_frames[2][1]),(eight_frames[3][1])])
    lib = np.array([(six_frames[0][2]), (six_frames[1][2]), (six_frames[2][2]), (six_frames[3][2]), (six_frames[4][2]), (six_frames[5][2]),
                    (six_frames[6][2]), (six_frames[7][2]), (six_frames[8][2]), (six_frames[9][2]),
                    (six_frames[10][2]), (six_frames[11][2]), (six_frames[12][2]), (six_frames[13][2]),
                    (eight_frames[0][2]),(eight_frames[1][2]),(eight_frames[2][2]),(eight_frames[3][2])])
    brx = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 2, 4,
                    (eight_frames[0][4]),(eight_frames[1][4]),(eight_frames[2][4]),(eight_frames[3][4])])
    grn = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2,
                    (eight_frames[0][5]),(eight_frames[1][5]),(eight_frames[2][5]),(eight_frames[3][5])])
    nat = np.array([(six_frames[0][3]+six_frames[0][4]), (six_frames[1][3]+six_frames[1][4]), (six_frames[2][3]+six_frames[2][4]),
                    (six_frames[3][3]+six_frames[3][4]), (six_frames[4][3]+six_frames[4][4]), (six_frames[5][3]+six_frames[5][4]),
                    (six_frames[6][3]+six_frames[6][4]), (six_frames[7][3]+six_frames[7][4]), (six_frames[8][3]+six_frames[8][4]),
                    (six_frames[9][3]+six_frames[9][4]), (six_frames[10][3]+six_frames[10][4]), (six_frames[11][3]+six_frames[11][4]),
                    (six_frames[12][3]+six_frames[12][4]), (six_frames[13][3]+six_frames[13][4]),
                    (eight_frames[0][3])+(eight_frames[0][6]),(eight_frames[1][3])+(eight_frames[1][6]),
                    (eight_frames[2][3])+(eight_frames[2][6]),(eight_frames[3][3])+(eight_frames[3][6])])
    sdp = np.array([0, 0, 0, 0, 0, 0, 0, 0, (six_frames[8][10]), (six_frames[9][10]), 0, 0, 0, 0, 0, 0, 0, 0])
    oth = np.array([(int(seat_prompt)-con[0]-lab[0]-lib[0]-brx[0]-grn[0]-nat[0]), (int(seat_prompt)-con[1]-lab[1]-lib[1]-brx[1]-grn[1]-nat[1]),
                    (int(seat_prompt)-con[2]-lab[2]-lib[2]-brx[2]-grn[2]-nat[2]), (int(seat_prompt)-con[3]-lab[3]-lib[3]-brx[3]-grn[3]-nat[3]),
                    (int(seat_prompt)-con[4]-lab[4]-lib[4]-brx[4]-grn[4]-nat[4]), (int(seat_prompt)-con[5]-lab[5]-lib[5]-brx[5]-grn[5]-nat[5]),
                    (int(seat_prompt)-con[6]-lab[6]-lib[6]-brx[6]-grn[6]-nat[6]), (int(seat_prompt)-con[7]-lab[7]-lib[7]-brx[7]-grn[7]-nat[7]),
                    (int(seat_prompt)-con[8]-lab[8]-lib[8]-brx[8]-grn[8]-nat[8]-sdp[8]), (int(seat_prompt)-con[9]-lab[9]-lib[9]-brx[9]-grn[9]-nat[9]-sdp[9]),
                    (int(seat_prompt)-con[10]-lab[10]-lib[10]-brx[10]-grn[10]-nat[10]), (int(seat_prompt)-con[11]-lab[11]-lib[11]-brx[11]-grn[11]-nat[11]),
                    (int(seat_prompt)-con[12]-lab[12]-lib[12]-brx[12]-grn[12]-nat[12]), (int(seat_prompt)-con[13]-lab[13]-lib[13]-brx[13]-grn[13]-nat[13]),
                    (int(seat_prompt)-con[14]-lab[14]-lib[14]-brx[14]-grn[14]-nat[14]), (int(seat_prompt)-con[15]-lab[15]-lib[15]-brx[15]-grn[15]-nat[15]),
                    (int(seat_prompt)-con[16]-lab[16]-lib[16]-brx[16]-grn[16]-nat[16]), (int(seat_prompt)-con[17]-lab[17]-lib[17]-brx[17]-grn[17]-nat[17])])
    
    #= 0.5
    fig, ax = plt.subplots()
    ax.bar(labels, brx, color='cyan')
    ax.bar(labels, con, bottom=brx, color='blue')
    ax.bar(labels, lib, bottom=brx+con, color='gold')
    ax.bar(labels, oth, bottom=brx+con+lib, color='dimgrey')
    ax.bar(labels, sdp, bottom=brx+con+lib+oth, color='mediumvioletred')
    ax.bar(labels, lab, bottom=brx+con+lib+oth+sdp, color='red')
    ax.bar(labels, nat, bottom=brx+con+lib+oth+sdp+lab, color='forestgreen')
    ax.bar(labels, grn, bottom=brx+con+lib+oth+sdp+lab+nat, color='lime')
    ax.legend(["UKIP/Brexit/Reform", "Conservative", "Liberal (Democrat)", "Others, NI", "SDP", "Labour", "SNP, Plaid Cymru", "Green"])
    plt.axhline(y=int(seat_prompt)/2, color='black')
    plt.show()

def main():
    six_election = ['electoral_calculus_data/1955.csv', 'electoral_calculus_data/1959.csv',
                    'electoral_calculus_data/1964.csv', 'electoral_calculus_data/1966.csv',
                    'electoral_calculus_data/1970.csv', 'electoral_calculus_data/1974f.csv',
                    'electoral_calculus_data/1974o.csv', 'electoral_calculus_data/1979.csv',
                    'electoral_calculus_data/1983.csv', 'electoral_calculus_data/1987.csv',
                    'electoral_calculus_data/1992.csv', 'electoral_calculus_data/1997.csv',
                    'electoral_calculus_data/2001.csv', 'electoral_calculus_data/2005.csv', ]
    eight_election = [ 'electoral_calculus_data/2010.csv', 'electoral_calculus_data/2015.csv',
                       'electoral_calculus_data/2017.csv', 'electoral_calculus_data/2019.csv',
                       'electoral_calculus_data/2024.csv', 'PLMR-25Q4-NTV-C.csv', 'PLMR-25Q4-TV-C.csv']

    election_frames = []
    prompt_one = input("Type in electoral system, Hamilton/Largest Remainder (HW) or the D'Hondt Method (DH): ")

    if prompt_one in ['DH', 'dh', 'D\'Hondt', 'D\'hondt', 'DHondt', 'Dhondt']:
        prompt_two = input("Would you like to plot the results? ")
        if prompt_two in ['Yes', 'yes', 'y', 'Y', 'ok', 'OK', 'Okay', 'okay']:
            plot_dhondt(six_election, eight_election)
        else:
            seat_prompt = input("Please type in the desired seat total as an integer (>0): ")
            for elec in six_election:
                result = CalcElec(infile=elec, sixparty=True, seat_total=int(seat_prompt)).dhondt_calc()
                election_frames.append(result)
            for elec in eight_election:
                result = CalcElec(infile=elec, sixparty=False, seat_total=int(seat_prompt)).dhondt_calc()
                election_frames.append(result)
            return election_frames

    elif prompt_one in ['HW', 'hw', 'H', 'h', 'Hamilton', 'hamilton', 'Largest Remainder', 'Largest remainder', 'largest remainder']:
        seat_prompt = input("Please type in the desired seat total as an integer (>0): ")
        for elec in six_election:
            result = CalcElec(infile=elec, sixparty=True, seat_total=int(seat_prompt)).hamilton()
            election_frames.append(result)
        for elec in eight_election:
            result = CalcElec(infile=elec, sixparty=False, seat_total=int(seat_prompt)).hamilton()
            election_frames.append(result)
        return election_frames
    
    else:
        print("\n\n\nPlease enter a valid electoral system...")
        sys.exit()

if __name__ == '__main__':
    main()
