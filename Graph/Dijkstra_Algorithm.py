"""

Dijkstra's Algorithm is a popular algorithm in graph theory. It was developed by computer scientist 
Edsger W. Dijkstra in 1959. 

This algorithm is used to find the shortest path from a start node to all other nodes in a graph, 
which may represent, for example, road networks. 

Here are the basic steps of the algorithm:

(1) Set the start node as the current node.
(2) Set the start node distance as 0 and for all other nodes set distance as infinity 
(or a sufficiently large value).
(3) For the current node, consider all of its neighbor nodes and calculate their tentative distances through 
the current node.
(4) If the newly calculated tentative distance to a neighbor node is less than its current assigned value, 
update this.
(5) Once all neighbor nodes of the current node have been considered, mark the current node as visited. 
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

# Define a function that takes a graph and a start node as arguments
def dijkstra(graph, startNode):
    # To keep track of visited nodes
    visited = set()
    # Create an empty dictionary to store the shortest distances of each node from the start node
    shortestDistances = {}
    # Iterate over each node in the graph
    for node in graph:
        # Set the start shortest distance for each node to infinity
        shortestDistances[node] = float('infinity')
    # Set the shortest distance of the start node to itself as 0
    shortestDistances[startNode] = 0
    print("Shortest Distances:", shortestDistances)
    # Create a tuple for the priorityQueue queue: (shortest distance to node, node)
    priorityQueue = [(0, startNode)]
    print("Priority Queue", priorityQueue, "\n")

    while priorityQueue:
        # Get the node with the smallest distance so far
        (dist, currentNode) = heapq.heappop(priorityQueue)
        print("current node (popped node)", currentNode, "with smallest distance:", dist)
        # Print priority queue after heap pop
        print("Priority Queue:", priorityQueue)
        # If we've not visited the current node
        if currentNode not in visited:
        # Mark the node as visited
            visited.add(currentNode)
            print("visited set:", visited, "\n")
            
            # Look at all the neighbor nodes
            for neighbor, distance in graph[currentNode].items():
                print("current node:", currentNode, "neighbor:", neighbor, "distance:", distance)
                oldDistance = shortestDistances[neighbor]
                newDistance = shortestDistances[currentNode] + distance
                print("Old Distance:", oldDistance, "New Distance:", newDistance)
                # If the new distance is shorter than the old distance
                if newDistance < oldDistance:
                    # Replace the neighbor's shortest distance with the new distance
                    shortestDistances[neighbor] = newDistance
                    print("Shortest Distances:", shortestDistances, "\n")
                    # Add the current node's neighbor to the priorityQueue
                    heapq.heappush(priorityQueue, (newDistance, neighbor))
                    print("Priority Queue:", priorityQueue, "\n")

    return shortestDistances  # Dictionary of shortest distances

# Define the graph
graph = {'A': {'B': 1, 'C': 3}, 'B': {'A': 1, 'D': 2}, 'C': {'A': 3}, 'D': {'B': 2}}
print(dijkstra(graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 3}
