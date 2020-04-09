#!/usr/bin/env python3

from PIL import Image
import os

path = "../supplier-data/images/"

files = os.listdir(path)

for file in files:
  print(file)
  try:
    file_name, ext = file.split('.') #get the file name for renaming
    im = Image.open(path+file)
    new_im = im.resize((600,400)).convert("RGBA") #processing the alpha channel
    background = Image.new('RGBA', new_im.size, (255,255,255))
    final = Image.alpha_composite(background, new_im).convert("RGB")
    final.save(path + file_name + '.jpeg', 'JPEG', quality=100)
  except:
    continue

