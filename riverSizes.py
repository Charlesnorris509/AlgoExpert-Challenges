def riverSizes(matrix):
    visited = [[False for x in row] for row in matrix]
	res = []
	for x in range(len(matrix)):
		for y in range(len(matrix[x])):
			if visited[x][y]:
				continue
			traverse(x, y, matrix, visited, res)
	return res

def traverse(idx1, idx2, matrix, visited, res):
	curr = 0
	stack = [[idx1, idx2]]
	while len(stack) != 0:
		curr_stack =  stack.pop()
		i = curr_stack[0]
		j = curr_stack[1]
		if visited[i][j]:
			continue
		visited[i][j] = True
		if matrix[i][j] ==0:
			continue
		curr += 1
		unvisited = helper(i, j, matrix, visited)
		for temp in unvisited:
			stack.append(temp)
	if curr > 0:
		res.append(curr)
		
def helper(i, j, matrix, visited):
	unvisitedNeighbors = []
	if i > 0 and not visited[i -1][j]:
		unvisitedNeighbors.append([i - 1, j])
	if i < len(matrix) - 1 and not visited[i+1][j]:
		unvisitedNeighbors.append([i + 1, j])
	if j > 0 and not visited[i][j -1]:
		unvisitedNeighbors.append([i, j - 1])
	if j < len(matrix[i])-1 and not visited[i][j + 1]:
		unvisitedNeighbors.append([i, j +1])
	return unvisitedNeighbors
