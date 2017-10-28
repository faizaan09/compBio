# import pdb; pdb.set_trace()




def print_opt(opt):
	print('\n'.join([''.join(['{:8}'.format(item) for item in row]) 
      for row in opt]))

def get_edit_distance(x,y):
	opt = [[[0,1] for j in range(len(y)+1)] for i in range(len(x)+1)]
	rows = len(x)+1
	cols = len(y)+1
	map = [[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]
	# gap = 1

	opt[0][0] = 0,1
	for j in range(1,cols):
		opt[0][j] = gap + opt[0][j-1][0],1

	for i in range(1,rows):
		opt[i][0] = gap + opt[i-1][0][0],1

	for i in range(len(x)):
		for j in range(len(y)):
			temp = [ gap + opt[i+1][j][0], gap + opt[i][j+1][0], cost(x[i],y[j]) + opt[i][j][0]]
			mini = temp.index(min(temp))
			opt[i+1][j+1] = min(temp),0
			if temp[mini] == temp[0]:
				opt[i+1][j+1] = min(temp), opt[i+1][j][1] + opt[i+1][j+1][1] 
			if temp[mini] == temp[2]:
				opt[i+1][j+1] = min(temp), opt[i][j][1] + opt[i+1][j+1][1]
			if temp[mini] == temp[1]:
				opt[i+1][j+1] = min(temp), opt[i][j+1][1] + opt[i+1][j+1][1]
			
			# if mini == 2 and cost(x[i],y[j]) == 0:
			# 	map[i+1][j+1] = 3	
			# else:
			# 	map[i+1][j+1] = mini

	# print_opt(opt)
	print opt[rows-1][cols-1][1] %  134217727
	return opt,map

def cost(x,y):
	if x ==y:
		return 0
	else:
		return 1

gap =1

def main():
	file_name = 'rosalind_ctea.txt'
	inp = """>Rosalind_78
PLEASANTLY
>Rosalind_33
MEANLY"""
	with open(file_name) as f:
		inp = f.read().strip()
	
	x,y = inp[1:].split(">")
	x = x.split('\n')[1:]
	x = ''.join(x)
	y = y.split('\n')[1:]
	y = ''.join(y)

	opt,map = get_edit_distance(x,y)

	i = len(x)
	j = len(y)
	p_x = ""
	p_y = ""
	c = 0
	

if __name__ == '__main__':
	main()