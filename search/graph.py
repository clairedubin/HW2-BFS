import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if start not in self.graph.nodes():
            raise Exception("Node {} not in graph.".format(start))
        
        if end and end not in self.graph.nodes():
            raise Exception("Node {} not in graph.".format(end))
        
        #queue format: (node, distance)
        q = [(start,[])]
        visited = []
        
        while len(q) > 0:
            curr_node, curr_path = q.pop(0)
            if curr_node in visited:
                continue
            if curr_node == end:
                return curr_path + [curr_node]
            q += self.get_children(curr_node, curr_path)
            visited += [curr_node]

        if len(q) == 0 and not end:
            return visited
        
        #no path exists form start to end
        if len(q) == 0 and end:
            return
        
    def get_children(self, node, curr_path):
        """Returns list of tuples of child nodes and their distance from the start node """

        return [(i,curr_path+[node]) for i in self.graph.neighbors(node)]



