      # import libs && files

import time
import os
import sys
import random
from data.lists import *


      # codes of colors

class colors:
    BLUE        = '\033[94m'
    GREEN       = '\033[32m'
    RED         = '\033[0;31m'
    DEFAULT     = '\033[0m'
    ORANGE      = '\033[33m'
    WHITE       = '\033[97m'
    BOLD        = '\033[1m'
    BR_COLOUR   = '\033[1;37;40m'
    BLACK       = '\033[30m'
    YELLOW      = '\003[33m'
    CYAN        = '\003[36m'

 # slow print code

def slprint(s):
  for c in s + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(.005)


def restart():
  print (" ")
  chs = (input(" choose your text numbre (no) : "))
  if chs == "exit":
   slprint(colors.GREEN+"""
[+] thanks for using
"""+colors.WHITE)
   sys.exit(0)

  elif chs == "2":
   os.system (" python ifs2.py")
   sys.exit(0)
  elif chs == "3":
   os.system (" python ifs3.py")
   sys.exit(0)
  elif chs == "4":
   os.system ("python ifs4.py")
   sys.exit(0)
  elif chs == "help":
   slprint (choises_list)
   restart()
  else:
   slprint (colors.RED+"""
invailed choise
               ( you must choose availabe numbre )

"""+colors.WHITE)
   restart()
restart()
