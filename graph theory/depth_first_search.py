"""
These are basic steps involved in depth-first search:

1. Initialize a stack to keep track of the vertices to be explored.
2. Choose a starting vertex and mark it as visited.
3. Push the starting vertex onto the stack.
4. While the stack is not empty, repeat steps 5-8.
5. Pop a vertex from the stack and process it.
6. Explore all unvisited neighbors of the current vertex.
7. Mark each unvisited neighbor as visited and push it onto the stack.
8. Repeat steps 5-7 until the stack is empty.

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


# step 2: define the depth-first search function

# create a funciton called "depthFirstSearch" that takes the graph, starting vertex, and visited set 
# as arguments. The visited set will keep track of the visited vertices to avoid revisiting
# them.

# treat the current vertex as the starting vertex for depth-first search
def depthFirstSearch(graph, current, visited):
    # add current vertex into the visited set
    visited.add(current)
    # print or process the current vertex
    print("current vertex:", current)
    print("visited set:", visited)
    
    # Loop through all the neighbors of the current vertex 
    # by accessing the values of the graph dictionary
    for neighbor in graph[current]:
        print("neighbor of the current vertex", current, ":", neighbor, "\n")
        # if the neighbor of the current vertex is not found in the visited set
        if neighbor not in visited:
            # treat this neighbor as the current vertex for depth-first search
            depthFirstSearch(graph, neighbor, visited)
         
            
# step 3: invoke the depth-first search function

# you can invoke "depthFirstSearch" function to perform depth-first search on the graph.

# create an empty set to store visited vertices
visited = set()
# treat vertex A as the starting vertex
depthFirstSearch(graph, 'A', visited)

# All vertices that the depth-first search will visit sequentially
# [A, B, D, E, F, C]