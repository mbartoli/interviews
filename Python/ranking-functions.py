'''
Ranking Functions

@author mbartoli 
'''

import math
from collections import Counter


def main():
	iterations = [10,100,500,700]
	
	for n in iterations:
		functions = Counter()
		
		functions['n!'] = math.factorial(n)
		functions['47'] = 47
		functions['e^n'] = math.pow(math.e,n)
		functions['n log4 n'] = math.log(n,4) 	
		functions['n^1/3 + log5 n'] = math.pow(n, 0.3333333333) + math.log(n,5)
		functions['n'] = n
		functions['(3/2)^n'] = math.pow(1.5,n)
		functions['n2^n'] = n*math.pow(2,n)
		functions['(log2 n)^(log2 n)'] = math.pow(math.log(n,2),math.log(n,2))
		functions['sqrt n'] = math.pow(n,0.5)
		functions['2^n'] = math.pow(2,n)
		functions['n^(log2 log2 n)'] = math.pow(n,math.log(math.log(n,2),2))
		functions['log2 n!'] = math.log(math.factorial(n),2)
		functions['n^2'] = math.pow(n,2)
		functions['(n+1)!'] = math.factorial(n+1)
		functions['4^(log2 n)'] = math.pow(4,math.log(n,2))
		print "\n\n\n iterations: "+str(n)		
		print functions
	
	
if __name__ == '__main__':
	main()

