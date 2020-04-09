#!/usr/bin/env python3

import reports
import os
import datetime

def process_data():
  path = "../supplier-data/descriptions/"
  files = os.listdir(path)
  paragraph = ''
  for file in files:
    #print(file)
    with open(path + file) as fh:
      lines = fh.readlines()
      paragraph = paragraph + lines[0].strip() + "<br/>" + lines[1].strip() + "<br/><br/>"

  return paragraph

def main():
  string = process_data()
  reports.generate_report('/tmp/processed.pdf',title, string)

if __name__ == "__main__":
  main()
