#!/usr/bin/env python3
import requests
import os

# upload images using Python Requests module

path = "../supplier-data/images/"
files = os.listdir(path)

url = "http://localhost/upload/"

for file in files:
  if file.endswith('.jpeg'):
    with open(path + file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
    if r.status_code == 201: print('image {} successfully uploaded'.format(file))
    else: print('Error while uploading {}, returned error {}'.format(file, r.status_code))

