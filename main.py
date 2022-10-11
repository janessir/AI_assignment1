
import json
import heapq
import math
from multiprocessing import heap

with open("coord.json") as file:
    Coord = json.load(file)
with open("cost.json") as file:
    Cost = json.load(file)
with open("dist.json") as file:
    Dist = json.load(file)
with open("graph.json") as file:
    G = json.load(file)

src = "1"
dest = "50"
ENERGY_BUDGET = 287932

##### TASK 1 #####
def DijkstraTask1():
    numOfV = len(Coord) #finds total number of V
    d = {str(i): float('inf') for i in range(1,numOfV+1)} #d[v]=inf
    pi = {str(i): 0 for i in range(1,numOfV+1)} #pi[v]=null (ie 0)
    S = {str(i):0 for i in range(1,numOfV+1)} #S[v]=0
    
    # set d[src]=0
    d[src]=0
    
    # Initialise the Q
    Q = []
    heapq.heappush(Q, (d[src],src))
    
    while(Q):
        _, u = heapq.heappop(Q) #will get the dictionary pair
        S[u]=1
        for v in G[u]:
            if(S[v] != 1 and (d[v] > (d[u] + Dist[str(u) + "," + str(v)]))):
                d[v] = d[u] + Dist[str(u) + "," + str(v)]
                pi[v] = u
                heapq.heappush(Q, (d[v], v))

    printResultTask1(pi,d)

##### TASK 2 #####

def UCS():
    alr_visited = set([])
    
    # pqueue = PriorityQueue()
    # pqueue.put((0, 0, start))
    pqueue = []
    heapq.heappush(pqueue, (0, 0, src))

    while pqueue:
        # length, weight, path = pqueue.get()
        length, weight, path = heapq.heappop(pqueue)

        if weight <= ENERGY_BUDGET:
            node = path[len(path) - 1]

            if node not in alr_visited:
                alr_visited.add(node)

                if node == dest:
                    path.append(length)
                    path.append(weight)
                    printPathTask2(path[:-2])
                    print()
                    print("Shortest distance: ", path[-2])
                    print("Total energy cost: ", path[-1])
                    return

                for m in G[node]:
                    if m not in alr_visited:
                        x = str(node) + "," + str(m)

                        total_length = length + Dist[x]
                        total_weight = weight + Cost[x]
                        new_path = list(path[:])
                        new_path.append(m)
                        # pqueue.put((total_length, total_weight, new_path))
                        heapq.heappush(pqueue, (total_length, total_weight, new_path))


##### TASK 3 #####
def AStar():

    n = len(G)
    found = False

    g = {str(i): float('inf') for i in range(1,n+1)}
    accCost = {str(i): 0 for i in range(1,n+1)}
    f = {str(i): float('inf') for i in range(1,n+1)}
    visited = {str(i):False for i in range(1,n+1)} 
    parent = {str(i): 'na' for i in range(1,n+1)} 
    pq = []

    #processing starting vertex
    g[src] = 0
    h = heuristic(Coord[src], Coord[dest])
    f[src] = g[src] + h
    accCost[src] = 0
    parent[src] = 'nil'
    heapq.heappush(pq, (f[src], accCost[src], src))

    #while there're nodes to process
    while(len(pq) > 0):

        #pop smallest f value node from pq
        _, _, u = heapq.heappop(pq)

        #Found dest node! 
        #can exit alg and print results
        if u == dest:
            found = True
            break
        
        #skip visited nodes
        if visited[u]:
            continue
        
        #add this node to visited list
        visited[u] = True
        
        #looping thru all adjacet nodes to u
        for v in G[u]:
            #calc accumulated cost from src to v
            cost = accCost[u] + Cost[u + "," + v]
            #considering unvisited v nodes with energy cost within ENERGY_BUDGET
            if visited[v] == False and cost <= ENERGY_BUDGET:

                #calc ev function
                newG = g[u] + Dist[u + "," + v]
                newH = heuristic(Coord[u], Coord[u])
                newF = newG + newH 

                #do relaxation if newF value < f[v] or 
                if newF < f[v] or (newF == f[v] and cost < accCost[v]):
                    #perform relaxation
                    g[v] = newG
                    f[v] = newF
                    parent[v] = u
                    accCost[v] = cost
                    #push v to pq
                    heapq.heappush(pq, (f[v], accCost[v], v))
                

    if found:
        printResultTask3(parent, g, accCost)
    else:
        print("Something went wrong teehee")
                    
def heuristic(uCoord, vCoord):
    return int(math.sqrt( (uCoord[0]-vCoord[0])**2 + (uCoord[1]-vCoord[1])**2 ))

#ADDITIONAL FUNCTIONS#
def printResultTask1(pi,d):
    dest = "50"
    result=[]
    while(pi[dest]!=0):
        result.insert(0,dest)
        dest = pi[dest]
    
    print("Shortest Path for task1:")
    print(str(src),end="")
    for element in result:
        print("->" + (str(element)), end ="")
    print()
    print()
    print("Shortest distance: ",end="")
    print(d["50"])

def printPathTask2(path):
    p = ""
    for i in range(len(path)-1):
        p += str(path[i]) + "->"
    p += '50'
    print("Shortest Path for task2:\n",p)

def printResultTask3(parent, g, accCost):
    result=[]
    temp = dest
    while(parent[temp]!= 'nil'):
        result.insert(0,temp)
        temp = parent[temp]

    print("Shortest Path for task3: ")
    print(src,end="")
    for element in result:
        print("->" + (element), end ="")
    print()
    print()
    print("Shortest distance: ",end="")
    print(g[dest])
    print("Total Energy Cost: " ,end="")
    print(accCost[dest])


########## Driver Code ##########

##### TASK 1 #####
print("------------------------------------------------------------------")
print("TASK1")
print()
DijkstraTask1()
print("------------------------------------------------------------------")

##### TASK 2 #####
print("TASK2")
print()
UCS()
print("------------------------------------------------------------------")

##### TASK 3 #####
print("TASK3")
print()
AStar()
print("------------------------------------------------------------------")

