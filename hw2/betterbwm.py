

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




def betterbwm(last,p):

	# first = getFirst(last)
	top  = 0
	bottom = len(last)-1

	cur_count = {'A':[0]*len(last),'C':[0]*len(last),'G':[0]*len(last),'T':[0]*len(last),'$':[0]*len(last)}
	tot_count = {'A':0,'C':0,'G':0,'T':0,'$':0}

	for i in range(len(last)):
		tot_count[last[i]]+=1
		cur_count[last[i]][i]= tot_count[last[i]]
	# print cur_count

	first_occ = {}
	for i in range(len(last)):
		if set(first_occ.keys()) == set(['A','C','G','T','$']):
			break
		if last[i] not in first_occ:
			first_occ[last[i]] = i
	# print first_occ


	while top <= bottom:
		if p:
			symbol = p.pop()
			if symbol in last[top:bottom+1]:
				top = first_occ[symbol] + cur_count[symbol][top]
				bottom = first_occ[symbol] + cur_count[symbol][bottom]-1
			else:
				return 0
		else:
			return bottom- top +1

	return -1




def main():
	file_name = 'rosalind_ba9l.txt'
	inp = """GGCGCCGC$TAGTCACACACGCCGTA
ACC CCG CAG"""
	# with open(file_name) as f:
	# 	inp = f.read().strip()
	
	inp,patterns = inp.split("\n")
	patterns = patterns.split(" ")

	ans = []
	for i in range(len(patterns)):
		ans.append(betterbwm(inp,list(patterns[i])))

	print ans


if __name__ == '__main__':
	main()