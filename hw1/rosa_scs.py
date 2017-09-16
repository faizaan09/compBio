# import pdb; pdb.set_trace()

def get_overlap(s1,s2):
	i,j = 0,0
	max = 0
	for i in range(0,min(len(s1),len(s2))):
		if s1[-i:] == s2[0:i]:
			if i > max:
				max = i 
	return -max

def get_best_connection(inp):
	x,y,min = 0,0,0
	
	for i in range(len(inp)-1):
		for j in range(i+1,len(inp)):
			overlap = get_overlap(inp[i],inp[j])
			if overlap < min:
				x,y = i,j
				min = overlap
	

	for i in range(len(inp)-1):
		for j in range(i+1,len(inp)):
			overlap = get_overlap(inp[j],inp[i])
			if overlap < min:
				x,y = j,i
				min = overlap
	
	
	return x,y,min
	

def main():
	# file_name = "demo.txt"
	file_name = 'rosalind_long.txt'
	inp = ''
	with open(file_name) as f:
		inp = f.read().strip()


	inp = inp[1:].split('>')

	inp = [i.split('\n',1)[1].replace('\n','') for i in inp] ## remove header and only store the string value
	size = len(inp)
	tmp = inp

	i,j,scs = 0,0,0
	while len(inp) >1:
		i,j,k = get_best_connection(inp)
		s1 = inp[i]
		s2 = inp[j]
		res = s1 + s2[-1*k:]
		inp.remove(s1)
		inp.remove(s2)
		inp.append(res)
	print inp[0]
	

if __name__ == '__main__':
	main()