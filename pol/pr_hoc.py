#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Modularising upcoming
'''

import pandas as pd
import sys

from iteround import saferound

def dhondt(nSeats, votes, verbose=False):
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


infile = 'electoral_calculus_data/2010.csv'
data = pd.read_csv(infile,delimiter=';')
seat_total = 650-2 # list containing each for each?[] 

seat_totals = [630-1, 630-2, 630-2, 630-2, 630-2, 635-2, 635-2, 635-2, 650-2, \
               650-2, 651-2, 659-2, 659-2, 650-2, 650-2, 650-2, 650-2, 650-2] # Total in the actual GE - number of constituencies whose population is too low to gain a seat

counties = data['County'].unique()
county_votes = []
electorates = {}
seats = {}
party_votes = {}

for cou in counties:
    county_votes.append(data.loc[data['County'] == cou, 'Electorate'].sum())

for i in range(len(counties)):
    electorates[counties[i]] = county_votes[i]
    party_votes[counties[i]] = {'CON': data.loc[data['County'] == counties[i], 'CON'].sum(),
                                'LAB': data.loc[data['County'] == counties[i], 'LAB'].sum(),
                                'LIB': data.loc[data['County'] == counties[i], 'LIB'].sum(),
                                'UKIP': data.loc[data['County'] == counties[i], 'UKIP'].sum(),
                                'Green': data.loc[data['County'] == counties[i], 'Green'].sum(),
                                'NAT': data.loc[data['County'] == counties[i], 'NAT'].sum(),
                                'MIN': data.loc[data['County'] == counties[i], 'MIN'].sum(),
                                'OTH': data.loc[data['County'] == counties[i], 'OTH'].sum()}

total_elec = sum(county_votes)

raw_seats = []
for tot in electorates.values():
    a = (tot/total_elec)*seat_total
    if a < 0.5:
        a += 1.0
    raw_seats.append(a)
rnd_seats = saferound(raw_seats, places=0)

for j in range(len(counties)):
    seats[counties[j]] = int(rnd_seats[j])

seats_ni = {}
party_votes_ni = {}
rnd_seats_ni = rnd_seats[-6:]

ni_keys = ['Antrim', 'Down', 'Armagh', 'Londonderry', 'Tyrone', 'Fermanagh']

for ky in ni_keys:
    vl = seats.pop(ky)
    vl = party_votes.pop(ky)
    seats_ni[ky] = vl
    party_votes_ni[ky] = {'UUP': data.loc[data['County'] == counties[i], 'CON'].sum(),
                          'SDLP': data.loc[data['County'] == counties[i], 'LAB'].sum(),
                          'DUP': data.loc[data['County'] == counties[i], 'LIB'].sum(),
                          'ALP': data.loc[data['County'] == counties[i], 'UKIP'].sum(),
                          'Green': data.loc[data['County'] == counties[i], 'Green'].sum(),
                          'SF': data.loc[data['County'] == counties[i], 'NAT'].sum(),
                          'MIN': data.loc[data['County'] == counties[i], 'MIN'].sum(),
                          'OTH': data.loc[data['County'] == counties[i], 'OTH'].sum()}

gb_res = []
ni_res = []

niv = iter(rnd_seats_ni)
for ok, di in party_votes_ni.items():
    #print(ok)
    results_ni = dhondt(next(niv), di, verbose=False)
    ni_res.append(results_ni)
ni_tots = {k: sum(d[k] for d in ni_res if k in d) for k in set(k for d in ni_res for k in d)}
print(ni_tots)

gbiv = iter(rnd_seats)
for gk, gi in party_votes.items():
    #print(gk)
    results = dhondt(next(gbiv), gi, verbose=False)
    gb_res.append(results)
tots = ni_tots = {k: sum(d[k] for d in gb_res if k in d) for k in set(k for d in gb_res for k in d)}
print(tots)
