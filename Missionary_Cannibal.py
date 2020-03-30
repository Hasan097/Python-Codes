import collections

def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)

class Problem:
    def __init__(self, initial, goal=0):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        if (state == (3,3,1)):      # if yes, send a missionary and a canniable to land B
            return (2,2,0)
        if (state == (2,2,0)):      # if yes, send a missionary back to land A
            return (3,2,1)
        if (state == (3,2,1)):      # if yes, send a missionary and a canniable to land B
            return (2,1,0)
        if (state == (2,1,0)):      # if yes, send a missionary back to land A
            return (3,1,1)
        if (state == (3,1,1)):      # if yes, send 2 missionary to land B
            return (1,1,0)
        if (state == (1,1,0)):      # if yes, send a missionary and a canniable to land A
            return (2,2,1)
        if (state == (2,2,1)):      # if yes, send 2 missionary to land B
            return (0,2,0)
        if (state == (0,2,0)):      # if yes, send a missionary to land A
            return (1,2,1)
        if (state == (1,2,1)):      # if yes, send a missionary and a canniable to land B
            return (0,1,0)
        if (state == (0,1,0)):      # if yes, send a missionary to land A
            return (1,1,1)
        if (state == (1,1,1)):      # if yes, send a missionary and a canniable to land B
            return (0,0,0)

        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        return self.actions(state)

        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


# ______________________________________________________________________________


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state. Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node. Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next_state = problem.result(self.state, action) 
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):     # Path taken to reach Goal
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_graph_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        # We use the hash value of the state
        # stored in the node instead of the node
        # object itself to quickly search a node
        # with the same state in a Hash Table
        return hash(self.state)


# ______________________________________________________________________________

def breadth_first_graph_search(problem):
    """[Figure 3.11]
    Note that this function can be implemented in a
    single line as below:
    return graph_search(problem, FIFOQueue())
    """
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node
    frontier = collections.deque([node])
    explored = set()
    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)
    return None

def main():
    print("Missionaries and Cannibal Problem")
    print("=================================")
    print("\nEnvironments include: Land A | river with boat | Land B")
    print("Goal: To get both missionaries and cannibals to land B by boat")
    print("Condition: cannibals must be < or = missionaries in all environments")
    print("There are 3 missionaries and cannibals on Land A")

    initial_state = (3,3,1)     #initial state on land A
    goal_state = (0,0,0)        #End state which means all have reached land B safely and the Boat is on Land B

    print("\n(missionaries, cannibals, boat)")
    print("boat = 1 if its on Land A and 0 if its on Land B")
    print("Our initial state: " + str(initial_state))
    print("Our goal state: " + str(goal_state))
    input("Press Enter To Find Path...")

    problem = Problem(initial_state,goal_state)
    end_goal = breadth_first_graph_search(problem)
    print("\nPath Taken:")
    for i in end_goal.path():
        if(i.state == (3,3,1)):
            print("3 Missionaries, 3 Cannibals, Boat on Land A - Initial")
        if(i.state == (2,2,0)):
            print("2 Missionaries, 2 Cannibals, Boat on Land B")
        if(i.state == (3,2,1)):
            print("3 Missionaries, 2 Cannibals, Boat on Land A")
        if(i.state == (2,1,0)):
            print("2 Missionaries, 1 Cannibals, Boat on Land B")
        if(i.state == (3,1,1)):
            print("3 Missionaries, 1 Cannibals, Boat on Land A")
        if(i.state == (1,1,0)):
            print("1 Missionaries, 1 Cannibals, Boat on Land B")
        if(i.state == (2,2,1)):
            print("2 Missionaries, 2 Cannibals, Boat on Land A")
        if(i.state == (0,2,0)):
            print("0 Missionaries, 2 Cannibals, Boat on Land B")
        if(i.state == (1,2,1)):
            print("1 Missionaries, 2 Cannibals, Boat on Land A")
        if(i.state == (0,1,0)):
            print("0 Missionaries, 1 Cannibals, Boat on Land B")
        if(i.state == (1,1,1)):
            print("1 Missionaries, 1 Cannibals, Boat on Land A")
        if(i.state == (0,0,0)):
            print("0 Missionaries, 0 Cannibals, Boat on Land B - Goal")

main()