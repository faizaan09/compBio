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


def lastToFirst(last, ind,first):

	# first = getFirst(last)
	count = {'A':0,'C':0,'G':0,'T':0,'$':0}
	new_last = []
	for l in last:
		new_last.append((l,count[l]))
		count[l] +=1

	last = new_last
	del new_last
	# print last,"\n\n\n"
	return first.index(last[ind])


def bwmatching(last,p):

	first = getFirst(last)
	top  = 0
	bottom = len(last)-1

	while top <= bottom:
		if p:
			symbol = p.pop()
			if symbol in last[top:bottom+1]:
				topIndex = last[top:bottom +1].find(symbol) +top
				bottomIndex = last[top:bottom +1].rfind(symbol) + top
				top = lastToFirst(last,topIndex,first)
				bottom = lastToFirst(last,bottomIndex,first)
			else:
				return 0
		else:
			return bottom- top +1

	return -1




def main():
	file_name = 'rosalind_ba9l.txt'
	inp = """TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
CCT CAC GAG CAG ATC"""
	with open(file_name) as f:
		inp = f.read().strip()
	
	inp,patterns = inp.split("\n")
	patterns = patterns.split(" ")

	ans = []
	for i in range(len(patterns)):
		ans.append(bwmatching(inp,list(patterns[i])))

	print ans


if __name__ == '__main__':
	main()