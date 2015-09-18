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
