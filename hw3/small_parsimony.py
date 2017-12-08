
import os
from collections import defaultdict
# import pdb; pdb.set_trace()

alphabet = ['A', 'C', 'G', 'T', ]


def dist(x, y):
	if x == y:
		return 0
	else:
		return 1

class Node(object):
	def __init__(self, index, is_leaf):
		self.index = index
		self.is_leaf = is_leaf
		self.children = []
		self.edge_len = []
		self.text = ''
		self.score = defaultdict(int)
		self.is_scored = False

	def calc_score(self, curr_letter):
		if self.is_leaf:
			for alpha in alphabet:
				if alpha == self.text[curr_letter]:
					self.score[alpha] = 0
				else:
					self.score[alpha] = float('inf')
		else:
			for alpha in alphabet:
				for child in self.children:
					self.score[alpha] += min([all_nodes[child].score[i]+dist(alpha, i) for i in alphabet])
		self.is_scored = True
		return None

	def is_ripe(self):
		if self.is_leaf:
			return True
		else:
			for c in self.children:
				if not all_nodes[c].is_scored:
					return False
		return True

	def __str__(self):
		return "\nindex: "+ str(self.index) + "\nisLeaf:" + str(self.is_leaf) +"\nChildren: " +' '.join(self.children) +"\nEdges: " + ' '.join(self.edge_len) +"\nText: " + self.text + "\nScore: " + str(self.score) +"\nScored: " + str(self.is_scored) + "\n"


def generate_tree(conn):
	num_leaves = int(conn.readline().strip())
	all_nodes = [Node(i, True) for i in range(num_leaves)]

	for j, inp in enumerate(conn):
		line = inp.strip().split('->')
		val = int(line[0])
		if val == len(all_nodes):
			all_nodes.append(Node(val, False))
		if j < num_leaves:
			all_nodes[val].children.append(j)
			all_nodes[val].edge_len.append(0)
			all_nodes[j].text = line[1]
		if j >= num_leaves:
			all_nodes[val].children.append(int(line[1]))
			all_nodes[val].edge_len.append(0)
	return all_nodes

def get_all_edge_weights(node):
	global running_sum
	if node.is_leaf:
		return None
	for index, item in enumerate(node.children):
		text_dist = 0
		for i in range(len(node.text)):
			if node.text[i] != all_nodes[item].text[i]:
				text_dist += 1
		
		running_sum += text_dist
		node.edge_len[index] = text_dist
		get_all_edge_weights(all_nodes[item])
	return None


def calc_tree_score(curr_letter):
	for node in all_nodes:
		if node.is_leaf:
			node.calc_score(curr_letter)
	while not all_nodes[-1].is_scored:
		for node in all_nodes:
			if not node.is_scored:
				if node.is_ripe():
					node.calc_score(curr_letter)
	return None


def phase_2(node, parent_letter=''):
	if node.is_leaf:
		return None
	mini = float('inf')
	choice = ''
	for letter in alphabet:
		s = node.score[letter]
		if parent_letter != letter:
			s += 1
		if s < mini:
			mini = s
			choice = letter
	node.text += choice
	for i in node.children:
		phase_2(all_nodes[i], choice)
	return None



def print_output(node):
	if node.is_leaf:
		return
	for i, c in enumerate(node.children):
		child = all_nodes[c]
		print node.text+'->'+child.text+':'+str(node.edge_len[i])+'\n'
		print child.text+'->'+node.text+':'+str(node.edge_len[i])+'\n'
		print_output(child)
	return


if __name__ == '__main__':

	file_name = 'rosalind_ba7f.txt'
	with open(file_name) as f:
		all_nodes = generate_tree(f)
	seq_len = len(all_nodes[0].text)
	for i in range(seq_len):
		calc_tree_score(i)
		phase_2(all_nodes[-1])
		for node in all_nodes:
			# reset scores
			node.score = defaultdict(int)
			node.is_scored = False
	running_sum = 0
	get_all_edge_weights(all_nodes[-1])
	print running_sum
	print_output(all_nodes[-1])