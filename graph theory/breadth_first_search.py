"""

breathFirstSearch is an algorithm used to traverse or search through a graph or tree data structure 
in a breadthward motion.

Here's a step-by-step guide to implementing breathFirstSearch in Python:

"""

# step 1: define the graph representation

# We have an adjacency list representation of the graph. 
# We can represent the graph using a dictionary, where the keys represent the vertices, 
# and the values are lists containing their adjacent vertices.

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# Step 2: Implement the breathFirstSearch algorithm
# Now let's implement the breathFirstSearch algorithm itself. 
# We'll use a queue to keep track of the nodes to visit.

from collections import deque

def breathFirstSearch(graph, start_node):
    # To keep track of visited nodes
    visited = set()  
    # Initialize the queue with the start node
    queue = deque([start_node])  

    while queue:
        # Dequeue the node from the front of the queue
        node = queue.popleft()  
        
        if node not in visited:
            # Mark the node as visited
            visited.add(node)
            # Process or perform any action on the node  
            print(node)  

            # Enqueue all the adjacent nodes that haven't been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# Step 3: Test the breath-first search algorithm
# To see the breath-first search algorithm in action, you can call the breathFirstSearch function with your graph 
# and a starting node.

breathFirstSearch(graph, 'A')
