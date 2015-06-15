"""
@author mbartoli

Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def primeFactors(n):
  c = 2
  while n > c**2: 
    while n % c == 0:
      n = n / c
    c += 1 
  return n
def main():
  n = 600851475143
  print primeFactors(n)

if __name__ == '__main__':
  main()
