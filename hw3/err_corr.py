def parse_input(path, no_id=True):
    ids = []
    seqs = []
    
    with open(path, 'r') as f:
        for line in f.readlines():
            if line.startswith('>'):
                ids.append(line[1:].strip())
                seqs.append('')
            else:
                seqs[-1] += line.strip()

	return seqs


def rev_comp(string):
	rev = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
	rev_string = ''.join([rev[i] for i in string[::-1]])

	return rev_string

def hamming_dist(x, y, limit=1):
	dist = 0
	
	for i in range(min(len(x), len(y))):
		if x[i] != y[i]:
			dist += 1
		if dist > limit:
			return(dist)

	return dist

def count_apperances(all_strings):
	str_count = {}

	for s in all_strings:
		if s in str_count:
			str_count[s] += 1
		else:
			if rev_comp(s) in str_count:
				str_count[rev_comp(s)] += 1
			else:
				str_count[s] = 1
				str_count[rev_comp(s)] = 1

	return str_count


def error_correct(all_strings):
	str_count = count_apperances(all_strings)
	correct = []
	incorrect = []
	corrections = []
	
	for j in str_count:
		if str_count[j] > 1:
			correct.append(j)
		else:
			incorrect.append(j)

	for i in incorrect:
		for j in correct:
			if hamming_dist(i, j) < 2:
				corrections.append([i, j])

	return corrections


def main():
	strings = parse_input('rosalind_corr.txt')
	strings += [rev_comp(i) for i in strings]

	corrected = error_correct(strings)
	
	for c in corrected:
		print c[0] + '->' +c[1] + '\n'


if __name__ == '__main__':
	main()