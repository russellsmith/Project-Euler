"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

class Node():
    def __init__(self, **kwargs):
        try:
            self.position = kwargs.pop('position')
        except KeyError:
            raise Exception("position argument missing")
        
        if len(self.position) is not 2:
            raise Exception("position argument has invalid length %d, expected 2"%len(self.position))
        
        if not isinstance(self.position[0], (int, long)):
            raise Exception("position argument has invalid values, expected type (int, long)")
        
        if not isinstance(self.position[1], (int, long)):
            raise Exception("position argument has invalid values, expected type (int, long)")
        
        self.__descendants = kwargs.get('descendants', [])
        
        self.value = kwargs.get('value', 0)
        
        # Init ancestors
        self.__calc_ancestors__()
        
        # init score
        self.path_cost = 0
        
        # Init path
        self.path = []
        
    def __calc_ancestors__(self):
        row, col = self.position[0], self.position[1]
        ancestors = []
        
        if row > 0:
            if col > 0:
                ancestors.append((row - 1, col - 1))
            ancestors.append((row - 1, col))
        
        self.__ancestors = ancestors
        
    def descendants(self):
        for d in self.__descendants:
            yield d
            
    def ancestors(self):
        for i in self.__ancestors:
            yield i
            
class Djikstra():
    def __init__(self, **kwargs):
        try:
            self.nodes = kwargs.get('nodes')
            
        except KeyError:
            raise Exception("nodes argument missing")
        
        self.max_node = None
        self.explored = set()
        self.unexplored = set()
        self.to_process = set()
        
        for i in xrange(0, len(self.nodes), 1):
            for j in xrange(0, len(self.nodes[i]), 1):
                self.unexplored.add(self.nodes[i][j])
        
    def start(self):
        nodes = self.nodes
        explored = self.explored
        self.max_node = nodes[0][0]
        self.max_node.path_cost = self.max_node.value
        to_process = self.to_process
        to_process.add(self.nodes[0][0])
        
        
        # While there are nodes to process
        while len(to_process) > 0:
            node = to_process.pop()
            for i in node.ancestors():
                # Grab ancestor
                row, col = i[0], i[1]
                ancestor = nodes[row][col]
                
                # Cost to get to this node is cost to get to ancestor + this nodes cost
                value = node.value + ancestor.path_cost
                
                if value > node.path_cost:
                    # Cost is better than previously calculated
                    path = ancestor.path
                    assert isinstance(path, list)
                    path = path[:]
                    path.append(node.position)
                    node.path = path
                    node.path_cost = value
                    
                    if value > self.max_node.path_cost:
                        self.max_node = node
            for d in node.descendants():
                row, col = d[0], d[1]
                descendant = nodes[row][col]
                to_process.add(descendant)
            
            explored.add(node)
        
        print 'done'

if __name__ == "__main__":
    f = open("files/triangle.txt")
    pyramid = f.readlines()
    max_length = 0
    for i in xrange(0, len(pyramid),1):
        # Split on spaces
        line = pyramid[i]
        pyramid[i] = line.strip().split(' ')
        
        max_length = len(pyramid[i]) if len(pyramid[i]) > max_length else max_length
        
        # Convert all strings to integers
        for j in xrange(0, len(pyramid[i]), 1):
            pyramid[i][j] = int(pyramid[i][j])
            
    
    #Pad each list with 0s up to max_length
    for i in xrange(0, len(pyramid), 1):
        length = len(pyramid[i])
        pyramid[i] += [0]*(max_length-length)
        
    for i in xrange(0, len(pyramid), 1):
        for j in xrange(0, len(pyramid[i]),1):
            value = pyramid[i][j]
            descendants = [(i+1, j), (i+1, j+1)] if i < len(pyramid) - 1 else []
            pyramid[i][j] = Node(position = (i,j), value = value, descendants = descendants)
    
    graph = Djikstra(nodes = pyramid)
    graph.start()
    node = graph.max_node
    print 'Path had max cost of %d' % node.path_cost