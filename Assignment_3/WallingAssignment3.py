#!/usr/bin/env python
import sys
from Graph import Graph

def parseFile(fileDescriptor):
	parsed = []
	for line in fileDescriptor:
		parsed.append(line.rstrip('\n').split(' '))
	return parsed

fileName = "world1.txt"
heuristic = "manhattan"
fileName2 = "world2.txt"
heuristic2 = "diagonal" 

worldFile = open(fileName, 'r')
parsedWorld = parseFile(worldFile)


print 'A* on ' + fileName + ' using ' + heuristic
Graph(parsedWorld, heuristic)

print ""
print ""

print 'A* on ' + fileName + ' using ' + heuristic2
Graph(parsedWorld, heuristic2)

worldFile.close()

print ""
print ""


worldFile2 = open(fileName2, 'r')
parsedWorld2 = parseFile(worldFile2)

print 'A* on ' + fileName2 + ' using ' + heuristic
Graph(parsedWorld2, heuristic)

print ""
print ""

print 'A* on ' + fileName2 + ' using ' + heuristic2
Graph(parsedWorld2, heuristic2)

worldFile2.close()
