import pdb; pdb.set_trace()



def cost(x,y):
	if x ==y:
		return 0
	else:
		return 1


def print_opt(opt):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in opt]))

def get_edit_distance(x,y):
	opt = [[99999 for j in range(len(y)+1)] for i in range(len(x)+1)]
	rows = len(x)+1
	cols = len(y)+1
	gap = 1

	opt[0][0] = 0
	for j in range(1,cols):
		opt[0][j] = gap + opt[0][j-1]

	for i in range(1,rows):
		opt[i][0] = gap + opt[i-1][0]

	for i in range(len(x)):
		for j in range(len(y)):
			opt[i+1][j+1] = min(cost(x[i],y[j]) + opt[i][j], gap + opt[i][j+1], gap + opt[i+1][j])

	print_opt(opt)
	return opt





def main():
	file_name = 'rosalind_ba9l.txt'
	inp = """>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN"""
	# with open(file_name) as f:
	# 	inp = f.read().strip()
	
	x,y = inp[1:].split(">")
	x = x.split('\n')[1]
	y = y.split('\n')[1]

	# x = 'AAGGTATGAATC'
	# y = 'AACGTTGAC'
	opt = get_edit_distance(x,y)

	i = len(x)
	j = len(y)
	p_x = ""
	p_y = ""
	c = 0
	gap =1
	while i >0 and j>0:
		cur = opt[i][j]
		temp = [gap + opt[i-1][j], opt[i-1][j-1] , gap + opt[i][j-1]] 
		mini = temp.index(min(temp))
		print mini
		if mini == 1:
			if cur != opt[i-1][j-1]:
				c+=1
			p_x = x[i-1] + p_x
			p_y = y[j-1] + p_y
			i-=1
			j-=1
			continue
		elif mini == 0:
			p_x = x[i-1] + p_x
			p_y = "-" + p_y
			i-=1
			c+=1
		else:
			p_x = "-" + p_x
			p_y = y[j-1] + p_y
			j-=1
			c+=1
	print p_x
	print p_y
	print c

if __name__ == '__main__':
	main()