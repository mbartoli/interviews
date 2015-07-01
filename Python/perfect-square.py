"""
@author mbartoli

Checks if a number is a perfect square

Ex.
python perfect-square.py 4
4 is a perfect square

python perfect-square.py 4 5 9
4 is a perfect square
9 is a perfect square
"""

import sys
import math

def isPerfectSquare(n):
  if (math.sqrt(n) % 1 != 0):
    return False
  else:
    return True       
    

def main():
  for x in range(1,len(sys.argv)):
    if isPerfectSquare(float(sys.argv[x])):
      print str(sys.argv[x]) + " is a perfect sqare" 

if __name__ == '__main__':
  main()
