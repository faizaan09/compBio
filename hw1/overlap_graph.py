

def get_overlap(s1,s2,o_size):
	i,j = 0,0
	max = 0
	for i in range(0,min(len(s1),len(s2))):
		if s1[-i:] == s2[0:i]:
			if i > max:
				max = i 
	return max == o_size

def get_all_overlaps(inp,o_size):
	x,y,min = 0,0,0
	res = []
	for i in range(len(inp)-1):
		for j in range(i+1,len(inp)):
			overlap = get_overlap(inp[i],inp[j],o_size)
			o2 = get_overlap(inp[j],inp[i],o_size)
			if overlap:
				res.append([i,j])
			if o2:
				res.append([j,i])
				
	return res



def main():
	# file_name = 'demo.txt'
	file_name = 'rosalind_grph.txt'
	inp = ''
	with open(file_name) as f:
		inp = f.read().strip()

	inp = inp[1:].split('>')
	tmp = inp[:]
	inp = [i.split('\n',1)[1].replace('\n','') for i in inp] ## remove header and only store the string value
	strings = {}
	for i in tmp:
		v,k = i.split('\n',1)
		strings[k.replace('\n','')] = v.strip()
	res = get_all_overlaps(inp,3)
	check = []
	for r in res:
		check.append(strings[inp[r[0]]]+" "+strings[inp[r[1]]])

if __name__ == '__main__':
	main()

