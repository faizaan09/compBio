import pdb; pdb.set_trace()

class Tree(object):

	def __init__(self,data=None,left=None,right=None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return self.data + ": left->"+ self.left + "\n" + self.data + ": right->"+ self.right		

def main():
	input_data = """4
4->CAAATCCC
4->ATTGCGAC
5->CTGCGCTG
5->ATGGACGA
6->4
6->5"""

	input_data = input_data.split('\n')
	leaves = {}
	tag = {}
	num_leaves = int(input_data[0])
	for i in range(num_leaves):
		node,val = input_data[i+1].split("->")
		if node not in leaves:
			leaves[node] = Tree(node,val)
		else:
			tree_node = leaves[node]
			tree_node.right = val
	# for i in range(1+ num_leaves,len(input_data)):
	print leaves['5']
	print leaves['4']
	pass

if __name__ == '__main__':
	main()