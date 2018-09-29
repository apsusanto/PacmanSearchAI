# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def transformPathToDirections(path):
    util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    open_ds = util.Stack()
    dir_ds = util.Stack()

    start_state = problem.getStartState()
    open_ds.push([start_state])
    dir_ds.push([])

    while not open_ds.isEmpty():
        node = open_ds.pop()
        dir_node = dir_ds.pop()
        end_state = node[-1]

        if problem.isGoalState(end_state):
            return dir_node

        successors = problem.getSuccessors(end_state)
        for succ in successors:
            if succ[0] not in node:
                new_node = copy.deepcopy(node)
                new_node.append(succ[0])
                open_ds.push(new_node)
                new_dir = dir_node + [succ[1]]
                dir_ds.push(new_dir)
    
    return False

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    open_ds = util.Queue()
    dir_ds = util.Queue()

    start_state = problem.getStartState()
    open_ds.push([start_state])
    dir_ds.push([])

    visited_state = [start_state]

    while not open_ds.isEmpty():
        node = open_ds.pop()
        dir_node = dir_ds.pop()
        end_state = node[-1]

        if problem.isGoalState(end_state):
            return dir_node

        successors = problem.getSuccessors(end_state)
        for succ in successors:
            if succ[0] not in visited_state:
                visited_state.append(succ[0])
                new_node = copy.deepcopy(node)
                new_node.append(succ[0])
                open_ds.push(new_node)
                new_dir = dir_node + [succ[1]]
                dir_ds.push(new_dir)
    
    return False

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    open_ds = util.PriorityQueue()
    dir_ds = util.PriorityQueue()
    cost_ds = util.PriorityQueue()

    start_state = problem.getStartState()
    open_ds.push([start_state], 0)
    dir_ds.push([], 0)
    cost_ds.push(0, 0)

    visited_state = {start_state: 0}

    while not open_ds.isEmpty():
        node = open_ds.pop()
        dir_node = dir_ds.pop()
        cost = cost_ds.pop()

        end_state = node[-1]

        if end_state not in visited_state or cost <= visited_state[end_state]:
            if problem.isGoalState(end_state):
                return dir_node

            successors = problem.getSuccessors(end_state)
            for succ in successors:
                if succ[0] not in visited_state or cost + succ[2] < visited_state[succ[0]]:
                    visited_state[succ[0]] = cost + succ[2]
                    new_node = copy.deepcopy(node)
                    new_node.append(succ[0])
                    open_ds.push(new_node, cost + succ[2])
                    new_dir = dir_node + [succ[1]]
                    dir_ds.push(new_dir, cost + succ[2])
                    cost_ds.push(cost + succ[2], cost + succ[2])

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # TODO: Implement tie breaking
    open_ds = util.PriorityQueue()
    dir_ds = util.PriorityQueue()
    cost_ds = util.PriorityQueue()

    start_state = problem.getStartState()
    open_ds.push([start_state], 0)
    dir_ds.push([], 0)
    cost_ds.push(0, 0)

    visited_state = {start_state: 0}

    while not open_ds.isEmpty():
        node = open_ds.pop()
        dir_node = dir_ds.pop()
        cost = cost_ds.pop()

        end_state = node[-1]

        if end_state not in visited_state or cost <= visited_state[end_state]:
            if problem.isGoalState(end_state):
                return dir_node

            successors = problem.getSuccessors(end_state)
            for succ in successors:
                if succ[0] not in visited_state or cost + succ[2] + heuristic(succ[0], problem) < visited_state[succ[0]]:
                    visited_state[succ[0]] = cost + succ[2] + heuristic(succ[0], problem)
                    new_node = copy.deepcopy(node)
                    new_node.append(succ[0])
                    open_ds.push(new_node, cost + succ[2] + heuristic(succ[0], problem))
                    new_dir = dir_node + [succ[1]]
                    dir_ds.push(new_dir, cost + succ[2] + heuristic(succ[0], problem))
                    cost_ds.push(cost + succ[2], cost + succ[2] + heuristic(succ[0], problem))

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
