"""
@author mbartoli

Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import math

def isPalindrome(n):
  n = str(n)
  size = len(n)
  if size % 2 == 0:
    return n[:size/2] == (n[size/2:][::-1])
  elif size == 1:
    return True
  else:
    return (n[:int(size/2.0-.5)] == ((n[int(size/2.0+.5)])[::-1]))

def main():
  palindromes = set()
  for x in range(1,1000):
    for y in range(1,1000):
      mult = x*y
      if isPalindrome(mult):
        palindromes.add(mult)
  print max(palindromes)

if __name__ == '__main__':
  main()
