#This is the solution for an AlgoExpert Challenges
# Validate Subsequence - Easy 

def isValidSubsequence(array, sequence):
	x = 0
	y = 0
	while x < len(array):
		if array[x] == sequence[y]:
			y += 1
		if y == len(sequence):
			return True
		x += 1
	return False
