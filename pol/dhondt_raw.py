#!/usr/bin/env python3
# -*- coding: utf-8 -*-

####################### ELECTORAL SYSTEM ########################################
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


################################# RAW DATA - POLLS ###############################


# print("Electoral Calculus poll of polls, 01/2023 & LucidTalk (BT), 11/2022")
# ni = {'SF':320, 'DUP':270, 'APNI':150, 'UUP':90, 'SDLP':70, 'TUV':50, 'Grn':20, 'Oth': 30}
# sc = {'Con':153, 'Lab':280, 'Lib':60, 'Brx':10, 'Grn':24, 'SNP':456}
# ne = {'Con':231, 'Lab':567, 'Lib':48, 'Brx':75, 'Grn':56}
# nw = {'Con':224, 'Lab':583, 'Lib':52, 'Brx':67, 'Grn':54}
# yh = {'Con':267, 'Lab':529, 'Lib':57, 'Brx':73, 'Grn':51}
# cy = {'Con':221, 'Lab':507, 'Lib':33, 'Brx':49, 'Grn':23, 'PC':149}
# wm = {'Con':315, 'Lab':482, 'Lib':66, 'Brx':72, 'Grn':50}
# em = {'Con':340, 'Lab':458, 'Lib':55, 'Brx':71, 'Grn':50}
# ea = {'Con':348, 'Lab':403, 'Lib':110, 'Brx':72, 'Grn':50}
# sw = {'Con':315, 'Lab':379, 'Lib':158, 'Brx':70, 'Grn':52}
# ld = {'Con':172, 'Lab':605, 'Lib':91, 'Brx':60, 'Grn':59}
# se = {'Con':330, 'Lab':381, 'Lib':146, 'Brx':70, 'Grn':57}

# print ("Electoral Calculus poll of polls, 12/2019 & Exit poll NI 12/2019")
# ni = {'SF':228, 'DUP':306, 'APNI':168, 'UUP':117, 'SDLP':149, 'TUV':0, 'Grn':2, 'Oth': 31}
# sc = {'Con':285, 'Lab':180, 'Lib':110, 'Brx':0, 'Grn':10, 'SNP':415}
# ne = {'Con':390, 'Lab':446, 'Lib':79, 'Brx':56, 'Grn':21}
# nw = {'Con':381, 'Lab':450, 'Lib':91, 'Brx':46, 'Grn':22}
# yh = {'Con':424, 'Lab':408, 'Lib':88, 'Brx':49, 'Grn':21}
# cy = {'Con':354, 'Lab':419, 'Lib':60, 'Brx':59, 'Grn':15, 'PC':89}
# wm = {'Con':495, 'Lab':339, 'Lib':105, 'Brx':26, 'Grn':24}
# em = {'Con':504, 'Lab':350, 'Lib':81, 'Brx':31, 'Grn':21}
# ea = {'Con':533, 'Lab':269, 'Lib':141, 'Brx':21, 'Grn':24}
# sw = {'Con':492, 'Lab':247, 'Lib':197, 'Brx':22, 'Grn':28}
# ld = {'Con':328, 'Lab':472, 'Lib':139, 'Brx':29, 'Grn':25}
# se = {'Con':516, 'Lab':247, 'Lib':170, 'Brx':22, 'Grn':32}

print ("Electoral Calculus poll of polls, 11/2018 & Survation NI 11/2018")
ni = {'SF':270, 'DUP':310, 'APNI':120, 'UUP':150, 'SDLP':110, 'TUV':0, 'Grn':0, 'Oth': 40}
sc = {'Con':266, 'Lab':241, 'Lib':66, 'Brx':14, 'Grn':14, 'SNP':389}
ne = {'Con':285, 'Lab':523, 'Lib':66, 'Brx':78, 'Grn':32}
nw = {'Con':303, 'Lab':518, 'Lib':74, 'Brx':58, 'Grn':30}
yh = {'Con':346, 'Lab':459, 'Lib':70, 'Brx':65, 'Grn':32}
cy = {'Con':277, 'Lab':458, 'Lib':65, 'Brx':59, 'Grn':22, 'PC':104}
wm = {'Con':431, 'Lab':394, 'Lib':64, 'Brx':57, 'Grn':36}
em = {'Con':448, 'Lab':374, 'Lib':63, 'Brx':63, 'Grn':34}
ea = {'Con':487, 'Lab':296, 'Lib':99, 'Brx':64, 'Grn':38}
sw = {'Con':455, 'Lab':260, 'Lib':170, 'Brx':50, 'Grn':42}
ld = {'Con':272, 'Lab':514, 'Lib':108, 'Brx':52, 'Grn':37}
se = {'Con':487, 'Lab':255, 'Lib':125, 'Brx':62, 'Grn':50}

############################ SEAT TOTALS PER REGION #############################

regions =   [ni, sc, ne, nw, yh, cy, wm, em, ea, sw, ld, se]
seat_tots = [7, 21, 11, 28, 21, 12, 22, 18, 24, 22, 29, 35] # 250-seat, 2017-2019
#seat_tots = [7, 21, 10, 28, 21, 12, 22, 18, 24, 22, 30, 35] # 250-seat, 2019-2024
#seat_tots = [17,55, 28, 75, 54, 32, 58, 48, 61, 57, 75, 90] # 650-seat, Westminster since 2010
result = []

######################## CALCULATION AND PRESENTATION ###########################

for i in range(0, len(regions)):
    result.append(dhondt(nSeats=seat_tots[i],votes=regions[i],verbose=False))

con = int(result[1]['Con']+result[2]['Con']+result[3]['Con']+result[4]['Con']+result[5]['Con']+result[6]['Con']+result[7]['Con']+result[8]['Con']+result[9]['Con']+result[10]['Con']+result[11]['Con'])
lab = int(result[1]['Lab']+result[2]['Lab']+result[3]['Lab']+result[4]['Lab']+result[5]['Lab']+result[6]['Lab']+result[7]['Lab']+result[8]['Lab']+result[9]['Lab']+result[10]['Lab']+result[11]['Lab'])
lib = int(result[1]['Lib']+result[2]['Lib']+result[3]['Lib']+result[4]['Lib']+result[5]['Lib']+result[6]['Lib']+result[7]['Lib']+result[8]['Lib']+result[9]['Lib']+result[10]['Lib']+result[11]['Lib'])
brx = int(result[1]['Brx']+result[2]['Brx']+result[3]['Brx']+result[4]['Brx']+result[5]['Brx']+result[6]['Brx']+result[7]['Brx']+result[8]['Brx']+result[9]['Brx']+result[10]['Brx']+result[11]['Brx'])
grn = int(result[0]['Grn']+result[1]['Grn']+result[2]['Grn']+result[3]['Grn']+result[4]['Grn']+result[5]['Grn']+result[6]['Grn']+result[7]['Grn']+result[8]['Grn']+result[9]['Grn']+result[10]['Grn']+result[11]['Grn'])
snp = int(result[1]['SNP'])
pcy = int(result[5]['PC'])
uup = int(result[0]['UUP'])
sdl = int(result[0]['SDLP'])
sif = int(result[0]['SF'])
dup = int(result[0]['DUP'])
ali = int(result[0]['APNI'])

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
                    '\n\nTotal seats:', con+lab+lib+snp+pcy+uup+sdl+sif+dup+grn+ali+brx)

print('Done')
 # {{legend|#0E610D|Party 1: 3 seats}} {{legend|#4BF012|Party 2: 9 seats}} {{legend|#0BB01D|Party 3: 2 seats}} {{legend|#FEFE25|Party 4: 11 seats}} {{legend|#F52121|Party 5: 124 seats}} {{legend|#FEE16A|Party 6: 1 seat}} {{legend|#F7CC1F|Party 7: 20 seats}} {{legend|#2F14F8|Party 8: 67 seats}} {{legend|#EA7B62|DUP: 3 seats}} {{legend|#54EFE8|df: 10 seats}}
