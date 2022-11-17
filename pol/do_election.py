#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:04:42 2022

@author: e.mcgill
"""

from calcelec import CalcElec
import pandas as pd

six_election = ['electoral_calculus_data/1955.csv', 'electoral_calculus_data/1959.csv', 
                 'electoral_calculus_data/1964.csv', 'electoral_calculus_data/1966.csv', 
                 'electoral_calculus_data/1970.csv', 'electoral_calculus_data/1974f.csv', 
                 'electoral_calculus_data/1974o.csv', 'electoral_calculus_data/1979.csv', 
                 'electoral_calculus_data/1983.csv', 'electoral_calculus_data/1987.csv', 
                 'electoral_calculus_data/1992.csv', 'electoral_calculus_data/1997.csv', 
                 'electoral_calculus_data/2001.csv', 'electoral_calculus_data/2005.csv', ]

eight_election = [ 'electoral_calculus_data/2010.csv', 'electoral_calculus_data/2015.csv', 
                   'electoral_calculus_data/2017.csv', 'electoral_calculus_data/2019.csv', ]

#%%
six_frames = []

eight_frames = []

calculate = CalcElec(infile='electoral_calculus_data/2019.csv', sixparty=False).hamilton()
