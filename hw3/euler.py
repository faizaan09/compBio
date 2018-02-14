from collections import defaultdict
from copy import copy, deepcopy

# import pdb; pdb.set_trace()


def DFS(node, adj_list, visited, path=[]):
	visited[node] = True
	path.append(node)
	if node not in adj_list:
		return

	for i in adj_list[node]:
		if not visited[i]:
			DFS(i, adj_list, visited, path)
	return


def get_vertices(G):
	counts = set(key for key in G.keys())

	for node in G:
		for dst in G[node]:
			if dst not in counts:
				counts.add(dst)

	return counts


def is_bridge(adj_list, node):
	all_vers = get_vertices(adj_list)
	visited = {ver: False for ver in all_vers}
	path = []
	DFS(node, adj_list, visited, path)
	return len(path) != len(all_vers)


def traverse(cur_node,adj_list):
	
	traversed_path = []
	while cur_node in adj_list:
		if len(adj_list[cur_node]) == 1:
			dst = adj_list[cur_node][0]
			adj_list[cur_node].remove(dst)
			if len(adj_list[cur_node]) == 0:
				adj_list.pop(cur_node, None)
			traversed_path.append(cur_node)
			cur_node = dst
			continue

		for dst in adj_list[cur_node]:
			if not is_bridge(adj_list, dst):
				adj_list[cur_node].remove(dst)
				if len(adj_list[cur_node]) == 0:
					adj_list.pop(cur_node, None)
				traversed_path.append(cur_node)
				cur_node = dst
				break

	if cur_node not in adj_list:
		traversed_path.append(cur_node)
		return traversed_path


	


def main():
	inp = """0 -> 2
1 -> 3
2 -> 1
3 -> 0,4
6 -> 3,7
7 -> 8
8 -> 9
9 -> 6"""

	file_name = '../../Computational-Biology/hw3/eulerian_path.txt'
	with open(file_name) as f:
		inp = f.read().strip()

	inp = inp.split('\n')
	adj_list = {}
	for i in range(len(inp)):
		s = inp[i].split('->')
		# print s
		adj_list[int(s[0])] = [int(dest.strip()) for dest in s[1].split(',')]
		# print adj_list
	
	degree = defaultdict(int)

	for node in adj_list:
		dests = adj_list[node]
		degree[node] += len(dests)
		for d in dests:
			degree[d] -=1
	
	start_node = max(degree,key=lambda x: degree[x])
	end_node = min(degree, key=lambda x: degree[x])
	pass  

	path =  traverse(start_node,deepcopy(adj_list))
	euler_path = ""
	for node in path:
		euler_path+= str(node) + "->"
	print euler_path

if __name__ == '__main__':
	main()