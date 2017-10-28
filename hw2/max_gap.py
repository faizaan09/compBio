# import pdb; pdb.set_trace()




def print_opt(opt):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in opt]))

def get_edit_distance(x,y):
	opt = [[99999 for j in range(len(y)+1)] for i in range(len(x)+1)]
	rows = len(x)+1
	cols = len(y)+1
	map = [[-1 for j in range(len(y)+1)] for i in range(len(x)+1)]
	# gap = 1

	opt[0][0] = 0
	for j in range(1,cols):
		opt[0][j] = gap + opt[0][j-1]

	for i in range(1,rows):
		opt[i][0] = gap + opt[i-1][0]

	for i in range(len(x)):
		for j in range(len(y)):
			temp = [ gap + opt[i+1][j], gap + opt[i][j+1], cost(x[i],y[j]) + opt[i][j]]
			mini = temp.index(max(temp))
			opt[i+1][j+1] = max(temp)
	
	# print_opt(opt)
	# print "\n\n\n"
	# print_opt(map)
	return opt,map


def cost(x,y):
	if x ==y:
		return 1
	else:
		return -2

gap =-1

def main():
	file_name = 'rosalind_mgap.txt'
	inp = """>Rosalind_92
AACGTA
>Rosalind_47
ACACCTA"""
	with open(file_name) as f:
		inp = f.read().strip()
	
	x,y = inp[1:].split(">")
	x = x.split('\n')[1:]
	x = ''.join(x)
	y = y.split('\n')[1:]
	y = ''.join(y)

	opt,map = get_edit_distance(x,y)
	# print_opt(map)

	i = len(x)
	j = len(y)
	p_x = ""
	p_y = ""
	c = 0

	while i >0 and j>0:
		cur = opt[i][j]
		temp = [gap + opt[i][j-1], gap + opt[i-1][j], cost(x[i-1],y[j-1]) + opt[i-1][j-1]] 
		mini = temp.index(max(temp))
		# print mini
		if mini == 2:
			if cur != opt[i-1][j-1]:
				c+=1
			p_x = x[i-1] + p_x
			p_y = y[j-1] + p_y
			i-=1
			j-=1
			continue
		elif mini == 1:
			p_x = x[i-1] + p_x
			p_y = "-" + p_y
			i-=1
			c+=1
		else:
			p_x = "-" + p_x
			p_y = y[j-1] + p_y
			j-=1
			c+=1
	print p_x.count('-') + p_y.count('-')
	

if __name__ == '__main__':
	main()