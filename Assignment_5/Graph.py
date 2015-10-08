class Node:
	def __init__(self, x, y, wall, reward):
		self.parent = None
		self.utility = 0
		self.x = x
		self.y = y
		self.wall = wall
		self.reward = reward

	def printNode(self):
		print self.x, self.y, self.reward, self.utility, self.wall, self.parent

class Graph:
	def __init__(self, height, width, gamma = 0.9):
		self.closed = set()
		self.nodes = []
		self.actions = ['left', 'right', 'up', 'down']
		self.height = height
		self.width = width
		self.gamma = gamma

	def MDP(self, graph):
		reward = 0
		for y in range(len(graph)):
			for x in range(len(graph[0])):
				wall = False
				#print("x: ", x)
				#print ("y: ", y)
				#print ("Value: ", graph[y][x])
				if graph[y][x] is '0':		#empty space
					reward = 0
				if graph[y][x] is '1':		#mountain
					reward = -1
				if graph[y][x] is '2':		#wall
					wall = True
					reward = 0
				if graph[y][x] is '3':		#snake
					reward = -2
				if graph[y][x] is '4':		#barn
					reward = 1
				if x == self.width - 1 and y == self.height - 1:	#end state
					reward = 50
				self.nodes.append(Node(x, y, wall, reward))
		self.start = self.getNode(0, 0)
		self.end = self.getNode(len(graph[0]) - 1, len(graph) - 1)

	def getNode(self, x, y):
		#print "start print"
		#for i in self.nodes:
		#	i.printNode()
		#print len(self.nodes)
		#print "x:",x,"y:" , y
		#print y * self.width + x
		#print self.width
		#print self.height
		return self.nodes[y * self.width + x]

	def printNodes(self):
		print "hello"
		for i in range(0, self.width * self.height):
			print self.nodes[i].printNode()

	def transition(self, x, y):
		actionvalue = []
		for i in range(len(self.actions)):
			if self.actions[i] is 'left':
				temp = 0
				if x - 1 >= 0:
					temp = .8 * self.getNode(x - 1, y).utility
				if y + 1 <= self.height - 1:
					temp = .1 * self.getNode(x, y + 1).utility + temp
				if y - 1 >= 0:
					temp = .1 * self.getNode(x, y - 1).utility + temp
				actionvalue.append(temp)
			if self.actions[i] is 'right':
				temp = 0
				if x + 1 <= self.width - 1:
					temp = .8 * self.getNode(x + 1, y).utility
				if y + 1 <= self.height - 1:
					temp = .1 * self.getNode(x, y + 1).utility + temp
				if y - 1 >- 0:
					temp = .1 * self.getNode(x, y - 1).utility + temp
				actionvalue.append(temp)
			if self.actions[i] is 'up':
				temp = 0
				if y + 1 <= self.height - 1:
					temp = .8 * self.getNode(x, y + 1).utility
				if x + 1 <= self.width - 1:
					temp = .1 * self.getNode(x + 1, y).utility + temp
				if x - 1 >= 0:
					temp = .1 * self.getNode(x - 1, y).utility + temp
				actionvalue.append(temp)
			if self.actions[i] is 'down':
				temp = 0
				if y - 1 >= 0:
					temp = .8 * self.getNode(x, y - 1).utility
				if x + 1 <= self.width - 1:
					temp = .1 * self.getNode(x + 1, y).utility + temp
				if x - 1 >= 0:
					temp = .1 * self.getNode(x - 1, y).utility + temp
				actionvalue.append(temp)
		return actionvalue

	def valueIteration(self, epsilon):
		gamma = self.gamma
		delta = float('Inf')
		while delta > epsilon*(1 - gamma)/gamma:
			for n in reversed(self.nodes):
				if n.wall is False:
					currentUtility = n.utility
				#	print n.x , " " , n.y
				#	print max(self.transition(n.x, n.y))
					n.utility = n.reward + gamma*max(self.transition(n.x, n.y))
					delta = abs(currentUtility - n.utility)

	def path(self):
		self.adjacentNode(self.start)
		p = []
		tempnode = self.end
		p.append(tempnode)
		while tempnode.parent is not self.start:
			tempnode = tempnode.parent
			p.append(tempnode)
		p.append(self.start)	
		print "Printing Path"
		for n in reversed(p):
			#n.printNode()
			print "x:", n.x, "y:", n.y

	def adjacentNode(self, node):
		adjUtility = []
		adjNode = []
		if node.x < self.width-1:
			adjUtility.append(self.getNode(node.x + 1, node.y).utility)
			adjNode.append(self.getNode(node.x + 1, node.y))	
		if node.x > 0:
			adjUtility.append(self.getNode(node.x - 1, node.y).utility)
			adjNode.append(self.getNode(node.x - 1, node.y))
		if node.y < self.height - 1:
			adjUtility.append(self.getNode(node.x, node.y + 1).utility)
			adjNode.append(self.getNode(node.x, node.y + 1))
		if node.y > 0:
			adjUtility.append(self.getNode(node.x, node.y - 1).utility)
			adjNode.append(self.getNode(node.x, node.y - 1))

		if node is not self.end:
			adjNode[adjUtility.index(max(adjUtility))].parent = node
			self.adjacentNode(adjNode[adjUtility.index(max(adjUtility))])
