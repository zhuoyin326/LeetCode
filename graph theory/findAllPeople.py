import itertools
from collections import deque
from collections import defaultdict

# Breadth-First Search Code:
firstPerson = 1
# create a set to store the individuals who know the secret
hasSecret = {0, firstPerson}

# define meetings
meetings = [[1,2,5],[2,3,8],[1,5,10],[3,1,3],[1,2,2],[0,3,3],[3,4,2],[1,2,1],[2,3,1]]

# sort the meeting by time: the element at index 2
meetings.sort(key=lambda x:x[2])

print("meetings:", meetings, "\n")

# group by the multiple meetings using the meeting time
groups = itertools.groupby(meetings, key = lambda x:x[2])

	# build a chronological graph for people who know the secret 
for key, group in groups:
	# each node represents a person
    # each link represents whether person 1 and person 2 are hosting a meeting
    graph = defaultdict(list)
    # create a set to store the individuals who know the secret based on the meetings
    currentSecret = set()
	# built a link between person 1 and person 2 if there is a meeting between them
    for person1, person2, time in group:
        graph[person1].append(person2)
        graph[person2].append(person1)
        # if person 1 knows the secret, add person 1 into the currentSet set
        if person1 in hasSecret:
            currentSecret.add(person1)
        # if person 2 knows the secret, add person 2 into the currentSet set
        if person2 in hasSecret:
            currentSecret.add(person2)

		# queue keeps track of people who know the secret
		# each element of the queue is a person who knows the secret
        queue = deque(currentSecret)

        print("currentSecret", queue)
        
        # perform breadth-first search on the graph
        while queue:
            # dequeue the person from the front of the queue
            person = queue.popleft()
            print("person:", person)
            
            print("graph:", graph, "\n")
            
            # enqueue all the people had meetings with the person
            for neighbor in graph[person]:
                # if the person’s neighbor does not know the secret
                if neighbor not in hasSecret:
                    # mark the person’s neighbor as having a secret
                    hasSecret.add(neighbor)
                    # add the adjacent person who knows the secret to the queue
                    queue.append(neighbor)