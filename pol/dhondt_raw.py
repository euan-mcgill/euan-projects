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

# print("Blank draft - DO NOT EDIT")
# ni = {'SF': 0, 'DUP': 0, 'APNI': 0, 'UUP': 0, 'SDLP': 0, 'TUV': 0, 'Grn': 0, 'Oth': 0}
# sc = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'SNP': 0}
# ne = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# nw = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# yh = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# cy = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0, 'PC': 0}
# wm = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# em = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# ea = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# sw = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# ld = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}
# se = {'Con': 0, 'Lab': 0, 'LIB': 0, 'Brx': 0, 'Grn': 0}

print("Electoral Calculus poll of polls 09/2023 and Belfast Telegraph 08/2023")
ni = {'SF': 310, 'DUP': 260, 'APNI': 150, 'UUP': 100, 'SDLP': 60, 'TUV': 50, 'Grn': 20, 'Oth': 40}
sc = {'Con': 163, 'Lab': 336, 'LIB': 63, 'Brx': 17, 'Grn': 27, 'SNP': 367}
ne = {'Con': 231, 'Lab': 550, 'LIB': 69, 'Brx': 94, 'Grn': 53}
nw = {'Con': 226, 'Lab': 570, 'LIB': 72, 'Brx': 78, 'Grn': 52}
yh = {'Con': 256, 'Lab': 516, 'LIB': 74, 'Brx': 92, 'Grn': 56}
cy = {'Con': 230, 'Lab': 486, 'LIB': 44, 'Brx': 67, 'Grn': 29, 'PC': 142}
wm = {'Con': 328, 'Lab': 453, 'LIB': 92, 'Brx': 72, 'Grn': 53}
em = {'Con': 313, 'Lab': 460, 'LIB': 76, 'Brx': 89, 'Grn': 54}
ea = {'Con': 357, 'Lab': 369, 'LIB': 138, 'Brx': 75, 'Grn': 59}
sw = {'Con': 327, 'Lab': 335, 'LIB': 202, 'Brx': 73, 'Grn': 60}
ld = {'Con': 209, 'Lab': 564, 'LIB': 90, 'Brx': 56, 'Grn': 79}
se = {'Con': 342, 'Lab': 339, 'LIB': 176, 'Brx': 72, 'Grn': 68}

# print("Electoral Calculus poll of polls 08/2023, NI local elections 1st pref")
# ni = {'SF': 309, 'DUP': 233, 'APNI': 133, 'UUP': 109, 'SDLP': 87, 'TUV': 39, 'Grn': 17, 'Oth': 68}
# sc = {'Con': 183, 'Lab': 333, 'LIB': 83, 'Brx': 0, 'Grn': 7, 'SNP': 363}
# ne = {'Con': 217, 'Lab': 565, 'LIB': 67, 'Brx': 81, 'Grn': 47}
# nw = {'Con': 214, 'Lab': 585, 'LIB': 70, 'Brx': 67, 'Grn': 46}
# yh = {'Con': 243, 'Lab': 531, 'LIB': 73, 'Brx': 80, 'Grn': 49}
# cy = {'Con': 220, 'Lab': 502, 'LIB': 43, 'Brx': 58, 'Grn': 26, 'PC': 142}
# wm = {'Con': 318, 'Lab': 468, 'LIB': 91, 'Brx': 62, 'Grn': 47}
# em = {'Con': 301, 'Lab': 475, 'LIB': 75, 'Brx': 78, 'Grn': 47}
# ea = {'Con': 348, 'Lab': 384, 'LIB': 137, 'Brx': 66, 'Grn': 52}
# sw = {'Con': 315, 'Lab': 347, 'LIB': 200, 'Brx': 64, 'Grn': 53}
# ld = {'Con': 203, 'Lab': 579, 'LIB': 88, 'Brx': 50, 'Grn': 70}
# se = {'Con': 335, 'Lab': 355, 'LIB': 174, 'Brx': 64, 'Grn': 60}

# print("Electoral Calculus poll of polls 07/2023, NI local elections 1st pref")
# ni = {'SF': 309, 'DUP': 233, 'APNI': 133, 'UUP': 109, 'SDLP': 87, 'TUV': 39, 'Grn': 17, 'Oth': 68}
# sc = {'Con': 185, 'Lab': 315, 'LIB': 78, 'Brx': 0, 'Grn': 13, 'SNP': 364}
# ne = {'Con': 213, 'Lab': 561, 'LIB': 72, 'Brx': 81, 'Grn': 51}
# nw = {'Con': 217, 'Lab': 575, 'LIB': 78, 'Brx': 63, 'Grn': 50}
# yh = {'Con': 243, 'Lab': 526, 'LIB': 84, 'Brx': 77, 'Grn': 51}
# cy = {'Con': 206, 'Lab': 489, 'LIB': 76, 'Brx': 69, 'Grn': 48, 'PC': 92}
# wm = {'Con': 296, 'Lab': 486, 'LIB': 79, 'Brx': 72, 'Grn': 54}
# em = {'Con': 301, 'Lab': 471, 'LIB': 76, 'Brx': 75, 'Grn': 54}
# ea = {'Con': 329, 'Lab': 400, 'LIB': 124, 'Brx': 71, 'Grn': 63}
# sw = {'Con': 305, 'Lab': 375, 'LIB': 166, 'Brx': 65, 'Grn': 66}
# ld = {'Con': 206, 'Lab': 555, 'LIB': 124, 'Brx': 42, 'Grn': 64}
# se = {'Con': 320, 'Lab': 373, 'LIB': 154, 'Brx': 63, 'Grn': 76}

# print("Electoral Calculus poll of polls 06/2023, NI local elections 1st pref 05/2023")
# ni = {'SF': 309, 'DUP': 233, 'APNI': 133, 'UUP': 109, 'SDLP': 87, 'TUV': 39, 'Grn': 17, 'Oth': 68}
# sc = {'Con': 174, 'Lab': 307, 'LIB': 80, 'Brx': 14, 'Grn': 27, 'SNP': 378}
# ne = {'Con': 240, 'Lab': 545, 'LIB': 70, 'Brx': 67, 'Grn': 51}
# nw = {'Con': 242, 'Lab': 558, 'LIB': 76, 'Brx': 52, 'Grn': 51}
# yh = {'Con': 270, 'Lab': 509, 'LIB': 82, 'Brx': 64, 'Grn': 52}
# cy = {'Con': 232, 'Lab': 472, 'LIB': 73, 'Brx': 57, 'Grn': 49, 'PC': 92}
# wm = {'Con': 322, 'Lab': 469, 'LIB': 76, 'Brx': 59, 'Grn': 55}
# em = {'Con': 327, 'Lab': 454, 'LIB': 74, 'Brx': 62, 'Grn': 55}
# ea = {'Con': 355, 'Lab': 383, 'LIB': 119, 'Brx': 59, 'Grn': 64}
# sw = {'Con': 330, 'Lab': 359, 'LIB': 163, 'Brx': 53, 'Grn': 67}
# ld = {'Con': 229, 'Lab': 539, 'LIB': 122, 'Brx': 33, 'Grn': 64}
# se = {'Con': 346, 'Lab': 357, 'LIB': 152, 'Brx': 51, 'Grn': 77}

# print("Electoral Calculus poll of polls 05/2023, LucidTalk (BT) 04/2023")
# ni = {'SF': 290, 'DUP': 250, 'APNI': 130, 'UUP': 110, 'SDLP': 70, 'TUV': 70, 'Grn': 20, 'Oth': 50}
# sc = {'Con': 177, 'Lab': 303, 'LIB': 83, 'Brx': 20, 'Grn': 27, 'SNP': 377}
# ne = {'Con': 246, 'Lab': 543, 'LIB': 59, 'Brx': 80, 'Grn': 44}
# nw = {'Con': 251, 'Lab': 556, 'LIB': 64, 'Brx': 63, 'Grn': 43}
# yh = {'Con': 278, 'Lab': 507, 'LIB': 69, 'Brx': 76, 'Grn': 45}
# cy = {'Con': 239, 'Lab': 470, 'LIB': 62, 'Brx': 68, 'Grn': 42, 'PC': 92}
# wm = {'Con': 330, 'Lab': 467, 'LIB': 64, 'Brx': 71, 'Grn': 48}
# em = {'Con': 335, 'Lab': 453, 'LIB': 62, 'Brx': 75, 'Grn': 47}
# ea = {'Con': 367, 'Lab': 381, 'LIB': 104, 'Brx': 71, 'Grn': 56}
# sw = {'Con': 343, 'Lab': 357, 'LIB': 147, 'Brx': 64, 'Grn': 58}
# ld = {'Con': 244, 'Lab': 537, 'LIB': 106, 'Brx': 42, 'Grn': 56}
# se = {'Con': 359, 'Lab': 355, 'LIB': 136, 'Brx': 63, 'Grn': 67}

# print("Electoral Calculus poll of polls 04/2023, UoLiverpool 03/2023")
# ni = {'SF': 306, 'DUP': 239, 'APNI': 154, 'UUP': 113, 'SDLP': 67, 'TUV': 48, 'Grn': 32, 'Oth': 41}
# sc = {'Con': 187, 'Lab': 300, 'LIB': 60, 'Brx': 7, 'Grn': 33, 'SNP': 393}
# ne = {'Con': 222, 'Lab': 567, 'LIB': 62, 'Brx': 76, 'Grn': 43}
# nw = {'Con': 227, 'Lab': 580, 'LIB': 67, 'Brx': 59, 'Grn': 42}
# yh = {'Con': 254, 'Lab': 531, 'LIB': 73, 'Brx': 72, 'Grn': 44}
# cy = {'Con': 215, 'Lab': 494, 'LIB': 65, 'Brx': 65, 'Grn': 41, 'PC': 92}
# wm = {'Con': 306, 'Lab': 491, 'LIB': 67, 'Brx': 67, 'Grn': 46}
# em = {'Con': 311, 'Lab': 477, 'LIB': 65, 'Brx': 71, 'Grn': 46}
# ea = {'Con': 342, 'Lab': 405, 'LIB': 108, 'Brx': 67, 'Grn': 55}
# sw = {'Con': 318, 'Lab': 381, 'LIB': 152, 'Brx': 60, 'Grn': 57}
# ld = {'Con': 219, 'Lab': 561, 'LIB': 110, 'Brx': 38, 'Grn': 55}
# se = {'Con': 335, 'Lab': 379, 'LIB': 140, 'Brx': 59, 'Grn': 66}

# print("Electoral Calculus poll of polls, 03/2023 & LucidTalk (BT), 01/2023")
# ni = {'SF':320, 'DUP':270, 'APNI':150, 'UUP':90, 'SDLP':70, 'TUV':50, 'Grn':20, 'Oth': 30}
# sc = {'Con': 177, 'Lab': 303, 'LIB': 60, 'Brx': 7, 'Grn': 13, 'SNP': 410}
# ne = {'Con': 209, 'Lab': 576, 'LIB': 59, 'Brx': 81, 'Grn': 47}
# nw = {'Con': 214, 'Lab': 590, 'LIB': 64, 'Brx': 64, 'Grn': 46}
# yh = {'Con': 241, 'Lab': 241, 'LIB': 69, 'Brx': 77, 'Grn': 47}
# cy = {'Con': 202, 'Lab': 504, 'LIB': 62, 'Brx': 69, 'Grn': 45, 'PC': 92}
# wm = {'Con': 293, 'Lab': 500, 'LIB': 64, 'Brx': 72, 'Grn': 51}
# em = {'Con': 298, 'Lab': 486, 'LIB': 62, 'Brx': 75, 'Grn': 50}
# ea = {'Con': 329, 'Lab': 415, 'LIB': 104, 'Brx': 72, 'Grn': 59}
# sw = {'Con': 304, 'Lab': 390, 'LIB': 148, 'Brx': 66, 'Grn': 62}
# ld = {'Con': 206, 'Lab': 570, 'LIB': 107, 'Brx': 43, 'Grn': 60}
# se = {'Con': 320, 'Lab': 388, 'LIB': 137, 'Brx': 64, 'Grn': 72}

# print("Electoral Calculus poll of polls, 01/2023 & LucidTalk (BT), 11/2022")
# ni = {'SF':320, 'DUP':270, 'APNI':150, 'UUP':90, 'SDLP':70, 'TUV':50, 'Grn':20, 'Oth': 30}
# sc = {'Con':153, 'Lab':280, 'LIB':60, 'Brx':10, 'Grn':24, 'SNP':456}
# ne = {'Con':231, 'Lab':567, 'LIB':48, 'Brx':75, 'Grn':56}
# nw = {'Con':224, 'Lab':583, 'LIB':52, 'Brx':67, 'Grn':54}
# yh = {'Con':267, 'Lab':529, 'LIB':57, 'Brx':73, 'Grn':51}
# cy = {'Con':221, 'Lab':507, 'LIB':33, 'Brx':49, 'Grn':23, 'PC':149}
# wm = {'Con':315, 'Lab':482, 'LIB':66, 'Brx':72, 'Grn':50}
# em = {'Con':340, 'Lab':458, 'LIB':55, 'Brx':71, 'Grn':50}
# ea = {'Con':348, 'Lab':403, 'LIB':110, 'Brx':72, 'Grn':50}
# sw = {'Con':315, 'Lab':379, 'LIB':158, 'Brx':70, 'Grn':52}
# ld = {'Con':172, 'Lab':605, 'LIB':91, 'Brx':60, 'Grn':59}
# se = {'Con':330, 'Lab':381, 'LIB':146, 'Brx':70, 'Grn':57}

# print("Electoral Calculus poll of polls, 07/2022 & UoL, 07/2022")
# ni = {'SF': 309, 'DUP': 201, 'APNI': 153, 'UUP': 96, 'SDLP': 100, 'TUV': 47, 'Grn': 28, 'Oth': 66}
# sc = {'Con': 187, 'Lab': 233, 'LIB': 79, 'Brx': 0, 'Grn': 20, 'SNP': 450}
# ne = {'Con': 301, 'Lab': 495, 'LIB': 71, 'Brx': 19, 'Grn': 52}
# nw = {'Con': 288, 'Lab': 516, 'LIB': 76, 'Brx': 14, 'Grn': 53}
# yh = {'Con': 330, 'Lab': 460, 'LIB': 78, 'Brx': 18, 'Grn': 53}
# cy = {'Con': 237, 'Lab': 446, 'LIB': 57, 'Brx': 16, 'Grn': 21, 'PC': 181}
# wm = {'Con': 405, 'Lab': 378, 'LIB': 102, 'Brx': 14, 'Grn': 52}
# em = {'Con': 398, 'Lab': 404, 'LIB': 73, 'Brx': 15, 'Grn': 51}
# ea = {'Con': 426, 'Lab': 321, 'LIB': 140, 'Brx': 13, 'Grn': 50}
# sw = {'Con': 389, 'Lab': 310, 'LIB': 180, 'Brx': 11, 'Grn': 54}
# ld = {'Con': 240, 'Lab': 481, 'LIB': 155, 'Brx': 10, 'Grn': 70}
# se = {'Con': 400, 'Lab': 309, 'LIB': 174, 'Brx': 11, 'Grn': 57}

# print("Electoral Calculus poll of polls, 09/2021 & LucidTalk (BT) 08/2021")
# ni = {'SF': 250, 'DUP': 130, 'APNI': 130, 'UUP': 160, 'SDLP': 130, 'TUV': 140, 'Grn': 20, 'Oth': 40}
# sc = {'Con': 223, 'Lab': 183, 'LIB': 63, 'Brx': 7, 'Grn': 7, 'SNP': 483}
# ne = {'Con': 319, 'Lab': 445, 'LIB': 49, 'Brx': 85, 'Grn': 66}
# nw = {'Con': 311, 'Lab': 493, 'LIB': 56, 'Brx': 43, 'Grn': 68}
# yh = {'Con': 367, 'Lab': 409, 'LIB': 57, 'Brx': 63, 'Grn': 66}
# cy = {'Con': 297, 'Lab': 428, 'LIB': 42, 'Brx': 58, 'Grn': 51, 'PC': 99}
# wm = {'Con': 471, 'Lab': 359, 'LIB': 56, 'Brx': 18, 'Grn': 73}
# em = {'Con': 484, 'Lab': 337, 'LIB': 56, 'Brx': 19, 'Grn': 69}
# ea = {'Con': 508, 'Lab': 268, 'LIB': 95, 'Brx': 9, 'Grn': 81}
# sw = {'Con': 464, 'Lab': 261, 'LIB': 129, 'Brx': 9, 'Grn': 96}
# ld = {'Con': 256, 'Lab': 506, 'LIB': 106, 'Brx': 19, 'Grn': 84}
# se = {'Con': 476, 'Lab': 248, 'LIB': 130, 'Brx': 9, 'Grn': 98}

# print("Electoral Calculus poll of polls, 10/2020 & LucidTalk (BT) 10/2020")
# ni = {'SF': 240, 'DUP': 230, 'APNI': 160, 'UUP': 120, 'SDLP': 130, 'TUV': 60, 'Grn': 30, 'Oth': 30}
# sc = {'Con': 200, 'Lab': 184, 'LIB': 55, 'Brx': 11, 'Grn': 11, 'SNP': 526}
# ne = {'Con': 334, 'Lab': 475, 'LIB': 41, 'Brx': 81, 'Grn': 37}
# nw = {'Con': 326, 'Lab': 524, 'LIB': 47, 'Brx': 39, 'Grn': 39}
# yh = {'Con': 382, 'Lab': 441, 'LIB': 48, 'Brx': 59, 'Grn': 37}
# cy = {'Con': 312, 'Lab': 456, 'LIB': 36, 'Brx': 55, 'Grn': 23, 'PC': 99}
# wm = {'Con': 486, 'Lab': 390, 'LIB': 47, 'Brx': 14, 'Grn': 44}
# em = {'Con': 499, 'Lab': 369, 'LIB': 47, 'Brx': 15, 'Grn': 40}
# ea = {'Con': 523, 'Lab': 311, 'LIB': 80, 'Brx': 4, 'Grn': 48}
# sw = {'Con': 479, 'Lab': 312, 'LIB': 109, 'Brx': 4, 'Grn': 60}
# ld = {'Con': 271, 'Lab': 551, 'LIB': 89, 'Brx': 14, 'Grn': 50}
# se = {'Con': 491, 'Lab': 300, 'LIB': 109, 'Brx': 3, 'Grn': 61}

# print ("Electoral Calculus poll of polls, 12/2019 & Exit poll NI 12/2019")
# ni = {'SF':228, 'DUP':306, 'APNI':168, 'UUP':117, 'SDLP':149, 'TUV':0, 'Grn':2, 'Oth': 31}
# sc = {'Con':285, 'Lab':180, 'LIB':110, 'Brx':0, 'Grn':10, 'SNP':415}
# ne = {'Con':390, 'Lab':446, 'LIB':79, 'Brx':56, 'Grn':21}
# nw = {'Con':381, 'Lab':450, 'LIB':91, 'Brx':46, 'Grn':22}
# yh = {'Con':424, 'Lab':408, 'LIB':88, 'Brx':49, 'Grn':21}
# cy = {'Con':354, 'Lab':419, 'LIB':60, 'Brx':59, 'Grn':15, 'PC':89}
# wm = {'Con':495, 'Lab':339, 'LIB':105, 'Brx':26, 'Grn':24}
# em = {'Con':504, 'Lab':350, 'LIB':81, 'Brx':31, 'Grn':21}
# ea = {'Con':533, 'Lab':269, 'LIB':141, 'Brx':21, 'Grn':24}
# sw = {'Con':492, 'Lab':247, 'LIB':197, 'Brx':22, 'Grn':28}
# ld = {'Con':328, 'Lab':472, 'LIB':139, 'Brx':29, 'Grn':25}
# se = {'Con':516, 'Lab':247, 'LIB':170, 'Brx':22, 'Grn':32}

# print("Electoral Calculus poll of polls, 11/2019 & 2019 EU election in NI first preferences")
# ni = {'SF': 222, 'DUP': 218, 'APNI': 185, 'UUP': 93, 'SDLP': 137, 'TUV': 108, 'Grn': 22, 'Oth': 15}
# sc = {'Con': 210, 'Lab': 190, 'LIB': 130, 'Brx': 50, 'Grn': 20, 'SNP': 390}
# ne = {'Con': 288, 'Lab': 345, 'LIB': 144, 'Brx': 159, 'Grn': 40}
# nw = {'Con': 298, 'Lab': 353, 'LIB': 152, 'Brx': 136, 'Grn': 39}
# yh = {'Con': 319, 'Lab': 320, 'LIB': 146, 'Brx': 153, 'Grn': 41}
# cy = {'Con': 280, 'Lab': 279, 'LIB': 157, 'Brx': 110, 'Grn': 25, 'PC': 135}
# wm = {'Con': 392, 'Lab': 251, 'LIB': 163, 'Brx': 128, 'Grn': 40}
# em = {'Con': 374, 'Lab': 263, 'LIB': 141, 'Brx': 163, 'Grn': 38}
# ea = {'Con': 420, 'Lab': 182, 'LIB': 201, 'Brx': 129, 'Grn': 43}
# sw = {'Con': 396, 'Lab': 154, 'LIB': 262, 'Brx': 115, 'Grn': 48}
# ld = {'Con': 289, 'Lab': 339, 'LIB': 216, 'Brx': 75, 'Grn': 57}
# se = {'Con': 418, 'Lab': 159, 'LIB': 229, 'Brx': 116, 'Grn': 53}

# print("Electoral Calculus poll of polls, 7/2019 & 2019 EU election in NI first preferences")
# ni = {'SF': 222, 'DUP': 218, 'APNI': 185, 'UUP': 93, 'SDLP': 137, 'TUV': 108, 'Grn': 22, 'Oth': 15}
# sc = {'Con': 180, 'Lab': 170, 'LIB': 130, 'Brx': 90, 'Grn': 20, 'SNP': 380}
# ne = {'Con': 169, 'Lab': 327, 'LIB': 144, 'Brx': 241, 'Grn': 79}
# nw = {'Con': 183, 'Lab': 338, 'LIB': 154, 'Brx': 214, 'Grn': 75}
# yh = {'Con': 201, 'Lab': 306, 'LIB': 146, 'Brx': 234, 'Grn': 77}
# cy = {'Con': 147, 'Lab': 258, 'LIB': 132, 'Brx': 270, 'Grn': 61, 'PC': 111}
# wm = {'Con': 251, 'Lab': 263, 'LIB': 163, 'Brx': 229, 'Grn': 63}
# em = {'Con': 246, 'Lab': 246, 'LIB': 132, 'Brx': 265, 'Grn': 74}
# ea = {'Con': 275, 'Lab': 184, 'LIB': 198, 'Brx': 245, 'Grn': 66}
# sw = {'Con': 253, 'Lab': 153, 'LIB': 261, 'Brx': 233, 'Grn': 68}
# ld = {'Con': 193, 'Lab': 358, 'LIB': 233, 'Brx': 114, 'Grn': 75}
# se = {'Con': 281, 'Lab': 159, 'LIB': 227, 'Brx': 226, 'Grn': 75}

# print("Electoral Calculus poll of polls, 02/2019 & Northern Slant 02/2019")
# ni = {'SF': 324, 'DUP': 336, 'APNI': 80, 'UUP': 103, 'SDLP': 86, 'TUV': 23, 'Grn': 19, 'Oth': 34}
# sc = {'Con': 266, 'Lab': 241, 'LIB': 66, 'Brx': 14, 'Grn': 14, 'SNP': 389}
# ne = {'Con': 285, 'Lab': 523, 'LIB': 66, 'Brx': 78, 'Grn': 32}
# nw = {'Con': 303, 'Lab': 518, 'LIB': 74, 'Brx': 58, 'Grn': 30}
# yh = {'Con': 346, 'Lab': 459, 'LIB': 70, 'Brx': 65, 'Grn': 32}
# cy = {'Con': 277, 'Lab': 458, 'LIB': 65, 'Brx': 59, 'Grn': 22, 'PC': 104}
# wm = {'Con': 431, 'Lab': 394, 'LIB': 64, 'Brx': 57, 'Grn': 36}
# em = {'Con': 448, 'Lab': 374, 'LIB': 63, 'Brx': 63, 'Grn': 34}
# ea = {'Con': 487, 'Lab': 296, 'LIB': 99, 'Brx': 64, 'Grn': 38}
# sw = {'Con': 455, 'Lab': 260, 'LIB': 170, 'Brx': 50, 'Grn': 42}
# ld = {'Con': 272, 'Lab': 514, 'LIB': 108, 'Brx': 52, 'Grn': 37}
# se = {'Con': 487, 'Lab': 255, 'LIB': 125, 'Brx': 62, 'Grn': 50}

# print ("Electoral Calculus poll of polls, 09/2018 & GUE/NGL 12/2017")
# ni = {'SF':328, 'DUP':337, 'APNI':79, 'UUP':89, 'SDLP':86, 'TUV':11, 'Grn':22, 'Oth': 38}
# sc = {'Con':250, 'Lab':270, 'LIB':62, 'Brx':10, 'Grn':25, 'SNP':374}
# ne = {'Con':316, 'Lab':539, 'LIB':56, 'Brx':57, 'Grn':21}
# nw = {'Con':334, 'Lab':534, 'LIB':64, 'Brx':37, 'Grn':19}
# yh = {'Con':377, 'Lab':475, 'LIB':60, 'Brx':44, 'Grn':21}
# cy = {'Con':308, 'Lab':474, 'LIB':55, 'Brx':38, 'Grn':11, 'PC':104}
# wm = {'Con':462, 'Lab':410, 'LIB':54, 'Brx':36, 'Grn':25}
# em = {'Con':479, 'Lab':390, 'LIB':53, 'Brx':42, 'Grn':23}
# ea = {'Con':518, 'Lab':312, 'LIB':89, 'Brx':43, 'Grn':27}
# sw = {'Con':486, 'Lab':276, 'LIB':160, 'Brx':29, 'Grn':31}
# ld = {'Con':303, 'Lab':530, 'LIB':98, 'Brx':31, 'Grn':26}
# se = {'Con':518, 'Lab':271, 'LIB':115, 'Brx':41, 'Grn':39}

# print ("Electoral Calculus poll of polls, 04/2018 & GUE/NGL 12/2017")
# ni = {'SF':328, 'DUP':337, 'APNI':79, 'UUP':89, 'SDLP':86, 'TUV':11, 'Grn':22, 'Oth': 38}
# sc = {'Con':240, 'Lab':270, 'LIB':63, 'Brx':13, 'Grn':25, 'SNP':380}
# ne = {'Con':314, 'Lab':551, 'LIB':46, 'Brx':61, 'Grn':21}
# nw = {'Con':332, 'Lab':546, 'LIB':54, 'Brx':41, 'Grn':19}
# yh = {'Con':375, 'Lab':487, 'LIB':50, 'Brx':48, 'Grn':21}
# cy = {'Con':306, 'Lab':486, 'LIB':45, 'Brx':42, 'Grn':11, 'PC':104}
# wm = {'Con':460, 'Lab':422, 'LIB':44, 'Brx':40, 'Grn':25}
# em = {'Con':477, 'Lab':402, 'LIB':43, 'Brx':46, 'Grn':23}
# ea = {'Con':516, 'Lab':324, 'LIB':79, 'Brx':47, 'Grn':27}
# sw = {'Con':484, 'Lab':288, 'LIB':150, 'Brx':33, 'Grn':31}
# ld = {'Con':301, 'Lab':542, 'LIB':88, 'Brx':35, 'Grn':26}
# se = {'Con':516, 'Lab':283, 'LIB':105, 'Brx':45, 'Grn':39}

# print ("Electoral Calculus poll of polls, 02/2018 & GUE/NGL 12/2017")
# ni = {'SF':328, 'DUP':337, 'APNI':79, 'UUP':89, 'SDLP':86, 'TUV':11, 'Grn':22, 'Oth': 38}
# sc = {'Con':235, 'Lab':275, 'LIB':65, 'Brx':20, 'Grn':20, 'SNP':375}
# ne = {'Con':315, 'Lab':555, 'LIB':40, 'Brx':59, 'Grn':23}
# nw = {'Con':333, 'Lab':550, 'LIB':48, 'Brx':39, 'Grn':21}
# yh = {'Con':376, 'Lab':491, 'LIB':44, 'Brx':46, 'Grn':23}
# cy = {'Con':307, 'Lab':490, 'LIB':39, 'Brx':40, 'Grn':13, 'PC':104}
# wm = {'Con':461, 'Lab':426, 'LIB':38, 'Brx':38, 'Grn':27}
# em = {'Con':478, 'Lab':406, 'LIB':37, 'Brx':44, 'Grn':25}
# ea = {'Con':517, 'Lab':328, 'LIB':73, 'Brx':45, 'Grn':29}
# sw = {'Con':485, 'Lab':292, 'LIB':144, 'Brx':31, 'Grn':33}
# ld = {'Con':302, 'Lab':546, 'LIB':82, 'Brx':33, 'Grn':28}
# se = {'Con':517, 'Lab':287, 'LIB':99, 'Brx':43, 'Grn':41}

############################ SEAT TOTALS PER REGION #############################

regions =   [ni, sc, ne, nw, yh, cy, wm, em, ea, sw, ld, se]
# seat_tots = [7, 21, 11, 28, 21, 12, 22, 18, 24, 22, 29, 35] # 250-seat, 2017-2019
# seat_tots = [7, 21, 10, 28, 21, 12, 22, 18, 24, 22, 30, 35] # 250-seat, 2019-2024
seat_tots = [17,55, 28, 75, 54, 32, 58, 48, 61, 57, 75, 90] # 650-seat, Westminster since 2010
#seat_tots = [7, 20, 10, 27, 20, 12, 21, 18, 23, 21, 28, 33] # 240 seat Lords reform
result = []

######################## CALCULATION AND PRESENTATION ###########################

for i in range(0, len(regions)):
    result.append(dhondt(nSeats=seat_tots[i],votes=regions[i],verbose=False))

con = int(result[1]['Con']+result[2]['Con']+result[3]['Con']+result[4]['Con']+result[5]['Con']+result[6]['Con']+result[7]['Con']+result[8]['Con']+result[9]['Con']+result[10]['Con']+result[11]['Con'])
lab = int(result[1]['Lab']+result[2]['Lab']+result[3]['Lab']+result[4]['Lab']+result[5]['Lab']+result[6]['Lab']+result[7]['Lab']+result[8]['Lab']+result[9]['Lab']+result[10]['Lab']+result[11]['Lab'])
lib = int(result[1]['LIB']+result[2]['LIB']+result[3]['LIB']+result[4]['LIB']+result[5]['LIB']+result[6]['LIB']+result[7]['LIB']+result[8]['LIB']+result[9]['LIB']+result[10]['LIB']+result[11]['LIB'])
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

print(result)

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
