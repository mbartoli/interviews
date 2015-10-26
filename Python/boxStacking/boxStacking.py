"""
CS140 HW9 - #4 Block Stacking

@author Michael Bartoli

Problem: 
The goal of this program is to build the tallest tower possible out of a collection
of rectangular blocks. You are given some number of types of blocks, each with its
height, width, and length (all positive integers) specified. You can use as many of
each type of block as you would like, and a block can be placed in any of the three
stable orientations. A block can be stacked on top of another block if and only if the
two dimensions on the base of the top block are smaller than the two dimensions on
the base of the lower block.

Solution:
We simplfy the problem, slightly, by forcing the width to be greater than the length.
Then we generate the three rotations (instead of 6). We sort the array of possible
rotations in nondreasing order based on the base area. Our problem is now the same
as LIS. We solve it similarly. We run the output verifying each width, length 
combination is valid. We count the elements in our resulting array for the number of
blocks. 

We broke down the complexity of each function, to get a big-oh of O(n^2) 
You can see this if you sum up every occurence of big-oh. Try it (some are inline)! 

An interesting design function is my use of lambda to sort by the base areea. 

I tested my code against numerous examples I wrote out by hand. I deleted the 
assertions and test in this final version. 
See README for usage.
"""

import sys
from operator import itemgetter

def getBlockTypes(infile):
	"""
	@description gets the number of block types from the infile
	@complexity O(1)
	"""
	f = open(infile, 'r')
	blockTypes = int(f.readline().rstrip('\n'))
	return blockTypes

def getBlocks(infile):
	"""
	@description converts infile to a 2D array of int blocks
	@complexity O(n)
	"""
	f = open(infile, 'r')
	blocks = []
	counter = 0
	for line in f:
		if counter != 0:
			block = line.rstrip('\n').split(" ")
			block = [int(i) for i in block] 
			blocks.append(block)
		counter += 1
	return blocks

def getRotations(blocks):
	"""
	@description gets rotations for all blocks and returns a 2D array
	@complexity O(n)
	"""
	rotations = []
	# O(n) here
	for block in blocks:
		height = block[0]
		width = block[1]
		length = block[2]
		if width >= length:
			pass
		else:
			nl = width
			width = length
			length = nl
		
		rotation1 = [height, width, length]
		if height >= length:
			rotation2 = [width, height, length]
		else:
			rotation2 = [width, length, height]
		if width >= height: 
			rotation3 = [length, width, height]
		else: 
			rotation3 = [length, height, width]
		rotations.append(rotation1)
		rotations.append(rotation2)
		rotations.append(rotation3)
	return rotations

def getMaxHeight(blocks):
	"""
	@description gets max height using LIS and DP
	@complexity O(n^2)
	"""
	rotations = getRotations(blocks)
	# nondecreasing sort using the area (w x l) for every block
	rotations = sorted(rotations, key=lambda block : block[1]*block[2], reverse=True)
	
	heights = []
	results = []
	order = []        
	
	counter = 0
	# O(n) 
	for block in rotations:
		heights.append(block[0])
		results.append(counter)
		order.append(block)
		counter += 1
	
	# O(n^2) here, this is the DP part
	for i in range(1,len(heights)):
		for j in range(0,i):
			if (rotations[i][2] < rotations[j][2] and rotations[i][1] < rotations[j][1]):
				if (heights[j]+rotations[i][0] > heights[i]):
					heights[i] = heights[j] + rotations[i][0]
					results[i] = j

	forder = -1
	finalOrder = [[]]
	maxHeight = -2147483648 #minimum integer
	maxBlock = {}
	# O(n)
	for i in range(0,len(heights)):
		if (heights[i] > maxHeight):
			maxHeight = heights[i]
			finalOrder.append(order[i])

	finalOrder = finalOrder[1:]
	# sorting is O(n log n) here
 	finalOrder = sorted(finalOrder, key=lambda block : block[1]*block[2], reverse=False)
	output = [[]]
	previousBlock = [0,0,0]
	# O(n) here 
	for block in finalOrder:
		if previousBlock[1] < block[1] and previousBlock[2] < block[2]:
			output.append(block)
			previousBlock = block
	output = output[1:]
	blockSize = len(output)
	return [maxHeight, output, blockSize]


def main(infile):
	blockTypes = getBlockTypes(infile)
	blocks = getBlocks(infile)	
	bundle = getMaxHeight(blocks)
	maxHeight = bundle[0]
	order = bundle[1]
	numBlocks = bundle[2]
	print "The tallest tower has " + str(numBlocks) + " blocks and a height of " + str(maxHeight)
	file = open('outfile.txt','w')
	file.write(str(numBlocks)+"\n")
	for block in order: #O(n) to write to file 
		file.write(str(block[0])+" "+str(block[1])+" "+str(block[2])+"\n")	
	file.close()

if __name__ == "__main__":
	main(sys.argv[1])
