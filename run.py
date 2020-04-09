#! /usr/bin/env python3

import os
import requests

path = "../supplier-data/descriptions/"

files = os.listdir(path)

for file in files:
  #print(file)
  item_dict = {}
  with open(path + file) as fh:
    lines = fh.readlines()
    item_dict['name'] = lines[0].strip()
    weight = lines[1].split()
    item_dict['weight'] = int(weight[0])
    item_dict['description'] = lines[2].strip()
    file_name, ext = file.split('.')
    item_dict['image_name'] = file_name + '.jpeg'

    r = requests.post('http://35.193.30.105/fruits/', json = item_dict)
    if r.status_code == 201: print('item {} successfully uploaded'.format(file))
    else: print('Error while uploading {}, returned error {}'.format(file, r.status_code))

    #print(item_dict) 
