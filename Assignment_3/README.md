##Assignment 3 CSCI 3202
A* Path finding implemented in Python

##Run
>python WallingAssignment3.py

##Diagonal Heuristic
>I got the idea for my heuristic from http://rocketmandevelopment.com/blog/a-heuristics/
>The original equation I found was:

```
var xDist:int = Math.abs(currentCell.x-goalCell.x);
var yDist:int = Math.abs(currentCell.y-goalCell.y);
if(xDist > yDist){
   H = 1.4*yDist + (xDist-yDist);
} else {
   H = 1.4*xDist + (yDist-xDist);
}
```

>So then I rewrote that in python to fit my program

```python
def diagonal(self, current, next):
Dist1 = abs(current[0] - next[0])
Dist2 = abs(current[1] - next[1])
if Dist1 > Dist2:
	return 10 * (1.4*Dist2 + (Dist1-Dist2))
else:
	return 10 * (1.4*Dist1 + (Dist2-Dist1))
```

#Motivation
>The idea behind this heuristic is to get a more straight shot to the goal as opposed to going as far in the x direction as you can and then as far in the y direction as you can
>
>I thought this would be a good method because as I said, it's more of a straight shot to the goal you want to reach.

#Results
```
A* on world1.txt using manhattan
___________________path found___________________
cost to reach goal: 156
number of locations evaluated: 103
Starting from the end: (9,7), (8,7), (7,7), (6,7), (5,7), (4,6), (3,5), (2,5), (1,4), (1,3), (1,2), (1,1), (0,0), 
```
```
>A* on world1.txt using diagonal
___________________path found___________________
cost to reach goal: 130
number of locations evaluated: 81
Starting from the end: (9,7), (8,7), (7,6), (7,5), (6,4), (5,4), (4,3), (4,2), (3,1), (2,0), (1,0), (0,0), 
```
```
>A* on world2.txt using manhattan
___________________path found___________________
cost to reach goal: 142
number of locations evaluated: 57
Starting from the end: (9,7), (8,7), (7,7), (6,7), (5,7), (4,6), (4,5), (4,4), (3,3), (2,3), (1,3), (0,2), (0,1), (0,0), 
```
```
A* on world2.txt using diagonal
___________________path found___________________
cost to reach goal: 142
number of locations evaluated: 150
Starting from the end: (9,7), (8,7), (7,7), (6,7), (5,7), (4,6), (4,5), (4,4), (4,3), (3,2), (3,1), (2,0), (1,0), (0,0),
``` 
