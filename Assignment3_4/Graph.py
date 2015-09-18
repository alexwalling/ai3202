import Queue
import math

class Graph():
	def __init__(self, data, heuristic):
		self.closed = {}
		self.height = len(data)
		self.width = len(data[0])
		self.data = data
		self.start = (self.height - 1, 0)
		self.end = (0, self.width - 1)

        	self.aStar(heuristic)

	def printInfo(self):
		print 'height: ' + str(self.height)
 		print 'width: ' + str(self.width)


	def manhattan(self, current, next):
		return 10 * (abs(current[0] - next[0]) + abs(current[1] - next[1]))
	
	def diagonal(self, current, next):
		Dist1 = abs(current[0] - next[0])
		Dist2 = abs(current[1] - next[1])
		if Dist1 > Dist2:
			return 10 * (1.4*Dist2 + (Dist1-Dist2))
		else:
			return 10 * (1.4*Dist1 + (Dist2-Dist1))

	def isMountain(self, myTuple):
		return int(self.data[myTuple[0]] [myTuple[1]]) == 1

	def isWall(self, myTuple):
		return int(self.data[myTuple[0]] [myTuple[1]]) == 2


	def adjacent(self, current):
		def isValid(myTuple):
			first, second = myTuple
			return (first > -1) and (first < self.height) and (second > -1) and (second < self.width)

		def validadjacent(adjacentNodes):
			ret = []
			for i in adjacentNodes:
				if isValid(i) and not self.isWall(i):
					ret.append(i)
			return ret

		x, y = current

		adjacentNodes = [(x-1, y), (x-1, y+1), (x,y+1), (x+1,y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)]

		return validadjacent(adjacentNodes)


	def cost(self, curr, next):
		if (int(self.manhattan(curr, next)) == 10):
			ret = 10
		else:
			ret = 14
		if (self.isMountain(next)):
			ret += 10
		return ret

	def aStar(self, heuristic):
		def printPath(curr):
			toPrint ="Starting from the end: "
			while (not curr == None):
				toPrint += "(" + str(curr[1]) + "," + str(self.height - 1 - curr[0]) + ")"+ ", "
				curr = cameFrom[curr]
 			print toPrint

		open = Queue.PriorityQueue()
		open.put((0, self.start))
		locationsEvaluated = 0
		cameFrom = {self.start: None}

		costSoFar = {self.start: 0}

		while (not open.empty()):
			(closed, curr) = open.get()
			if (curr == self.end):
				print "___________________path found___________________"
				print "cost to reach goal: " + str(costSoFar[self.end])
				print "number of locations evaluated: " + str(locationsEvaluated)
				printPath(self.end)
				break

			for nextNode in self.adjacent(curr):
				locationsEvaluated += 1
				newCost = costSoFar[curr] + self.cost(curr, nextNode)
				if nextNode not in costSoFar or newCost < costSoFar[nextNode]:
					costSoFar[nextNode] = newCost
					if (heuristic == 'manhattan'):
						optimality = newCost + self.manhattan(nextNode, self.end)
					else:
						optimality = newCost + self.diagonal(nextNode, self.end)
					open.put((optimality, nextNode))
					cameFrom[nextNode] = curr
