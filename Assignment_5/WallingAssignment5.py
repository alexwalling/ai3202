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

a = Graph(len(parsedWorld), len(parsedWorld[0]))
#print parsedWorld
a.MDP(parsedWorld)
a.valueIteration(float(.5))
a.path()


#a.printNodes()

worldFile.close()

