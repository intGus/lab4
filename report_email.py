#!/usr/bin/env python3

import reports
import os
from datetime import date
import emails

def process_data():
  path = "../supplier-data/descriptions/"
  files = os.listdir(path)
  paragraph = ''
  for file in files:
    #print(file)
    with open(path + file) as fh:
      lines = fh.readlines()
      paragraph = paragraph + "name: " + lines[0].strip() + "<br/>" + "weight: " + lines[1].strip() + "<br/><br/>"

  return paragraph

def main():
  string = process_data()
  title = "Processed Update on " + date.today().strftime("%B %d, %Y")
  #print(title) 
  reports.generate_report('/tmp/processed.pdf',title, string)

  #emailing
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate_email(sender,receiver,subject,body, '/tmp/processed.pdf')
  emails.send_email(message)

if __name__ == "__main__":
  main()
