##Assignment 3 CSCI 3202
A* Path finding implemented in Python

##Run
>python WallingAssignment3.py

##Diagonal Heuristic
I got the idea for my heuristic from http://rocketmandevelopment.com/blog/a-heuristics/
The original equation I found was:

'''
var xDist:int = Math.abs(currentCell.x-goalCell.x);
var yDist:int = Math.abs(currentCell.y-goalCell.y);
if(xDist > yDist){
   H = 1.4*yDist + (xDist-yDist);
} else {
   H = 1.4*xDist + (yDist-xDist);
}

'''
So then I rewrote that in python to fit my program
