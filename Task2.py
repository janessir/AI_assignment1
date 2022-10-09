import json
from queue import PriorityQueue



def UCS(start, goal, cost, dist, graph):
    alr_visited = set([])
    
    pqueue = PriorityQueue()
    pqueue.put((0, 0, start))

    while pqueue:
        length, weight, path = pqueue.get()

        if weight <= 287932:
            node = path[len(path) - 1]

            if node not in alr_visited:
                alr_visited.add(node)

                if node == goal:
                    path.append(length)
                    path.append(weight)
                    printPath(path[:-2])
                    print("Shortest distance:", path[-2])
                    print("Total energy cost:", path[-1])
                    return

                for m in graph[node]:
                    if m not in alr_visited:
                        x = str(node) + "," + str(m)

                        total_length = length + dist[x]
                        total_weight = weight + cost[x]
                        new_path = list(path[:])
                        new_path.append(m)
                        pqueue.put((total_length, total_weight, new_path))


def printPath(path):
    p = ""
    for i in range(len(path)-1):
        p += str(path[i]) + "->"
    p += '50'
    print("Shortest path: ",p)


if __name__ == "__main__":
    g = open('G.json')
    graph = json.load(g)
    f = open('Dist.json')
    dist = json.load(f)
    c = open('Cost.json')
    cost = json.load(c)
    d=open('Coord.json')
    coord=json.load(d)

    start = "1"
    goal = "50"


    print("\nTask 2 : Uniform Cost Search: ")
    UCS(start, goal, cost, dist, graph)


    g.close()
    f.close()
    c.close()
