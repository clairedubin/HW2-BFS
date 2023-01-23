# write tests for bfs
import pytest
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph('data/tiny_network.adjlist')
    marina_traverse = g.bfs("Marina Sirota")

    #check that all nodes are visited once
    assert(len(marina_traverse)==30), "All nodes should be visited once"
    assert(len(set(marina_traverse)) == 30), "All nodes should be visited once"

    #check that exception is raised for a start node not in the graph
    with pytest.raises(Exception):
        assert(g.bfs('Fake Node')), "Start node not in tree should raise exception"
        


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    g = graph.Graph('data/citation_network.adjlist')

    #correct example shortest path
    correct_path = ['Nadav Ahituv', '32728249', 'Yin Shen', '33545030', 'Tony Capra'] 
    assert g.bfs('Nadav Ahituv', 'Tony Capra') == correct_path, "Shortest path is incorrect"

    #nodes that are not connected
    assert g.bfs('34550967', '34321313') == None, "Unconnected nodes should return None"

    #end node not in tree - raises exception
    with pytest.raises(Exception):
        assert g.bfs('34550967', 'fake end node'), "End node not in tree should raise exception"



