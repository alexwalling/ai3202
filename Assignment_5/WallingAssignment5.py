import sys
from Graph import Graph

def parseFile(fileDescriptor):
	parsed = []
	for line in fileDescriptor:
		#parsed.append(line.rstrip('\n').split(' '))
		parsed.append([elt.strip() for elt in line.split()])
	return parsed

fileName = "World1MDP.txt"

worldFile = open(fileName, 'r')
parsedWorld = parseFile(worldFile)

parsedWorld.reverse()

print "Enter epsilon value: "
epsilon = raw_input()
if isinstance(epsilon, str):
	epsilon = .5

a = Graph(len(parsedWorld), len(parsedWorld[0]))
#print parsedWorld
a.MDP(parsedWorld)
a.valueIteration(float(epsilon))
a.path()


#a.printNodes()

worldFile.close()

