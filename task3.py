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

src = '1'
dest = '50'

def AStar(G, Coord, Dist, Cost):

    n = len(G)

    g = [Inf for _ in range(n)]
    f = [Inf for _ in range(n)]
    visited = [False for _ in range(n)]
    pq = []
    parent = ['na' for _ in range(n)]
    accCost = []

    #processing starting vertex
    g[src] = 0
    sCoord = Coord[src]
    dCoord = Coord[dest]
    h = math.sqrt( (sCoord[0]-dCoord[0])**2 + (sCoord[1]-dCoord[1])**2 )
    f[src] = g[src] + h
    heapq.heappush(pq, (f[src], 0, src));

    #while there're nodes to process
    while(len(pq) > 0):

        #pop smallest f value node u from pq
        _, _, u = heapq.heappop(pq)

        if u == dest:
            break

        if visited[u]:
            continue
        
        visited[u] = True
        
        for v in G[u]:
            cost = 
            if visited[v] == False and :
                visited[v] = True
                g = g[u] + Dist[u + "," + v]
                
                #calc heuristic dynamically when needed 
                uCoord = Coord[u]
                vCoord = Coord[v]
                h = math.sqrt( (uCoord[0]-vCoord[0])**2 + (uCoord[1]-vCoord[1])**2 )
                
                f = g + h

                if f < f[v]:
                    #do relaxation
                    g[v] = g
                    f[v] = f
                    parent[v] = u
                    heapq.heappush(pq, (f[v], Cost[u + "," + v]))
                    





        


    
