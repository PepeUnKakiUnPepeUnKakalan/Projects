import random

def TableGen(table):
  Total  = 0
  table.insert(0, "Python is gay, so they count 0")
  for crap in table:
    Total = Total + 1

  sec = random.randint(1,Total-1)

  ## Word Gen

  Num = 0
  for shit in table:
    if Num == sec :
      if shit == "Corporal Kenji will appreciate this":
        return "My Cumdolences"
      else:
        return shit
    Num = Num + 1
  