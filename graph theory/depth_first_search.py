"""
These are basic steps involved in depth first search:

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


# step 2: define the depth first search function

# create a funciton called "depthFirstSearch" that takes the graph, starting vertex, and visited set 
# as arguments. The visited set will keep track of the visited vertices to avoid revisiting
# them.

def depthFirstSearch(graph, current, visited):
    visited.add(current)
    # print or process the current vertex
    print(current)
    
    for neighbor in graph[current]:
        if neighbor not in visited:
            depthFirstSearch(graph, neighbor, visited)
         
            
# step 3: invoke the depth first search function

# you can invoke "depthFirstSearch" function to perform depth first search on the graph.

# create an empty set to store visited vertices
visited = set()
depthFirstSearch(graph, 'A', visited)

# update code to github