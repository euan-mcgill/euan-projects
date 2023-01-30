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


print("Electoral Calculus poll of polls, 01/2023 & LucidTalk (BT), 11/2022")
ni = {'SF':320, 'DUP':270, 'APNI':150, 'UUP':90, 'SDLP':70, 'TUV':50, 'Grn':20, 'Oth': 30}
sc = {'Con':153, 'Lab':280, 'OTH':60, 'Brx':10, 'Grn':24, 'SNP':456}
ne = {'Con':231, 'Lab':567, 'OTH':48, 'Brx':75, 'Grn':56}
nw = {'Con':224, 'Lab':583, 'OTH':52, 'Brx':67, 'Grn':54}
yh = {'Con':267, 'Lab':529, 'OTH':57, 'Brx':73, 'Grn':51}
cy = {'Con':221, 'Lab':507, 'OTH':33, 'Brx':49, 'Grn':23, 'PC':149}
wm = {'Con':315, 'Lab':482, 'OTH':66, 'Brx':72, 'Grn':50}
em = {'Con':340, 'Lab':458, 'OTH':55, 'Brx':71, 'Grn':50}
ea = {'Con':348, 'Lab':403, 'OTH':110, 'Brx':72, 'Grn':50}
sw = {'Con':315, 'Lab':379, 'OTH':158, 'Brx':70, 'Grn':52}
ld = {'Con':172, 'Lab':605, 'OTH':91, 'Brx':60, 'Grn':59}
se = {'Con':330, 'Lab':381, 'OTH':146, 'Brx':70, 'Grn':57}

# print ("Electoral Calculus poll of polls, 12/2019 & Exit poll NI 12/2019")
# ni = {'SF':228, 'DUP':306, 'APNI':168, 'UUP':117, 'SDLP':149, 'TUV':0, 'Grn':2, 'Oth': 31}
# sc = {'Con':285, 'Lab':180, 'OTH':110, 'Brx':0, 'Grn':10, 'SNP':415}
# ne = {'Con':390, 'Lab':446, 'OTH':79, 'Brx':56, 'Grn':21}
# nw = {'Con':381, 'Lab':450, 'OTH':91, 'Brx':46, 'Grn':22}
# yh = {'Con':424, 'Lab':408, 'OTH':88, 'Brx':49, 'Grn':21}
# cy = {'Con':354, 'Lab':419, 'OTH':60, 'Brx':59, 'Grn':15, 'PC':89}
# wm = {'Con':495, 'Lab':339, 'OTH':105, 'Brx':26, 'Grn':24}
# em = {'Con':504, 'Lab':350, 'OTH':81, 'Brx':31, 'Grn':21}
# ea = {'Con':533, 'Lab':269, 'OTH':141, 'Brx':21, 'Grn':24}
# sw = {'Con':492, 'Lab':247, 'OTH':197, 'Brx':22, 'Grn':28}
# ld = {'Con':328, 'Lab':472, 'OTH':139, 'Brx':29, 'Grn':25}
# se = {'Con':516, 'Lab':247, 'OTH':170, 'Brx':22, 'Grn':32}

# print ("Electoral Calculus poll of polls, 11/2018 & Survation NI 11/2018")
# ni = {'SF':270, 'DUP':310, 'APNI':120, 'UUP':150, 'SDLP':110, 'TUV':0, 'Grn':0, 'Oth': 40}
# sc = {'Con':266, 'Lab':241, 'OTH':66, 'Brx':14, 'Grn':14, 'SNP':389}
# ne = {'Con':285, 'Lab':523, 'OTH':66, 'Brx':78, 'Grn':32}
# nw = {'Con':303, 'Lab':518, 'OTH':74, 'Brx':58, 'Grn':30}
# yh = {'Con':346, 'Lab':459, 'OTH':70, 'Brx':65, 'Grn':32}
# cy = {'Con':277, 'Lab':458, 'OTH':65, 'Brx':59, 'Grn':22, 'PC':104}
# wm = {'Con':431, 'Lab':394, 'OTH':64, 'Brx':57, 'Grn':36}
# em = {'Con':448, 'Lab':374, 'OTH':63, 'Brx':63, 'Grn':34}
# ea = {'Con':487, 'Lab':296, 'OTH':99, 'Brx':64, 'Grn':38}
# sw = {'Con':455, 'Lab':260, 'OTH':170, 'Brx':50, 'Grn':42}
# ld = {'Con':272, 'Lab':514, 'OTH':108, 'Brx':52, 'Grn':37}
# se = {'Con':487, 'Lab':255, 'OTH':125, 'Brx':62, 'Grn':50}

############################ SEAT TOTALS PER REGION #############################

regions =   [ni, sc, ne, nw, yh, cy, wm, em, ea, sw, ld, se]
#seat_tots = [7, 21, 11, 28, 21, 12, 22, 18, 24, 22, 29, 35] # 250-seat, 2017-2019
#seat_tots = [7, 21, 10, 28, 21, 12, 22, 18, 24, 22, 30, 35] # 250-seat, 2019-2024
seat_tots = [17,55, 28, 75, 54, 32, 58, 48, 61, 57, 75, 90] # 650-seat, Westminster since 2010
result = []

######################## CALCULATION AND PRESENTATION ###########################

for i in range(0, len(regions)):
    result.append(dhondt(nSeats=seat_tots[i],votes=regions[i],verbose=False))

con = int(result[1]['Con']+result[2]['Con']+result[3]['Con']+result[4]['Con']+result[5]['Con']+result[6]['Con']+result[7]['Con']+result[8]['Con']+result[9]['Con']+result[10]['Con']+result[11]['Con'])
lab = int(result[1]['Lab']+result[2]['Lab']+result[3]['Lab']+result[4]['Lab']+result[5]['Lab']+result[6]['Lab']+result[7]['Lab']+result[8]['Lab']+result[9]['Lab']+result[10]['Lab']+result[11]['Lab'])
lib = int(result[1]['OTH']+result[2]['OTH']+result[3]['OTH']+result[4]['OTH']+result[5]['OTH']+result[6]['OTH']+result[7]['OTH']+result[8]['OTH']+result[9]['OTH']+result[10]['OTH']+result[11]['OTH'])
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


################################### USA ###################################################

seat_state_prz = {}
seat_state_hse = {'AL': 7, 'AK': 1,
              'AZ': 9, 'AR': 4, 
              'CA': 52, 'CO': 8, 
              'CN': 5, 'DE': 1, 
              'FL': 28, 'GA': 14, 
              'HI': 2, 'ID': 2, 
              'IL': 17, 'IN': 9,
              'IA': 4, 'KS': 4, 
              'KY': 6, 'LA': 6, 
              'ME': 2, 'MD': 8, 
              'MA': 9, 'MI': 13, 
              'MN': 8, 'MS': 4,
              'MO': 8, 'MT': 2, 
              'NE': 3, 'NV': 4, 
              'NH': 2, 'NJ': 12, 
              'NM': 3, 'NY': 26, 
              'NC': 14, 'ND': 1, 
              'OH': 15, 'OK': 5, 
              'OR': 6, 'PA': 17, 
              'RI': 2, 'SC': 7, 
              'SD': 1, 'TN': 9, 
              'TX': 38, 'UT': 4, 
              'VT': 1, 'VA': 11, 
              'WA': 10, 'WV': 2, 
              'WI': 8, 'WY': 1}
seats = list(seat_state_hse.values())

# House of Representatives Election, 2022
al = {'GOP': 7013, 'DEM': 2371, 'OTH': 10000-7013-2371}
ak = {'GOP': 2550+2330, 'DEM': 4880, 'OTH': 10000-2550-2330-4880}
az = {'GOP': 5614, 'DEM': 4305, 'OTH': 10000-5614-4305}
ar = {'GOP': 6803, 'DEM': 2923, 'OTH': 10000-6803-2923}
ca = {'GOP': 3622, 'DEM': 6328, 'OTH': 10000-3622-6328}
co = {'GOP': 4251, 'DEM': 5523, 'OTH': 10000-4251-5523}
cn = {'GOP': 4173, 'DEM': 5720, 'OTH': 10000-4173-5720}
de = {'GOP': 4297, 'DEM': 5547, 'OTH': 10000-4297-5547}
fl = {'GOP': 5825, 'DEM': 3963, 'OTH': 10000-5825-3963}
ga = {'GOP': 5231, 'DEM': 4769, 'OTH': 10000-5231-4769}
hi = {'GOP': 3093, 'DEM': 6779, 'OTH': 10000-6779-3093}
ido = {'GOP': 6774, 'DEM': 3101, 'OTH': 10000-6774-3101}
il = {'GOP': 4368, 'DEM': 5609, 'OTH': 10000-4368-5609}
ina = {'GOP': 5969, 'DEM': 3857, 'OTH': 10000-5969-3857}
ina = {'GOP': 5969, 'DEM': 3857, 'OTH': 10000-5969-3857}
ia = {'GOP': 5627, 'DEM': 4373, 'OTH': 10000-5627-4373}
ks = {'GOP': 5685, 'DEM': 4246, 'OTH': 10000-5685-4246}
ky = {'GOP': 6514, 'DEM': 3355, 'OTH': 10000-6514-3355}
la = {'GOP': 6828, 'DEM': 2815, 'OTH': 10000-6828-2815}
me = {'GOP': 4192, 'DEM': 5799, 'OTH': 10000-4192-5799}
md = {'GOP': 3460, 'DEM': 6471, 'OTH': 10000-3460-6471}
ma = {'GOP': 2964, 'DEM': 6967, 'OTH': 10000-2924-6967}
mi = {'GOP': 4759, 'DEM': 4983, 'OTH': 10000-4759-4983}
mn = {'GOP': 4811, 'DEM': 5010, 'OTH': 10000-4811-5010}
ms = {'GOP': 6418, 'DEM': 3532, 'OTH': 10000-6418-3532}
mo = {'GOP': 5940, 'DEM': 3859, 'OTH': 10000-5940-3859}
mt = {'GOP': 5286, 'DEM': 3424, 'OTH': 10000-5286-3424}
ne = {'GOP': 6271, 'DEM': 3532, 'OTH': 10000-6271-3532}
nv = {'GOP': 5106, 'DEM': 4762, 'OTH': 10000-5106-4762}
nh = {'GOP': 4499, 'DEM': 5490, 'OTH': 10000-4499-5490}
nj = {'GOP': 4446, 'DEM': 5427, 'OTH': 10000-4446-5427}
nm = {'GOP': 4493, 'DEM': 5506, 'OTH': 10000-4493-5506}
ny = {'GOP': 4388, 'DEM': 5559, 'OTH': 10000-4388-5559}
nc = {'GOP': 5203, 'DEM': 4773, 'OTH': 10000-5203-4773}
nd = {'GOP': 6220, 'DEM': 0, 'OTH': 10000-6220}
oh = {'GOP': 5643, 'DEM': 4357, 'OTH': 10000-5643-4357}
ok = {'GOP': 6636, 'DEM': 3114, 'OTH': 10000-6636-3114}
orn = {'GOP': 4468, 'DEM': 5310, 'OTH': 10000-4468-5310}
pa = {'GOP': 5245, 'DEM': 4730, 'OTH': 10000-5245-4730}
ri = {'GOP': 4204, 'DEM': 5643, 'OTH': 10000-4204-5643}
sc = {'GOP': 6712, 'DEM': 3288, 'OTH': 10000-6712-3288}
sd = {'GOP': 7740, 'DEM': 0, 'OTH': 10000-7740}
tn = {'GOP': 6428, 'DEM': 3402, 'OTH': 10000-6428-3402}
tx = {'GOP': 5878, 'DEM': 3873, 'OTH': 10000-5878-3873}
ut = {'GOP': 6308, 'DEM': 3220, 'OTH': 10000-6308-3220}
vt = {'GOP': 2690, 'DEM': 6050, 'OTH': 10000-2690-6050}
va = {'GOP': 5148, 'DEM': 4809, 'OTH': 10000-5148-4809}
wa = {'GOP': 4170, 'DEM': 5788, 'OTH': 10000-4170-5788}
wv = {'GOP': 6611, 'DEM': 3172, 'OTH': 10000-6611-3172}
wi = {'GOP': 5543, 'DEM': 4002, 'OTH': 10000-5543-4002}
wy = {'GOP': 6820, 'DEM': 2440, 'OTH': 10000-6820-2440}

# Presidential Election, 2020

usa = [al, ak, az, ar, ca, co, cn, de, fl, ga, hi, ido, il, ina,
           ia, ks, ky, la, me, md, ma, mi, mn, ms, mo, mt,  ne,  nv,
           nh, nj, nm, ny, nc, nd, oh, ok,orn, pa, ri, sc,  sd,  tn,
           tx, ut, vt, va, wa, wv, wi, wy]

results = []

for i in range(0, len(usa)):
    results.append(dhondt(seats[i], usa[i]))
