"""
A standard DFS implementation puts each node of the graph into one of two categories:
1. Visited
2. Not Visited

These are basic steps involved in depth-first search:
1. Initialize a stack to keep track of the nodes to be explored.
2. Choose a starting node and mark it as visited.
3. Push the starting node onto the stack.
4. While the stack is not empty, repeat steps 5-8.
5. Pop a node from the stack and process it.
6. Explore all unvisited neighbors of the current node.
7. Mark each unvisited neighbor as visited and push it onto the stack.
8. Repeat steps 5-7 until the stack is empty.

"""


# step 1: define the graph representation

# We have an adjacency list representation of the graph. 
# We can represent the graph using a dictionary, where each key represents a node, 
# and the value is a list of its adjacent nodes.

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


# step 2: define the depth-first search function

# create a funciton called "depthFirstSearch" that takes the graph and starting node as 
# arguments. The visited set will keep track of the visited nodes to avoid revisiting them.

def depthFirstSearch(graph, startNode):
    # keep track of visited nodes
    visited = set()
    # iniitialize the stack with the start node
    stack = [startNode]
    
    while stack:
        # take the last node from the stack
        currentNode = stack.pop()
        # print or process the current node
        print("current node:", currentNode)
    
        if currentNode not in visited:
            # add current node into the visited set
            visited.add(currentNode)
            # print the visited set
            print("visited set:", visited)
    
            # add the unvisited neighbors of the current node to the stack
            for neighbor in graph[currentNode]:                
                # if the neighbor of the current node is not found in the visited set
                if neighbor not in visited:
                    stack.append(neighbor)
                    print("current stack:", stack)

         
            
# step 3: invoke the depth-first search function

# you can invoke "depthFirstSearch" function to perform depth-first search on the graph.

# treat node A as the starting node
depthFirstSearch(graph, 'A')

# All nodes that the depth-first search will visit sequentially
# [A, B, D, E, F, C]