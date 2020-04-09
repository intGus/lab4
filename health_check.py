#!/usr/bin/env python3
import shutil
import psutil
import requests
import socket
import os
import emails

def check_localhost():
  localhost = socket.gethostbyname('localhost')
  return localhost == '127.0.0.1'

def check_connectivity():
  request = requests.get("http://www.google.com")
  #print(request.status_code)
  return request.status_code == 200

def check_disk_usage(disk):
  """Verifies that there's enough free space on disk"""
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20
def check_cpu_usage():
  """Verifies that there's enough unused CPU"""
  usage = psutil.cpu_percent(1)
  return usage < 80
def check_memory_usage():
  """Verifies that there's enough free memory"""
  memusage = psutil.virtual_memory()
  return memusage.available/1000000 > 500

# If there's not enough disk, or not enough CPU, print an error
subject = None
if not check_disk_usage('/'):
  subject = 'Error - Available disk space is less than 20%'
elif not check_cpu_usage():
  subject = 'Error - CPU usage is over 80%'
elif not check_memory_usage():
  subject = 'Error - Available memory is less than 500MB'
elif not check_localhost():
  subject = 'Error - localhost cannot be resolved to 127.0.0.1'
elif not check_connectivity():
  subject = 'No internet? how you send an email with no internet'

if subject == None:
  print('everything ok')
else:
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subj = subject
  body = "Please check your system and resolve the issue as soon as possible."

  message = emails.generate_error_report(sender, receiver, subj, body)
  emails.send_email(message)

  print(subject)
