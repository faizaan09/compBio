import pdb; pdb.set_trace()

from difflib import SequenceMatcher


def find_overlap(s1,s2):
	s = SequenceMatcher(None,s1,s2,autojunk=False)
	matches = s.get_matching_blocks()
	# print matches
	for m in range(len(matches)-1):
		i,j,k = matches[m]
		if k > 0 and (i+k) == len(s1) and j ==0:
			# print k
			return k*-1
	return 0
	

def get_overlap(s1,s2):
	i,j = 0,0
	max = 0
	for i in range(0,min(len(s1),len(s2))):
		if s1[-i:] == s2[0:i]:
			if i > max:
				max = i 
	return -max


def get_best_connection(mat,visited):
	x,y,min = 0,0,0
	
	for i in range(len(mat)):
		for j in range(len(mat)):
			if mat[i][j] < min and sum(visited[i]) == 0:
				x,y = i,j
				min = mat[i][j]
	return x,y
	





def main():
	file_name = "demo.txt"
	# file_name = 'rosalind_long.txt'
	inp = ''
	with open(file_name) as f:
		inp = f.read().strip()


	inp = inp[1:].split('>')

	inp = [i.split('\n',1)[1].replace('\n','') for i in inp] ## remove header and only store the string value
	size = len(inp)
	tmp = inp
	mat = [[0 for s in range(size)] for i in range(size)]
	visited = [[0 for i in xrange(size)] for x in xrange(size)]
	
	i=0
	for i in range(size):
		print "i", i
		for j in range(i+1,size):
			mat[i][j] = get_overlap(inp[i],inp[j])
			
			mat[j][i] = get_overlap(inp[j],inp[i])

	i,j,scs = 0,0,0
	for c in range(1,len(mat)):
		i,j = get_best_connection(mat,visited)
		visited[i][j] = 1
		inp[i] = inp[i] + inp[j][-1*mat[i][j]:]
		inp[j] = inp[i]
		before = 0
		after = 0
		scs = j
		c+=1
	print inp[scs]
	

if __name__ == '__main__':
	main()