"""
A standard depth-first search implementation puts each node of the graph into one of two categories:
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
    # Keep track of visited nodes
    visited = set()
    # Iniitialize the stack with the start node
    # Stack keeps track of nodes to be explored
    stack = [startNode]
    
    while stack:
        # Take the last node from the stack
        currentNode = stack.pop()
        # Print or process the current node
        print("current node:", currentNode)
    
        if currentNode not in visited:
            # Mark the node as visited
            visited.add(currentNode)
            # Print the visited set
            print("visited set:", visited)
    
            # Add the current node's unvisited neighbors to the stack
            for neighbor in graph[currentNode]:                
                # If the current node's neighbor is not found in the visited set
                if neighbor not in visited:
                    # Add the current node's neighbor to the stack (to be explored)
                    stack.append(neighbor)
                    print("current stack:", stack)

         
            
# step 3: invoke the depth-first search function

# you can invoke "depthFirstSearch" function to perform depth-first search on the graph.

# treat node A as the starting node
depthFirstSearch(graph, 'A')
