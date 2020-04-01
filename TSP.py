import random

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

        if state == 1:
            return city_dictionary[1]
        if state == 2:
            return city_dictionary[2]
        if state == 3:
            return city_dictionary[3]
        if state == 4:
            return city_dictionary[4]
        if state == 5:
            return city_dictionary[5]
        if state == 6:
            return city_dictionary[6]
        if state == 7:
            return city_dictionary[7]
        if state == 8:
            return city_dictionary[8]
        if state == 9:
            return city_dictionary[9]
        if state < 1 or state > 9:
            print("Error: Unknown city " + str(state))
            
        raise NotImplementedError

    def result(self, state):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        return self.actions(self,state)

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

# A dictionary that holds combinations and distances. City A: (city A, city B, distance between them)
city_dictionary = {  
    1: ((1,2,2),(1,3,11),(1,4,3),(1,5,18),(1,6,14),(1,7,20),(1,8,12),(1,9,5)),
    2: ((2,1,2),(2,3,13),(2,4,10),(2,5,5),(2,6,3),(2,7,8),(2,8,20),(2,9,17)),
    3: ((3,2,13),(3,1,11),(3,4,5),(3,5,19),(3,6,21),(3,7,2),(3,8,5),(3,9,8)),
    4: ((4,2,10),(4,3,5),(4,1,3),(4,5,6),(4,6,4),(4,7,12),(4,8,15),(4,9,1)),
    5: ((5,2,5),(5,3,19),(5,4,6),(5,1,18),(5,6,12),(5,7,6),(5,8,9),(5,9,7)),
    6: ((6,2,3),(6,3,21),(6,4,4),(6,5,12),(6,1,14),(6,7,19),(6,8,7),(6,9,4)),
    7: ((7,2,8),(7,3,2),(7,4,12),(7,5,6),(7,6,19),(7,1,20),(7,8,21),(7,9,13)),
    8: ((8,2,20),(8,3,5),(8,4,15),(8,5,9),(8,6,7),(8,7,21),(8,1,12),(8,9,6)),
    9: ((9,2,17),(9,3,8),(9,4,1),(9,5,7),(9,6,4),(9,7,13),(9,8,6),(9,1,5)),
}

def genetic_algorithm(city_dictionary, start, cities):                      # Genetic algorithm
    """[Figure 4.8]"""
    rout = []               # Datatype that holds the path the salesman will take
    rout.append(start)      # starting city
    path_cost = 0           # initial path cost variable
    salesman_pos = start    # indiactes the city the salesman is in

    while True:                     # loop till all cities are visited
        path_cost = path_cost + fitness_func(salesman_pos, rout)
        salesman_pos = rout[-1]     # new postion of salesman is updated here

        if len(rout) == 9:
            break
    
    return rout,path_cost


def fitness_func(city, rout):                                           # Fitness fuction
    
    cities_visited = 0

    for i in range (1,9):
        if i not in rout:
            break
        else:
            cities_visited += 1
    
    if cities_visited == 8:                                             # check if all cities have been visited then send 
        return 0

    else:
        combos = tuple(Problem.result(self=Problem,state=city))            # return every possible combination of selected city
        smallest = 50000
        pos = 0

        for i in range(len(combos)):
            if combos[i][2] <= smallest and combos[i][1] not in rout:            # Check if the distance is smaller and city is not in visited
                smallest = combos[i][2]
                pos = i
        
        rout.append(combos[pos][1])

        print("From " + str(city) + " to " + str(combos[pos][1]) + " is " + str(smallest) + " units.")
        return smallest
        

def main():
    the_cost = []
    path_dictionary = {}

    print("Travelling salesman problem")
    print("All possible paths and their costs\n")
    
    for i in range(1,10):          # A loop to initialize a start and end state for all cities. 
        Problem(i,i)
        print("Start City: " + str(i))
        path,cost = genetic_algorithm(city_dictionary,i,9)
        the_cost.append(cost)
        path_dictionary[cost] = path
        print("Path: " + str(path))
        print("A total of " + str(cost) + " units to get to all of the above cities\n")

    best_cost = min(the_cost)
    print("\nBest Cost: " + str(best_cost))
    print("Best Path: " + str(path_dictionary[best_cost]))

main()