# import pdb; pdb.set_trace()

from difflib import SequenceMatcher
import numpy as np


def find_overlap(s1,s2):
	s = SequenceMatcher(None,s1,s2)
	matches = s.get_matching_blocks()
	
	for m in matches:
		i,j,k = m
		if k > 0 and (i+k) == len(s1) and j ==0:
			return k*-1
	return 0


# def get_best_connection(mat):
# 	mi,mj = 0,0
# 	i,j = 0,0

# 	for 

	

def get_first(mat):
	for j in range(len(mat[0])):
		if sum(mat[:,j]) == 0:
			return j


def main():
	inp = '''>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC'''


	inp = inp[1:].split('>')

	inp = [i.split('\n',1)[1].replace('\n','') for i in inp] ## remove header and only store the string value
	size = len(inp)
	mat = np.zeros((size,size),dtype=int)
	visited = [[0 for i in xrange(size)] for x in xrange(size)]
	
	for i in range(size):
		for j in range(i+1,size):
			mat[i][j] = find_overlap(inp[i],inp[j])
			
			mat[j][i] = find_overlap(inp[j],inp[i])


	f = get_first(mat)
	scs = inp[f]
	for i in range(1,len(mat)):
		next_index = int(np.where(mat[f] == min(mat[f]))[0])
		next = inp[int(next_index)]
		next = next[-1*mat[f][next_index]:]
		scs = scs+ next
		f = next_index
		i+=1
	print scs

	

if __name__ == '__main__':
	main()