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



slprint (choises_list)
os.system (" python restart.py ")
sys.exit(0)
