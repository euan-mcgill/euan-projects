#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import csv
# import json
import requests
import re
# import spacy as sp

'''
A script to scrape transcription information from the iSignos corpus

Future: arrange operations in functions to be modular

Author: euan.mcgill@upf.edu | 2023/01/23
'''

metas = []
meten = []
videos = []
vidden = []
one_chan = ''
one_channel = []

for page_num in range(1, 4):
    my_page = f'http://isignos.uvigo.es/es/metadata?page={page_num}'
    en_page = f'http://isignos.uvigo.es/en/metadata?page={page_num}'
    page = requests.get(my_page)
    pagen = requests.get(en_page)
    # print(page.text)
    soup = BeautifulSoup(page.text, features="lxml")
    soupen = BeautifulSoup(pagen.text, features="lxml")
    metadata = soup.findAll('a', class_="btn btn-primary btn-sm")
    metadaten = soupen.findAll('a', class_="btn btn-primary btn-sm")
    for p,q in zip(metadata,metadaten):
        metas.append('http://isignos.uvigo.es'+p['href'])
        meten.append('http://isignos.uvigo.es'+q['href'])

for code,coden in zip(metas, meten):
    page = requests.get(code)
    pagen = requests.get(coden)
    videos.append(BeautifulSoup(page.text, features="lxml"))
    vidden.append(BeautifulSoup(pagen.text, features="lxml"))
    for v, w in zip(videos, vidden):
        title = v.find('source')['src'].split('/')[-1].split('.')[0]
        containers = list(v.findAll('div', class_='text')) #  <div class="text" data-start="705" data-end="9815"> marks the start of annotation blocks
        containen = list(w.findAll('div', class_='text'))
        sentence = [i+1 for i in range(len(containers))]
        espanol = [containers[i].decode_contents().split('<td colspan="100">')[-1].split('</td>')[0] for i in range(len(containers))]
        english = [containen[i].decode_contents().split('<td colspan="100">')[-1].split('</td>')[0] for i in range(len(containen))]
        start_time = [containers[i]['data-start'] for i in range(len(containers))]
        end_time = [containers[i]['data-end'] for i in range(len(containers))]
        derecha = [containers[i].decode_contents().split('<td><strong>D:</strong></td>')[-1].split('</tr>')[0] for i in range(len(containers))]
        izquierda = [containers[i].decode_contents().split('<td><strong>I:</strong></td>')[-1].split('</tr>')[0] for i in range(len(containers))]
        ### POSTPROCESSING ###
        esp_proc = [re.sub(',', '', espanol[i]) for i in range(len(espanol))]
        en_proc = [re.sub(',', '', english[i]) for i in range(len(english))]
        izquierda_proc_uno = [re.sub('<td></td>','<td>0</td>',izquierda[i]) for i in range(len(izquierda))]
        izquierda_proc_dos = [re.sub('</td>\\n<td>', ' ', izquierda_proc_uno[i]) for i in range(len(izquierda_proc_uno))]
        izquierda_proc_tres = [re.sub('(\\n<td>|</td>\\n)', '', izquierda_proc_dos[i]) for i in range(len(izquierda_proc_dos))]
        derecha_proc_uno = [re.sub('<td></td>','<td>0</td>',derecha[i]) for i in range(len(derecha))]
        derecha_proc_dos = [re.sub('</td>\\n<td>', ' ', derecha_proc_uno[i]) for i in range(len(derecha_proc_uno))]
        derecha_proc_tres = [re.sub('(\\n<td>|</td>\\n)', '', derecha_proc_dos[i]) for i in range(len(derecha_proc_dos))]
        ### Check dominant hand ###
        left_zeroes = [line.find('0')+1 for line in izquierda_proc_tres]
        right_zeroes = [line.find('0')+1 for line in derecha_proc_tres]
        ########################################### Write to CSV - two hands ###########################################
        with open(title+'_two_channel.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            header = ['ID', 'Start_time', 'End_time', 'English', 'Español', 'Dominant_Hand', 'Non_Dominant_Hand']
            writer.writerow(header)
            for sent, s, e, en, esp, i, d in zip(sentence, start_time, end_time, en_proc, esp_proc,
                                             izquierda_proc_tres, derecha_proc_tres):
                if sum(right_zeroes) >= sum(left_zeroes):
                    row = [sent, s, e, en, esp, i, d]
                else:
                    row = [sent, s, e, en, esp, d, i]
                writer.writerow(row)
        ################################################### Join LR hands #############################################
        one_channel = []
        if sum(right_zeroes) <= sum(left_zeroes):
            for d,i in zip(derecha_proc_tres, izquierda_proc_tres):
                c = ''
                for ld, li in zip(d.split(),i.split()):
                    c += '_'.join([ld,li])+' '
                one_channel.append(c)
        else:
            for d,i in zip(derecha_proc_tres, izquierda_proc_tres):
                c = ''
                for ld, li in zip(d.split(),i.split()):
                    c += '_'.join([li,ld])+' '
                one_channel.append(c)
        ######################################### POSTPROCESSING #######################################################
        one_channel_aa = [re.sub(r'(.*)(_)\1',r'\2\1',line) for line in one_channel] # remove duplicate glosses where sign is two-handed
        one_channel_ba = [re.sub('(_0|0_)', '', line) for line in one_channel_aa] # remove dummy label for no sign on one hand
        one_channel_ca = [re.sub(r'(_\b|\b_)', ' ', line) for line in one_channel_ba] # remove trailing underscores where dupe has been deleted
        one_channel_da = [re.sub('_', ' ', line) for line in one_channel_ca] # remove connecting underscores so that concurrent signs are now linearly Dominant-Non-Dominant
        one_channel_ea = [re.sub('  ', ' ', line) for line in one_channel_da] # remove double spaces
        # make further edits as req'd (any beyond the set [aa,ba,ca,da,ea] will differ from the contents of the FTP)
        with open(title+'_one_channel.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            header = ['ID', 'Start_time', 'End_time', 'English', 'Español', 'Gloss']
            writer.writerow(header)
            for sent, s, e, en, esp, g in zip(sentence, start_time, end_time, en_proc, esp_proc, one_channel_ea):
                row = [sent, s, e, en, esp, g]
                writer.writerow(row)
