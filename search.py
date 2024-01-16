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





def tinyMazeSearch(problem):

    """

    Returns a sequence of moves that solves tinyMaze.  For any other maze, the

    sequence of moves will be incorrect, so only use this for tinyMaze.

    """

    from game import Directions

    s = Directions.SOUTH

    w = Directions.WEST

    return  [s, s, w, s, w, w, s, w]

    

# Returns a Direction object

def getDirection(direction):

	from game import Directions

	n = Directions.NORTH

	e = Directions.EAST

	s = Directions.SOUTH

	w = Directions.WEST

	if direction == 'North':

		return n

	elif direction == 'East':

		return e

	elif direction == 'South':

		return s

	elif direction == 'West':

		return w

	else:

		return 'start'



def search(problem, state, fringe, expanded, path, priority = False, heur = False):

	#print("state: ", state)

	# goal state found

	position, counter = state[0]

	if problem.isGoalState(state[0]):

		# adding last direction into path

		print("GOAL STATE FOUND")

		newpath = list()

		direction = getDirection(state[1])

		if isinstance(counter, int):

			newpath.extend(path[state[0]])

		else:

			newpath.extend(path[position])

		if direction != 'start': 

			newpath.append(direction)

		path[(0, 0)] = newpath

		return path

	

	else:

		# adding current state into expanded list

		if isinstance(counter, int):

			expanded.add(state[0])

		else:

			expanded.add(position)

		# getting successors

		successors = problem.getSuccessors(state[0])

		#print("successors: ", successor)

		# looping through successor to add them to the fringe depending on the search strategy

		for child in successors:

			# adding successor as key with parent as value in path dictionary

			pos, count = child[0]

			if isinstance(count, int):

				# adding successor as key with parent as value in path dictionary

				if child[0] not in path:

					newpath = list()

					direction = getDirection(child[1])

					newpath.extend(path[state[0]])

					if direction != 'start': 

						newpath.append(direction)

					path[child[0]] = newpath

					#print('new path: ', path[child[0]])

				# adding successor to fringe if not already expanded

				if child[0] not in expanded:

					if priority == False:

						fringe.push(child)

					else:

						priority = problem.getCostOfActions(path[child[0]])

						fringe.push(child, priority)

			else:

				# adding successor as key with parent as value in path dictionary

				if pos not in path:

					newpath = list()

					direction = getDirection(pos)

					newpath.extend(path[position])

					if direction != 'start': 

						newpath.append(direction)

					path[pos] = newpath

				#print('new path: ', path[child[0]])

				# adding successor to fringe if not already expanded

				if pos not in expanded:

					if priority == False:

						fringe.push(child)

					else:

						priority = problem.getCostOfActions(path[pos])

						fringe.push(child, priority)

		# checking if fringe is empty

		if fringe.isEmpty():

			newpath = list()

			direction = getDirection(state[1])

			if isinstance(counter, object):

				newpath.extend(path[position])

				if direction != 'start': 

					newpath.append(direction)

			else:

				newpath.extend(path[state[0]])

			if direction != 'start': 

				newpath.append(direction)

			path[(0, 0)] = newpath

			return path

		else:

			# making sure the next state isn't the current state

			if heur == False:

				nextState = fringe.pop()

				if nextState == state:

					nextState = fringe.pop()

				position, counter = nextState[0]

				if priority == False:

					search(problem, nextState, fringe, expanded, path)

				else:

					search(problem, nextState, fringe, expanded, path, True)

			else:

				nextState = fringe.pop()

				if nextState == state:

					actions, nextState = fringe.pop()

				search(problem, nextState, fringe, expanded, path, False, True)		

		return path



def depthFirstSearch(problem):

    """

    Search the deepest nodes in the search tree first.



    Your search algorithm needs to return a list of actions that reaches the

    goal. Make sure to implement a graph search algorithm.



    To get started, you might want to try some of these simple commands to

    understand the search problem that is being passed in:

"""

    #print("Start:", problem.getStartState())

    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))

    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))



    "*** YOUR CODE HERE ***"

    start = problem.getStartState()	# starting coordinates

    startState = (start, 'start')	# starting fringe value

    fringe = util.Stack()

    fringe.push(startState)

    expanded = set()	# set of expanded nodes

    expanded.add(start)

    path = dict()		# path that is being constructed to goal during recursion

    path[start] = []

    solution = search(problem, startState, fringe, expanded, path)

    if (0,0) in solution:

    	return solution[(0,0)]

    else:

    	return []

    #print("paths: ", paths)

    



def breadthFirstSearch(problem):

    """Search the shallowest nodes in the search tree first."""

    "*** YOUR CODE HERE ***"

    start = problem.getStartState()

    pos, count = start

    startState = (start, 'start')

    fringe = util.Queue()

    fringe.push(startState)

    expanded = set()

    path = dict()

    if isinstance(count, int):

    	expanded.add(start)

    	path[start] = []

    else:

    	expanded.add(pos)

    	path[pos] = []

    solution = search(problem, startState, fringe, expanded, path)

    #print (solution[0,0])

    return solution[(0,0)]

    

def uniformCostSearch(problem):

    """Search the node of least total cost first."""

    "*** YOUR CODE HERE ***"

    solution = []

    start = problem.getStartState()

    startState = (start, 'start')

    fringe = util.PriorityQueue()

    #fringe.push(startState, 0)

    expanded = set()

    expanded.add(start)

    path = dict()

    path[start] = []

    solution = search(problem, startState, fringe, expanded, path, True)

    if (0,0) in solution:

    	return solution[(0,0)]

    else:

    	return []



def nullHeuristic(state, problem=None):

    """

    A heuristic function estimates the cost from the current state to the nearest

    goal in the provided SearchProblem.  This heuristic is trivial.

    """

    return 0



def aStarSearch(problem, heuristic=nullHeuristic):

	""" calculates the heuristic for a new state from a tuple

		queue.push((actions, state))

	"""

	def getHeuristic(item):

		actions, state = item

		cost = problem.getCostOfActions(actions)

		heuristicValue = heuristic(state[0], problem) + cost

		return heuristicValue



	solution = []

	start = problem.getStartState()

	startState = (start, 'start')

	state = ([], (start, 'start', 0))

	fringe = util.PriorityQueueWithFunction(getHeuristic)

	expanded = set()

	expanded.add(start)

	path = dict()

	path[start] = []

	solution = search(problem, startState, fringe, expanded, path, False, True)

	if (0,0) in solution:

		return solution[(0,0)]

	else:

		return []





# Abbreviations

bfs = breadthFirstSearch

dfs = depthFirstSearch

astar = aStarSearch

ucs = uniformCostSearch