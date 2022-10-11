# A* search alg that gives the shortest feasible patth btw nodes 1 & 50
# shortest path using dijkstra
# Energy constraint using ..
# Heuritstics using euclidean distance heuristics
    #  h = sqrt ( (current_cell.x – goal.x)2 + 
    #             (current_cell.y – goal.y)2 )
# calc g using DP to reduce time taken
# Use heapq as priority q

# with open('graph.json') as json_file:
#     data = json.load(json_file)

# print(data)
# print(type(data))

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
            # found = True
            # break
            return printResult(parent, g, accCost)
        
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
                

    # if found:
    #     printResult(parent, g, accCost)
    # else:
    print("Something went wrong teehee")
                    
def heuristic(uCoord, vCoord):
    return int(math.sqrt( (uCoord[0]-vCoord[0])**2 + (uCoord[1]-vCoord[1])**2 ))
    
def printResult(parent, g, accCost):
    
    result=[]
    temp = dest
    while(parent[temp]!= 'nil'):
        result.insert(0,temp)
        temp = parent[temp]
    
    print("ShortestPath for task3: ")
    print(src,end="")
    for element in result:
        print("->" + (element), end ="")
    print()

    print("Shortest distance: ",end="")
    print(g[dest])

    print("Total Energy Cost: " ,end="")
    print(accCost[dest])



AStar()
