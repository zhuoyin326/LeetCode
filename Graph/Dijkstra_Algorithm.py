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

# Define a function that takes a graph, a source node, and a destination node as arguments
def dijkstra(graph, source, destination):
    # Initialize a dictionary to store the distances of each node from the source
    distances = {}
    # Set the distance of the source node to zero
    distances[source] = 0
    # Initialize a priority queue to store the nodes and their distances
    queue = []
    # Push the source node and its distance to the queue
    heapq.heappush(queue, (0, source))
    # Initialize a set to store the visited nodes
    visited = set()
    # Loop until the queue is empty or the destination node is visited
    while queue and destination not in visited:
        # Pop the node with the smallest distance from the queue
        distance, node = heapq.heappop(queue)
        # Mark the node as visited
        visited.add(node)
        # Loop through the neighbors of the node
        for neighbor in graph[node]:
        # Calculate the distance to the neighbor through the node
            new_distance = distance + graph[node][neighbor]
            # If the neighbor is not visited and its distance is smaller than the current distance, update its distance and push it to the queue
            if neighbor not in visited and (neighbor not in distances or new_distance < distances[neighbor]):
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
    # Return the distance of the destination node if it is reachable, otherwise return infinity
    return distances.get(destination, float('inf'))

# Define an example graph as a dictionary of dictionaries, where each key is a node and each value is another dictionary of its neighbors and their weights
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 5, 'D': 10},
    'C': {'E': 3},
    'D': {'F': 11},
    'E': {'D': 4},
    'F': {}
}

# Test the function with some examples
print(dijkstra(graph, 'A', 'F')) # Output: 18
print(dijkstra(graph, 'C', 'D')) # Output: 7
print(dijkstra(graph, 'E', 'A')) # Output: inf

