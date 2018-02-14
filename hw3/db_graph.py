def get_overlap(s1,s2,o_size):
	i,j = 0,0
	max = 0
	for i in range(0,len(s1)):
		if s1[-i:] == s2[0:i]:
			if i > max:
				max = i 
	return max == o_size

def rev_comp(string):
	rev = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	rev_string = ''.join([rev[i] for i in string[::-1]])

	return rev_string

import pdb; pdb.set_trace()

def main():
	file_name = 'rosalind_dbru.txt'
	inp = """TGAT
CATG
TCAT
ATGC
CATC
CATC"""

	with open(file_name) as f:
		inp = f.read().strip()

	inp = inp.split('\n')
	inp.extend([rev_comp(i) for i in inp])
	k_mers = [mer[:-1] for mer in inp]
	k_mers.extend([mer[1:] for mer in inp])
	overlap_len = len(k_mers[0])
	
	adj_list = set()

	for i in range(len(k_mers)):
		for j in range(len(k_mers)):
			if i !=j:
				if get_overlap(k_mers[i],k_mers[j],overlap_len-1):
					adj_list.add((k_mers[i],k_mers[j]))

	for elem in sorted(adj_list,key=lambda x: x[0]):
		print elem





if __name__ == '__main__':
	main()