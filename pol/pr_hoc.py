#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Modularising to be completed
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

########################################################################################################

infiles = ['electoral_calculus_data/1955.csv', 'electoral_calculus_data/1959.csv',
            'electoral_calculus_data/1964.csv', 'electoral_calculus_data/1966.csv',
            'electoral_calculus_data/1970.csv', 'electoral_calculus_data/1974f.csv',
            'electoral_calculus_data/1974o.csv', 'electoral_calculus_data/1979.csv',
            'electoral_calculus_data/1983.csv', 'electoral_calculus_data/1987.csv',
            'electoral_calculus_data/1992.csv', 'electoral_calculus_data/1997.csv',
            'electoral_calculus_data/2001.csv', 'electoral_calculus_data/2005.csv',
            'electoral_calculus_data/2010.csv', 'electoral_calculus_data/2015.csv',
            'electoral_calculus_data/2017.csv', 'electoral_calculus_data/2019.csv',
            'electoral_calculus_data/2024-05ECpoll.csv',
            'electoral_calculus_data/2024-052ECpoll.csv',
            'electoral_calculus_data/2024-06-07ECpoll.csv',
            'YG-24-06-01.csv', 'BE-24-06-07.csv',
            'electoral_calculus_data/2024-06-14ECpoll.csv',
            'BE-24-06-16.csv', 'IPSOS-24-06-18.csv',
            'electoral_calculus_data/2024-06-21ECpoll.csv',
            'BE-24-06-22.csv', 'BE-24-06-29.csv',
            'electoral_calculus_data/2024-06-27ECpoll.csv',
            'YG-24-06-22.csv',
            'electoral_calculus_data/2024-06-30ECpoll.csv',
            'YG-24-07-03.csv',
            'electoral_calculus_data/2024-07-04ECpoll.csv',
            'electoral_calculus_data/2024.csv', 'electoral_calculus_data/2024-10-17ECpoll.csv',
            'MIC-2024-12-28.csv', 'electoral_calculus_data/2025-04ECpoll.csv',
            'electoral_calculus_data/2025-06ECpoll.csv', 'electoral_calculus_data/2025-07ECpoll.csv',
            'electoral_calculus_data/2025-08ECpoll.csv', 'electoral_calculus_data/2025-09ECpoll.csv',
            'electoral_calculus_data/2025-09ECpoll-London.csv', 'electoral_calculus_data/2025-09ECpoll-District.csv',
            'PLMR-25Q4-NTV-C.csv', 'PLMR-25Q4-NTV-D.csv',
            'PLMR-25Q4-TV-C.csv', 'PLMR-25Q4-TV-D.csv',
            'electoral_calculus_data/2024-district.csv'] # now add values to seat_totals

for i, val in enumerate(infiles):
    print(f'{i}: {val}')

infile = infiles[int(sys.argv[1])] #'electoral_calculus_data/1955.csv'
print('\nElection year:',infile)
data = pd.read_csv(infile,delimiter=';')

seat_totals = [630-1, 630-2, 630-2, 630-2, 630-2, 635-2, 635-2, 635-2, 650-2, \
               650-2, 651-2, 659-2, 659-2, 650-2, 650-2, 650-2, 650-2, 650-2, \
               650, 650, 650, 650-2, 650-2, 650, 650-2, 650-2, 650-2, 650-2, \
               650-2, 650-2, 650-2, 650-2, 650-2, 650-2, 650-2, 650-2, 650-2, 650-2, 650-2, 650-2,
               650-2, 650-2, 650-2, 650-1, 650-2, 650-1, 650-2, 650-1, 650-1] # now choose NI counties!
               # Total in the actual GE - number of constituencies whose population is too low to gain a seat
seat_total = seat_totals[int(sys.argv[1])] # list containing each for each?[] 


# For County or District
district = input("[C] County (administrative areas) or [D] District (4-7 seat constituencies)? \n")
if district in ['c', 'C', 'County', 'county']:
    district = False
elif district in ['d', 'D', 'District', 'district']:
    district = True
else:
    print("Enter a valid seat type")
    sys.exit


########################################################################################################

counties = data['County'].unique()
county_votes = []
electorates = {}
seats = {}
party_votes = {}

for cou in counties:
    county_votes.append(data.loc[data['County'] == cou, 'Electorate'].sum())

for i in range(len(counties)):
    electorates[counties[i]] = county_votes[i]
    try:
        party_votes[counties[i]] = {'CON': data.loc[data['County'] == counties[i], 'CON'].sum(),
                                'LAB': data.loc[data['County'] == counties[i], 'LAB'].sum(),
                                'LIB': data.loc[data['County'] == counties[i], 'LIB'].sum(),
                                'UKIP': data.loc[data['County'] == counties[i], 'UKIP'].sum(),
                                'Green': data.loc[data['County'] == counties[i], 'Green'].sum(),
                                'NAT': data.loc[data['County'] == counties[i], 'NAT'].sum(),
                                'MIN': data.loc[data['County'] == counties[i], 'MIN'].sum(),
                                'OTH': data.loc[data['County'] == counties[i], 'OTH'].sum()}
    except:
        party_votes[counties[i]] = {'CON': data.loc[data['County'] == counties[i], 'CON'].sum(),
                                'LAB': data.loc[data['County'] == counties[i], 'LAB'].sum(),
                                'LIB': data.loc[data['County'] == counties[i], 'LIB'].sum(),
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
print('\nNumber of seats by district (Northern Ireland calculated at-large for County-level):\n\n',seats)

seats_ni = {}
party_votes_ni = {}
rnd_seats_ni = rnd_seats[-6:]

# county-by-county
if district:
    ni_keys = ['Antrim and the Lagan Valley', 'Belfast', 'Armagh and Down', 'Ulster West']
else:
    ni_keys = ['Antrim', 'Down', 'Armagh', 'Londonderry', 'Tyrone', 'Fermanagh']


for ky in ni_keys:
    vl = seats.pop(ky)
    vl = party_votes.pop(ky)
    seats_ni[ky] = vl
    try:
        party_votes_ni[ky] = {'UUP': data.loc[data['County'] == counties[i], 'CON'].sum(),
                          'SDLP': data.loc[data['County'] == counties[i], 'LAB'].sum(),
                          'DUP': data.loc[data['County'] == counties[i], 'LIB'].sum(),
                          'ALP': data.loc[data['County'] == counties[i], 'UKIP'].sum(),
                          'Green': data.loc[data['County'] == counties[i], 'Green'].sum(),
                          'SF': data.loc[data['County'] == counties[i], 'NAT'].sum(),
                          'MIN': data.loc[data['County'] == counties[i], 'MIN'].sum(),
                          'OTH': data.loc[data['County'] == counties[i], 'OTH'].sum()}
    except:
        party_votes_ni[ky] = {'UUP': data.loc[data['County'] == counties[i], 'CON'].sum(),
                          'SDLP': data.loc[data['County'] == counties[i], 'LAB'].sum(),
                          'DUP': data.loc[data['County'] == counties[i], 'LIB'].sum(),
                          'SF': data.loc[data['County'] == counties[i], 'NAT'].sum(),
                          'MIN': data.loc[data['County'] == counties[i], 'MIN'].sum(),
                          'OTH': data.loc[data['County'] == counties[i], 'OTH'].sum()}

# NI at large
try:
    party_votes_nil = {'UUP': data.loc[data['Area'] == 1, 'CON'].sum(),
                      'SDLP': data.loc[data['Area'] == 1, 'LAB'].sum(),
                      'DUP': data.loc[data['Area'] == 1, 'LIB'].sum(),
                      'ALP': data.loc[data['Area'] == 1, 'UKIP'].sum(),
                      'TUV': data.loc[data['Area'] == 1, 'Green'].sum(),
                      'SF': data.loc[data['Area'] == 1, 'NAT'].sum(),
                      'MIN': data.loc[data['Area'] == 1, 'MIN'].sum(),
                      'OTH': data.loc[data['Area'] == 1, 'OTH'].sum()}
except:
    party_votes_nil = {'UUP': data.loc[data['Area'] == 1, 'CON'].sum(),
                      'SDLP': data.loc[data['Area'] == 1, 'LAB'].sum(),
                      'DUP': data.loc[data['Area'] == 1, 'LIB'].sum(),
                      'SF': data.loc[data['Area'] == 1, 'NAT'].sum(),
                      'MIN': data.loc[data['Area'] == 1, 'MIN'].sum(),
                      'OTH': data.loc[data['Area'] == 1, 'OTH'].sum()}

########################################################################################################

gb_res = []
ni_res = []

# NI county-by-county
print('\nResults:')
niv = iter(rnd_seats_ni) # for county
for ok, di in party_votes_ni.items():
    #print(ok)
    results_ni = dhondt(next(niv), di, verbose=False)
    ni_res.append(results_ni)
    print(ok,results_ni, max(di, key=di.get))
ni_tots = {k: sum(d[k] for d in ni_res if k in d) for k in set(k for d in ni_res for k in d)}

# NI at large
#print(party_votes_nil)
ni_seats = sum(rnd_seats_ni)
nis = int(ni_seats)
nil_tots = dhondt(nis, party_votes_nil, verbose=False)

print('\n')
gbiv = iter(rnd_seats) # for county
for gk, gi in party_votes.items():
    #print(gk)
    results = dhondt(next(gbiv), gi, verbose=False)
    print(gk,results, max(gi, key=gi.get)) #,max(gi.values()))
    #print(gk,results)
    gb_res.append(results)
tots = {k: sum(d[k] for d in gb_res if k in d) for k in set(k for d in gb_res for k in d)}

print('\nNorthern Ireland by County', ni_tots)
print('\nNorthern Ireland at Large', nil_tots)
print('\nGreat Britain', tots,'\n')
