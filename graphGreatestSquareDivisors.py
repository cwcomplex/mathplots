#!/usr/bin/python

import sys
import matplotlib.pyplot as plt

from math import sqrt
import operator
from operator import mul
from collections import defaultdict


def partition(seq, key):
  d = defaultdict(list)
  for x in seq:
    d[key(x)].append(x)
  return d

gend = {}

def primes(n):
  primfac = []
  d = 2
  while d*d <= n:
    while (n % d) == 0:
      primfac.append(d)  # supposing you want multiple factors repeated
      n /= d
    d += 1
  if n > 1:
    primfac.append(n)
  return primfac

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def getGreatestSquareDivisor(N):
  factors = primes(N)

  part = defaultdict(list)
  for f in factors:
    part[f].append(f)
  maxsquares = {}
  maxsquares[1] = 1
  gsd = 1
  pk = part.keys() 
  for k in pk:
    pcnt = len(part[k])
    if pcnt == 1:
      continue
    maxsq = 1
    for j in part[k]:
      maxsq *= j
    while pcnt > 2:
      if is_square(maxsq) == False:
        maxsq /= k
        pcnt -= 1
        continue
      break
    maxsquares[k] = maxsq
    gsd *= maxsq
  return gsd 

def main():
  N_MIN=2

  if len(sys.argv) != 2:
    print "Not enough arguments."
    sys.exit(0)
  N_MAX = int(sys.argv[1]) + 1
  if N_MAX <= 2:
    print "Choose value >=2"
    sys.exit(0)


  X = range(N_MIN, N_MAX+1)
  Y = []
  for N in X:
    gsd = getGreatestSquareDivisor(N)
    Y.append(gsd)

  plt.ylabel('Greatest Square Divisor')
  plt.plot(X,Y)
  plt.show() 

          
if __name__ == "__main__":
  main()
