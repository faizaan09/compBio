# import pdb; pdb.set_trace()

def getFirst(last):
	count = {'A':0,'C':0,'G':0,'T':0}
	
	for alpha in last:
		if alpha == '$':
			continue
		count[alpha]+=1

	first = [('$',0)]

	for k in sorted(count.keys()):
		for i in range(count[k]):
			first.append((k,i))
	return first


def lastToFirst(last, ind):

	first = getFirst(last)
	count = {'A':0,'C':0,'G':0,'T':0,'$':0}
	new_last = []
	for l in last:
		new_last.append((l,count[l]))
		count[l] +=1

	last = new_last
	del new_last
	# print last,"\n\n\n"
	return first.index(last[ind])


def main():
	file_name = 'rosalind_ba9k.txt'
	inp = """T$GACCA
3"""
	ind = 0
	with open(file_name) as f:
		inp = f.read().strip()
	
	inp,ind = inp.split("\n")
	ind = int(ind)

	# first =  getFirst(inp)
	print lastToFirst(inp,ind)


if __name__ == '__main__':
	main()