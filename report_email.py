#!/usr/bin/env python3

import reports
import os
import datetime

def process_data():
  path = "../supplier-data/descriptions/"
  files = os.listdir(path)

  for file in files:
  #print(file)
    item_dict = {}
    with open(path + file) as fh:
      lines = fh.readlines()
      paragraph = paragraph + lines[0].strip() + "<br/>" lines[1].strip() + "<br/> <br/>"

  return paragraph

add the rest
