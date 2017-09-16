from math import log






def main():
	file_name = 'rosalind_prob.txt'
	with open(file_name) as f:
		inp = f.read()
	# inp = '''ACGATACAA
# 0.129 0.287 0.423 0.476 0.641 0.742 0.783'''
	inp = inp.split('\n')
	dna = inp[0]
	A = inp[1]
	A = [float(a) for a in A.split(' ')]
	# print dna
	# print A
	GC = 0
	for d in dna:
		if d in ('G','C'):
			GC+=1
	AT = len(dna) - GC
	res = []
	for a in A:
		res.append(AT*log((1-a)/2.0,10) + GC*log(a/2.0,10))
	res = [round(r,3) for r in res]
	print res
if __name__ == '__main__':
	main()