      # import libs && files

import time
import os
import sys
import random


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


a=11
b=21
c=31
d=41
e=51
f=12
g=22
h=32
i=42
j=52
k=13
l=23
m=33
n=43
o=53
p=14
q=24
r=34
s=44
t=54
u=15
v=25
w=35
x=45
y=55
z=16

def ifs2():
  print ("")
  inpa = (input(" enter 1f letter : "))
  leta = inpa
  if inpa == "a":
   inpa = a
  if inpa == "b":
   inpa = b
  if inpa == "c":
   inpa = c
  if inpa == "d":
   inpa = d
  if inpa == "e":
   inpa = e
  if inpa == "f":
   inpa = f
  if inpa == "g":
   inpa = g
  if inpa == "h":
   inpa = h
  if inpa == "i":
   inpa = i
  if inpa == "j":
   inpa = j
  if inpa == "k":
   inpa = k
  if inpa == "l":
   inpa = l
  if inpa == "m":
   inpa = m
  if inpa == "n":
   inpa = n
  if inpa == "o":
   inpa = o
  if inpa == "p":
   inpa = p
  if inpa == "q":
   inpa = q
  if inpa == "r":
   inpa = r
  if inpa == "s":
   inpa = s
  if inpa == "t":
   inpa = t
  if inpa == "u":
   inpa = u
  if inpa == "v":
   inpa = v
  if inpa == "w":
   inpa = w
  if inpa == "x":
   inpa = x
  if inpa == "y":
   inpa = y
  if inpa == "z":
   inpa = z
                              # second letter
  print (" ")
  inpb = (input(" enter 2s letter : "))
  letb = inpb
  if inpb == "a":
   inpb = a
  if inpb == "b":
   inpb = b
  if inpb == "c":
   inpb = c
  if inpb == "d":
   inpb = d
  if inpb == "e":
   inpb = e
  if inpb == "f":
   inpb = f
  if inpb == "g":
   inpb = g
  if inpb == "h":
   inpb = h
  if inpb == "i":
   inpb = i
  if inpb == "j":
   inpb = j
  if inpb == "k":
   inpb = k
  if inpb == "l":
   inpb = l
  if inpb == "m":
   inpb = m
  if inpb == "n":
   inpb = n
  if inpb == "o":
   inpb = o
  if inpb == "p":
   inpb = p
  if inpb == "q":
   inpb = q
  if inpb == "r":
   inpb = r
  if inpb == "s":
   inpb = s
  if inpb == "t":
   inpb = t
  if inpb == "u":
   inpb = u
  if inpb == "v":
   inpb = v
  if inpb == "w":
   inpb = w
  if inpb == "x":
   inpb = x
  if inpb == "y":
   inpb = y
  elif inpb == "z":
   inpb = z
  print(" ")
  qenc = (input(" encrypt "+"( "+leta+letb+" )"+" to nlc ? (y,n) :  "))
  if qenc == "y":
   print (" ")
   print (inpa,inpb)
   os.system (" python restart.py ")
   sys.exit(0)
  else:
   ifs2()
ifs2()
