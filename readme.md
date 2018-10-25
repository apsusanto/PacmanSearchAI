# Pacman Search AI
Submission for University of Toronto CSC384 - Introduction to Artificial Inteliggence Assignment 1 - Search.

## Fixed Food Dot using Depth-First Search
```
python pacman.py -l tinyMaze -p SearchAgent
python pacman.py -l mediumMaze -p SearchAgent
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
Using Depth-First Search starting from Pacman's position to find the shortest path to a food dot.

## Fixed Food Dot using Breadth-First Search
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
Using Bredth-First Search starting from Pacman's position to find the shortest path to a food dot.

## Varying the Cost Function (Uniform Cost Search)
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
Instead of finding the least amount of actions, which BFS does, Uniformed Cost Search will find a least cost path (optimal path) to the food dot.  
The cost of each action might not be uniform for all actions, therefore, the shortest path to a food dot might not be the most optimal.

## A* search
```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
A* search starting from Pacman's position to find an optimal path to the food dot, using Manhattan Distance as heuristic.

## Finding All Corners
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
A new state space formulation for other Pacman problem, which is to visit all corners optimally.  

## Heuristic for Corners Problem
```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
A non-trivial, non-negative, and admissible heuristic for pacman to be able to perform A* search on the corners problem.

## Eating All Dots
```
python pacman.py -l testSearch -p AStarFoodSearchAgent
python pacman.py -l oneDotFocus -p AStarFoodSearchAgent
```
A non-trivial, non-negative, and admissible heuristic which can be used to for Pacman to visit all foods on the maze.  
Here, the minimum spanning tree of all foods are formulated through Kruskal's MST algorithm, and using the sum of values of the edges in the minimum spanning tree, added with the distance between Pacman and the closest food, a rough underestimation can be obtained.

## Suboptimal (Greedy) Search
```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
```
A* with a good heuristic might take very long to compute, so that option might not be viable, especially for a huge and complicated maze. Therefore, a greedy solution which may return a suboptimal result but can reasonably find a good path is also implemented.