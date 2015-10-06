
class Node:
	def __init__(self, x, y, wall, reward):
		self.parent = None
		self.utility = 0
		self.x = x
		self.y = y
		self.wall = wall
		self.reward = reward

	def printNode(self):
		print self.x , self.y , self.reward
