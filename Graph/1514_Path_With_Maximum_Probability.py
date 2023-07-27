"""
Joe’s code problem on July 22th, 2023

Title: 1514. Path with Maximum Probability
Tag: Array, Graph, Heap (Priority Queue), Shortest Path
Difficulty: Medium

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

Example 1:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:
Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:
Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 
Constraints:
2 <= n <= 104
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*104
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.


"""
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], 
                       succProb: List[float], start: int, end: int) -> float:
        # Create an empty dictionary to store the graph
        graph = defaultdict(list)
        
        # Iterate over edges to create the graph. We also store the probabilities in the graph.
        for i, edge in enumerate(edges):
            graph[edge[0]].append((edge[1], succProb[i]))
            graph[edge[1]].append((edge[0], succProb[i]))
        
        # Initialize the max probabilities for each node with 0
        maxProb = [0.0] * n
        # The max probability of start node is 1
        maxProb[start] = 1.0
        
        # Initialize the priority queue using a min heap, and push the start node into it
        priorityQueue = [(-1.0, start)]    
        
        # While the priority queue is not empty
        while priorityQueue:
            # Pop the current node with max probability (negative smallest probability) from the priority queue
            # Pop the max probability of the current node from the priority queue
            currentProb, currentNode = heapq.heappop(priorityQueue)
            
            # If the node is the end node
            if currentNode == end:
                # Then we have found the max probability path
                return -currentProb
            
            # Iterate over the neighbors of the current node
            for neighborNode, pathProb in graph[currentNode]:
                
                # If we can reach the neighbor with larger probability
                if -currentProb * pathProb > maxProb[neighborNode]:
                    # Substitute the neighbor's max probability with the new probability
                    maxProb[neighborNode] = -currentProb * pathProb
                    # Push the new probability and neighbor node into the priority queue
                    heapq.heappush(priorityQueue, (-maxProb[neighborNode], neighborNode))
                    
        # If there is no path from start to end, return 0
        return 0.0