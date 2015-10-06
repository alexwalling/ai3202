import sys
from Graph import Graph

def parseFile(fileDescriptor):
	parsed = []
	for line in fileDescriptor:
		parsed.append(line.rstrip('\n').split(' '))
	return parsed

fileName = "World1MDP.txt"

worldFile = open(fileName, 'r')
parsedWorld = parseFile(worldFile)

a = Graph(len(parsedWorld) - 1, len(parsedWorld[0]))
a.MDP(parsedWorld)

a.printNodes()

worldFile.close()

