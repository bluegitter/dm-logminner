#!/usr/bin/python
# Filename: cat.py
import sys
import re

def readfile(filename, seconds):
  '''Print a file to the standard output.'''
  f = file(filename)
  line1 = '';
  line = '';
  pattern = re.compile(r'\(ms\)\r\n')
  while True:
    line += f.readline()
    if len(line) == 0:
      break
    end = line[-1]
    end1 = line[-2]
    match = pattern.search(line) 
    if match:
      line1 = line;
      line = "";
      paraList = line1.split()
      if len(paraList) > 0:
        time = paraList[-1]
        time1 = time[:-4]
	if int(time1) >  seconds:
          print line1 # notice comma
      line1 = '';
  f.close()

# Script starts from here
if len(sys.argv) < 2:
  print 'Usage: logminer.py logfile seconds'
  sys.exit()

if sys.argv[1].startswith('--'):
  option = sys.argv[1][2:]
  # fetch sys.argv[1] but without the first two characters
  if option == 'version':
    print 'Version 1.2'
  elif option == 'help':
    print '''\
Usage: logminer.py logfile seconds
Options include:
  --version : Prints the version number
  --help : Display this help'''
  else:
    print 'Unknown option.'
    sys.exit()
else:
    #for filename in sys.argv[1:]:
    filename = sys.argv[1]
    if len(sys.argv) < 3:
      seconds = 1000;
    seconds = int(sys.argv[2])
    readfile(filename,seconds)

