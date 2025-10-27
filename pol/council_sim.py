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


#test = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0}
#cambs = {'Con': 72199, 'Lab': 36437, 'LIB': 53338, 'Brx': 343, 'Grn': 17455, 'Nat': 0, 'Min': 2283, 'Ind': 5150, 'Oth': 343+55+48}

#print("Consolidated results from https://www.andrewteale.me.uk/leap/results/2021/373/")
#print(dhondt(nSeats=8,votes=cambs,verbose=False))

con_total = 0
lab_total = 0
lib_total = 0
brx_total = 0
grn_total = 0
nat_total = 0
min_total = 0
ind_total = 0
oth_total = 0

# seats = {'Cambridge': 0, 'East Cambs': 0, 'Fenland': 0, 'Hunts': 0, 'South Cambs': 0}
# votes = [{'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0}]
# parl = 0

# Cambridgeshire
# seats = {'Cambridge': 12, 'East Cambs': 8, 'Fenland': 9, 'Hunts': 17, 'South Cambs': 15}
# votes = [{'Con': 3959, 'Lab': 10117, 'LIB': 7904, 'Brx': 3242, 'Grn': 7890, 'Nat': 0, 'Min': 0, 'Ind': 123, 'Oth': 0},
#          {'Con': 5762, 'Lab': 1625, 'LIB': 8589, 'Brx': 5896, 'Grn': 1677, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 9815, 'Lab': 2500, 'LIB': 2282, 'Brx': 11088, 'Grn': 1277, 'Nat': 0, 'Min': 0, 'Ind': 756, 'Oth': 0},
#          {'Con': 12826, 'Lab': 4628, 'LIB': 10205, 'Brx': 12951, 'Grn': 3091, 'Nat': 0, 'Min': 50, 'Ind': 2781, 'Oth': 0},
#          {'Con': 11721, 'Lab': 5606, 'LIB': 21939, 'Brx': 9520, 'Grn': 5380, 'Nat': 0, 'Min': 0, 'Ind': 547, 'Oth': 0}]
# parl = 8

# Devon
# seats = {'East Devon': 11, 'Exeter': 9, 'Mid Devon': 6, 'North Devon': 8, 'South Hams': 7,\
#          'Teignbridge': 10, 'Torridge': 5, 'West Devon': 4}
# votes = [{'Con': 10758, 'Lab': 1890, 'LIB': 12663, 'Brx': 11876, 'Grn': 3452, 'Nat': 0, 'Min': 0, 'Ind': 6857, 'Oth': 57},
#          {'Con': 5071, 'Lab': 8858, 'LIB': 4217, 'Brx': 7779, 'Grn': 6492, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 38},
#          {'Con': 4763, 'Lab': 1457, 'LIB': 8368, 'Brx': 6650, 'Grn': 1224, 'Nat': 0, 'Min': 0, 'Ind': 391, 'Oth': 52+13},
#          {'Con': 6680, 'Lab': 900, 'LIB': 9878, 'Brx': 7456, 'Grn': 2618, 'Nat': 0, 'Min': 0, 'Ind': 47, 'Oth': 0},
#          {'Con': 6332, 'Lab': 1108, 'LIB': 9621, 'Brx': 6162, 'Grn': 3346, 'Nat': 0, 'Min': 0, 'Ind': 197, 'Oth': 89+20},
#          {'Con': 7157, 'Lab': 2294, 'LIB': 11816, 'Brx': 11190, 'Grn': 2885, 'Nat': 0, 'Min': 0, 'Ind': 2895, 'Oth': 92+73+60},
#          {'Con': 4778, 'Lab': 679, 'LIB': 6244, 'Brx': 6240, 'Grn': 1721, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 4553, 'Lab': 1030, 'LIB': 3832, 'Brx': 4979, 'Grn': 2095, 'Nat': 0, 'Min': 0, 'Ind': 767, 'Oth': 0}]
# parl = 12

# Gloucestershire
# seats = {'Cheltenham': 10, 'Cotswold': 8, 'Forest of Dean': 8, 'Gloucester': 10, 'Stroud': 11, 'Tewkesbury': 8}
# votes = [{'Con': 6672, 'Lab': 1169, 'LIB': 14831, 'Brx': 6686, 'Grn': 3451, 'Nat': 0, 'Min': 0, 'Ind': 110, 'Oth': 76+22},
#          {'Con': 8509, 'Lab': 781, 'LIB': 10903, 'Brx': 5928, 'Grn': 1913, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 4474, 'Lab': 2421, 'LIB': 2342, 'Brx': 8312, 'Grn': 5582, 'Nat': 0, 'Min': 0, 'Ind': 2079, 'Oth': 0},
#          {'Con': 6880, 'Lab': 3313, 'LIB': 7721, 'Brx': 8263, 'Grn': 1551, 'Nat': 0, 'Min': 0, 'Ind': 1325, 'Oth': 67+34+30},
#          {'Con': 6570, 'Lab': 6878, 'LIB': 3727, 'Brx': 8785, 'Grn': 12152, 'Nat': 0, 'Min': 0, 'Ind': 927, 'Oth': 58+25},
#          {'Con': 4710, 'Lab': 870, 'LIB': 10041, 'Brx': 7930, 'Grn': 2461, 'Nat': 0, 'Min': 785, 'Ind': 638, 'Oth': 0}]
# parl = 7

# Kent
# seats = {'Ashford': 7, 'Canterbury': 8, 'Dartford': 6, 'Dover': 7, 'Folkestone and Hythe': 6,
#          'Gravesham': 5, 'Maidstone': 9, 'Sevenoaks': 6, 'Swale': 7, 'Thanet': 7, 'Tonbridge and Malling': 7,
#          'Tunbridge Wells': 6}
# votes = [{'Con': 7622, 'Lab': 4161, 'LIB': 2154, 'Brx': 14754, 'Grn': 5231, 'Nat': 0, 'Min': 1303, 'Ind': 0, 'Oth': 75},
#          {'Con': 7587, 'Lab': 8174, 'LIB': 6788, 'Brx': 12657, 'Grn': 5599, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 27},
#          {'Con': 7370, 'Lab': 4424, 'LIB': 157, 'Brx': 9997, 'Grn': 1819, 'Nat': 0, 'Min': 641, 'Ind': 0, 'Oth': 31},
#          {'Con': 8835, 'Lab': 9285, 'LIB': 3686, 'Brx': 19697, 'Grn': 4340, 'Nat': 0, 'Min': 0, 'Ind': 466, 'Oth': 33},
#          {'Con': 5306, 'Lab': 3870, 'LIB': 3586, 'Brx': 14293, 'Grn': 5545, 'Nat': 0, 'Min': 0, 'Ind': 136, 'Oth': 85+50},
#          {'Con': 8193, 'Lab': 8219, 'LIB': 683, 'Brx': 16141, 'Grn': 3401, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 12030, 'Lab': 3416, 'LIB': 9552, 'Brx': 18029, 'Grn': 8753, 'Nat': 0, 'Min': 0, 'Ind': 70, 'Oth': 70+64+57},
#          {'Con': 9875, 'Lab': 1721, 'LIB': 6246, 'Brx': 9889, 'Grn': 2815, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 5737, 'Lab': 4069, 'LIB': 4160, 'Brx': 19210, 'Grn': 3621, 'Nat': 0, 'Min': 5083, 'Ind': 1557, 'Oth': 0},
#          {'Con': 9375, 'Lab': 8802, 'LIB': 2447, 'Brx': 19932, 'Grn': 8824, 'Nat': 0, 'Min': 0, 'Ind': 772, 'Oth': 0},
#          {'Con': 12493, 'Lab': 2649, 'LIB': 6047, 'Brx': 11678, 'Grn': 11936, 'Nat': 0, 'Min': 0, 'Ind': 8, 'Oth': 0},
#          {'Con': 6713, 'Lab': 2049, 'LIB': 9779, 'Brx': 6868, 'Grn': 2126, 'Nat': 0, 'Min': 1968, 'Ind': 599, 'Oth': 0}]
# parl = 0

# Lancashire
seats = {'Burnley': 6, 'Chorley': 8, 'Fylde': 6, 'Hyndburn': 6, 'Lancaster': 10, 'Pendle': 6,\
         'Preston': 9, 'Ribble Valley': 4, 'Rossendale': 5, 'South Ribble': 8, 'West Lancs': 8, \
         'Wyre': 8}
votes = [{'Con': 3769, 'Lab': 2496, 'LIB': 1564, 'Brx': 8319, 'Grn': 1842, 'Nat': 0, 'Min': 0, 'Ind': 3896, 'Oth': 39},
         {'Con': 5290, 'Lab': 9639, 'LIB': 988, 'Brx': 10863, 'Grn': 2658, 'Nat': 0, 'Min': 0, 'Ind': 23, 'Oth': 271},
         {'Con': 7923, 'Lab': 2390, 'LIB': 1208, 'Brx': 7160, 'Grn': 1054, 'Nat': 0, 'Min': 0, 'Ind': 3358, 'Oth': 71},
         {'Con': 6159, 'Lab': 7064, 'LIB': 0, 'Brx': 11628, 'Grn': 3031, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
         {'Con': 4692, 'Lab': 6505, 'LIB': 3874, 'Brx': 10984, 'Grn': 8699, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
         {'Con': 7753, 'Lab': 2193, 'LIB': 6571, 'Brx': 8943, 'Grn': 1158, 'Nat': 0, 'Min': 0, 'Ind': 4904, 'Oth': 18},
         {'Con': 3931, 'Lab': 6064, 'LIB': 7498, 'Brx': 8749, 'Grn': 1377, 'Nat': 0, 'Min': 0, 'Ind': 3799, 'Oth': 48},
         {'Con': 4145, 'Lab': 2849, 'LIB': 1700, 'Brx': 7183, 'Grn': 1163, 'Nat': 0, 'Min': 0, 'Ind': 1915, 'Oth': 0},
         {'Con': 3745, 'Lab': 4929, 'LIB': 196, 'Brx': 8237, 'Grn': 1814, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
         {'Con': 7170, 'Lab': 6624, 'LIB': 3891, 'Brx': 11527, 'Grn': 1304, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 51},
         {'Con': 5618, 'Lab': 6239, 'LIB': 1307, 'Brx': 10018, 'Grn': 1854, 'Nat': 0, 'Min': 4066, 'Ind': 0, 'Oth': 0},
         {'Con': 9553, 'Lab': 5422, 'LIB': 929, 'Brx': 14096, 'Grn': 1675, 'Nat': 0, 'Min': 0, 'Ind': 129, 'Oth': 0}]
parl = 0

# Staffordshire
# seats = {'Cannock Chase': 7, 'East Staffs': 9, 'Lichfield': 8, 'Newcastle-under-Lyme': 9, 'South Staffs': 8, 'Stafford': 9,\
#          'Staffs Moorlands': 7, 'Tamworth': 5}
# votes = [{'Con': 4473, 'Lab': 3339, 'LIB': 196, 'Brx': 13012, 'Grn': 2725, 'Nat': 0, 'Min': 0, 'Ind': 492, 'Oth': 70+30},
#          {'Con': 8628, 'Lab': 5254, 'LIB': 825, 'Brx': 10152, 'Grn': 2281, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 8684, 'Lab': 5436, 'LIB': 3306, 'Brx': 10391, 'Grn': 686, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 0},
#          {'Con': 7316, 'Lab': 6419, 'LIB': 1978, 'Brx': 13053, 'Grn': 195, 'Nat': 0, 'Min': 0, 'Ind': 133, 'Oth': 99},
#          {'Con': 9733, 'Lab': 2467, 'LIB': 2357, 'Brx': 11805, 'Grn': 1250, 'Nat': 0, 'Min': 0, 'Ind': 551, 'Oth': 31},
#          {'Con': 9498, 'Lab': 5409, 'LIB': 2439, 'Brx': 11298, 'Grn': 3256, 'Nat': 0, 'Min': 2597, 'Ind': 303, 'Oth': 39},
#          {'Con': 8727, 'Lab': 3749, 'LIB': 809, 'Brx': 11810, 'Grn': 1590, 'Nat': 0, 'Min': 0, 'Ind': 2649, 'Oth': 0},
#          {'Con': 4415, 'Lab': 3427, 'LIB': 0, 'Brx': 9607, 'Grn': 625, 'Nat': 0, 'Min': 0, 'Ind': 0, 'Oth': 255+56}]
# parl = 12


for (area, num_seats), vote_counts in zip(seats.items(), votes):
    result = dhondt(nSeats=num_seats, votes=vote_counts, verbose=False)
    print(f"\n{area} ({num_seats} seats): {result}")
    con_total += result.get('Con', 0)
    lab_total += result.get('Lab', 0)
    lib_total += result.get('LIB', 0)
    brx_total += result.get('Brx', 0)
    grn_total += result.get('Grn', 0)
    min_total += result.get('Min', 0)
    ind_total += result.get('Ind', 0)

print(f"\n\nConservative: {con_total}")
print(f"Labour: {lab_total}")
print(f"Liberal Democrat: {lib_total}")
print(f"Reform: {brx_total}")
print(f"Green Party: {grn_total}")
print(f"Minority parties: {min_total}")
print(f"Independents: {ind_total}\n\n")
