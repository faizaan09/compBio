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
			mini = temp.index(min(temp))
			opt[i+1][j+1] = min(temp)
			if mini == 2 and cost(x[i],y[j]) == 0:
				map[i+1][j+1] = 3	
			else:
				map[i+1][j+1] = mini

	# print_opt(opt)
	# print "\n\n\n"
	# print_opt(map)
	return opt,map


def cost(x,y):
	if x ==y:
		return 0
	else:
		return 1

gap =1

def main():
	file_name = 'rosalind_edta.txt'
	inp = """>Rosalind_43
PRETTY
>Rosalind_97
PRTTEIN"""
	with open(file_name) as f:
		inp = f.read().strip()
	
	x,y = inp[1:].split(">")
	x = x.split('\n')[1:]
	x = ''.join(x)
	y = y.split('\n')[1:]
	y = ''.join(y)

	# x = 'AAGGTATGAATC'
	# y = 'AACGTTGAC'
	opt,map = get_edit_distance(x,y)
	# print_opt(map)

	i = len(x)
	j = len(y)
	p_x = ""
	p_y = ""
	c = 0

	# while i>0 and j>0:
	# 	cur = map[i][j]
	# 	if cur == 0:
	# 		p_x = "-" + p_x
	# 		p_y = y[j-1] + p_y
	# 		j-=1
	# 		c+=1
	# 	elif cur == 1:
	# 		p_x = x[i-1] + p_x
	# 		p_y = "_" + p_y
	# 		i-=1
	# 		c+=1
	# 	else:
	# 		if cur == 2:
	# 			c+=1
	# 		p_x = x[i-1] + p_x
	# 		p_y = y[j-1] + p_y
	# 		i-=1
	# 		j-=1
	
	# print x
	# print y
	while i >0 and j>0:
		cur = opt[i][j]
		temp = [ gap + opt[i-1][j], gap + opt[i][j-1], cost(x[i-1],y[j-1]) + opt[i-1][j-1]] 
		mini = temp.index(min(temp))
		# print mini
		if mini == 2:
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
	print c
	print p_x
	print p_y
	

if __name__ == '__main__':
	main()