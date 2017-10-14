def rotations(t):
	""" Return list of rotations of input string t """
	tt = t * 2
	return [ tt[i:i+len(t)] for i in xrange(0, len(t)) ]

def bwm(t):
	return sorted(rotations(t))

def bwtViaBwm(t):
	""" Given T, returns BWT(T) by way of the BWM """
	return ''.join(map(lambda x: x[-1], bwm(t)))


def main():
	file_name = 'rosalind_ba9i.txt'
	# inp = 'GCGTGCCTGGTCA$'
	with open(file_name) as f:
		inp = f.read().strip()

	print bwtViaBwm(inp)

if __name__ == '__main__':
	main()