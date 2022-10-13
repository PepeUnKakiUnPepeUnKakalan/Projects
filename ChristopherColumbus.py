##imports##

import time
import os
from Funny import funnyarray
from Funnyset import TableGen

true = True

##commands##

def user(X):
  return input(X)

def ahh(x):
  time.sleep(x)

def plus(X, C):
  return X + C

def minus(X, C):
  return X - C

def multiply(X, C):
  return X * C

def divide(X, C):
  return X / C

def timburs(X):
  print(X)

def timbur(X):
  print(X)

def wkwk():
  exit("About to end his men whole career.")

def daddy(X):
  exit(X)

def funnyshit():
  timburs("A Louis Vuitton security guard  slaps a 13 year old boy in the face at a Fashion Week outside the Louvre.")

def emoji(X):
  X = str(X)
  if X == "0":
    return "🗿"
  if X == "1":
    return "😳"
  elif X == "2":
    return "🤤"
  elif X == "3":
    return "🥵"
  elif X == "4":
    return "🤡"
  elif X == "5":
    return "🖕🏿"
  elif X == "6":
    return "🖕🏻"
  elif X >= "7":
    return "😳"
    
def clear():
  os.system('clear')

def funny():
  return TableGen(funnyarray)