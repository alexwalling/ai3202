class Node:
	def __init__(self, x, y, wall, reward):
		#self.parent = None
		self.utility = 0
		self.x = x
		self.y = y
		self.wall = wall
		self.reward = reward

	def printNode(self):
		print self.x, self.y, self.reward

class Graph:
	def __init__(self, height, width, gamma = 0.9):
		self.closed = set()
		self.nodes = []
		self.actions = ['left', 'right', 'up', 'down']
		self.height = height
		self.width = width
		self.gamma = gamma

	def MDP(self, graph):
		for y in range(self.height):
			for x in range(self.width):
				wall = False
				print("x: ", x)
				print ("y: ", y)
				print ("Value: ", graph[y][x])
				if graph[self.height - 1 - y][x] is '0':		#empty space
					reward = 0
				if graph[self.height - 1 - y][x] is '1':		#mountain
					reward = -1
				if graph[self.height - 1 - y][x] is '2':		#wall
					wall = True
					reward = 0
				if graph[self.height - 1 - y][x] is '3':		#snake
					reward = -2
				if graph[self.height - 1 - y][x] is '4':		#barn
					reward = 1
				if x == self.width - 1 and y == self.height - 1:		#end state
					reward = 50
				self.nodes.append(Node(x, y, wall, reward))
		self.start = self.getNode(0, 0)
		print "start" , self.start.printNode()
		self.end = self.getNode(self.width - 1, self.height - 1)
		print "end" , self.end.printNode()

	def getNode(self, x, y):
		print ""
		print self.width
		return self.nodes[y * self.width + x]

	def printNodes(self):
		print "hello"
		for i in range(0, self.width * self.height):
			print self.nodes[i].printNode()
