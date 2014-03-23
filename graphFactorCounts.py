#!/usr/bin/python

import sys
import matplotlib.pyplot as plt

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

def primesCount(n):
  pc = 0 
  d = 2
  while d*d <= n:
    while (n % d) == 0:
      pc += 1
      n /= d
    d += 1
  if n > 1:
    pc += 1
  return pc

def main():

 if len(sys.argv) != 2: 
   print "Not enough arguments."
   sys.exit(0)

 maxx = int(sys.argv[1]) + 1
 if maxx <= 2:
   print "Choose value >=2"
   sys.exit(0)

 X = range(2, int(sys.argv[1])) 
 Y = []
 for N in X:
   Y.append(primesCount(N))

 plt.ylabel('Number of prime factors in factorization')
 plt.plot(X, Y)
 plt.show()

if __name__ == '__main__':
  main()
