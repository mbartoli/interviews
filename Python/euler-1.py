"""
@author Mike Bartoli

Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def getMultiples(upperBound, multiplesOf):
  multiples = set()
  for n in multiplesOf:
    for x in xrange(1,upperBound):
      if x % n == 0:
        multiples.add(x)
  return multiples

def main():
  upperBound = 1000
  multiplesOf = [3,5]
  multiples = getMultiples(upperBound, multiplesOf)
  print sum(multiples)


if __name__ == "__main__": 
  main()
