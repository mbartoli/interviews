def subMergeLIS(i,j,A):
	bestStartIndex = i
	newStartIndex = i
	longestSoFar = 1
	numIncreasing = 1

	n = i
	while (n < j):
		if A[n] <= A[n+1]:
			numIncreasing += 1
			if numIncreasing > longestSoFar:
				longestSoFar = numIncreasing
				bestStartIndex = newStartIndex
		else:
			newStartIndex = n+1
			numIncreasing = 1
		n = n+1
	return bestStartIndex, longestSoFar


def main():
	stocks = [1,2,4,3,5,2,3,4]
	x, y = 3,7
	print subMergeLIS(x,y,stocks)

if __name__ == "__main__":
	main()
