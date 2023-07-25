"""

Dijkstra's Algorithm is a popular algorithm in graph theory. It was developed by computer scientist 
Edsger W. Dijkstra in 1959. 

This algorithm is used to find the shortest path from a starting node to all other nodes in a graph, 
which may represent, for example, road networks. 

Here are the basic steps of the algorithm:

(1) Set the initial node as the current node.
(2) Set the initial node distance as 0 and for all other nodes set distance as infinity 
(or a sufficiently large value).
(3) For the current node, consider all of its adjacent nodes and calculate their tentative distances through 
the current node.
(4) If the newly calculated tentative distance to an adjacent node is less than its current assigned value, 
update this.
(5) Once all adjacent nodes of the current node have been considered, mark the current node as visited. 
The visited nodes will not be checked again.
(6) If the destination node has been marked visited (when planning a route between two specific nodes) 
or if the smallest tentative distance among the nodes left is infinity (when planning a complete traversal), 
then stop. The algorithm has finished.
(7) Otherwise, select the unvisited node that is marked with the smallest tentative distance and set it as 
the new "current node". Then, go back to step 3.


Below is an example of Dijkstra's Algorithm implemented in Python. We'll use a dictionary 
to represent the graph where each key is a node and the corresponding value is a dictionary 
with neighbouring nodes as keys and the distances to them as values. 

"""

# Import heapq module for priority queue operations
import heapq

# Define a function that takes a graph and a starting node as arguments
def dijkstra(graph, start):
    # Create a dictionary to save the shortest distance of each node from the start node
    shortest_distances = {node: float('infinity') for node in graph}
    # Set the shortest distance of the start node to itself as 0
    shortest_distances[start] = 0
    # Create a tuple for the heap queue: (shortest distance to node, node)
    heap = [(0, start)]
    # Keep a set of nodes processed so far
    processed_nodes = set()

    while heap:
        # Get the node with the smallest distance so far
        (dist, current_node) = heapq.heappop(heap)
        # If we've processed the node already, skip
        if current_node in processed_nodes:
            continue
        # Add the current node to the processed nodes
        processed_nodes.add(current_node)
        # Look at all the neighboring nodes
        for neighbor, distance in graph[current_node].items():
            old_distance = shortest_distances[neighbor]
            new_distance = shortest_distances[current_node] + distance
            # If the new distance is shorter than the old distance, update it
            if new_distance < old_distance:
                shortest_distances[neighbor] = new_distance
                # Add the updated node to the heap
                heapq.heappush(heap, (new_distance, neighbor))

    return shortest_distances  # Dictionary of shortest distances

# Define the graph
graph = {'A': {'B': 1, 'C': 3}, 'B': {'A': 1, 'D': 2}, 'C': {'A': 3}, 'D': {'B': 2}}
print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 3}
