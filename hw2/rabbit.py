def main():
	file_name = 'rosalind_fibd.txt'

	inp = '6 3'
	with open(file_name) as f:
		inp = f.read().strip()
	
	month,age = inp.split(' ')
	month = int(month)
	age = int(age)

	rabs = [[0,0] for i in range(month)]
	for i in range(month):
		if i == 0:
			rabs[i] = [0,1]
		elif month < age:
			rabs[i][0] = rabs[i-1][0] + rabs[i-1][1]
			rabs[i][1] = rabs[i-1][0]
		else:
			rabs[i][0] = rabs[i-1][0] + rabs[i-1][1] - rabs[i-age][1]
			rabs[i][1] = rabs[i-1][0]
	
	print sum(rabs[month-1])

if __name__ == '__main__':
	main()