import json

with open("coord.json") as f:
    Coord = json.load(f)
with open("cost.json") as f:
    Cost = json.load(f)
with open("dist.json") as f:
    Dist = json.load(f)
with open("graph.json") as f:
    G = json.load(f)


        
def DijkstraTask1(Coord,Dist,Cost,G,Source,Destination):
    numOfV = len(Coord) #finds total number of V
    d = {str(i): float('inf') for i in range(1,numOfV+1)} #d[v]=inf
    pi = {str(i): 0 for i in range(1,numOfV+1)} #pi[v]=null (ie 0)
    S = {str(i):0 for i in range(1,numOfV+1)} #S[v]=0
    
    # set d[source]=0
    d[Source]=0
    
    # Initialise the Q
    Q = []
    Q.append(Source)
    
    
    while(Q):
        u= Q.pop(0) #will get the dictionary pair
        S[u]=1
        for v in G[u]:
            if(S[v] != 1 and (d[v] > (d[u] + Dist[str(u) + "," + str(v)]))):
                d[v] = d[u] + Dist[str(u) + "," + str(v)]
                pi[v] = u
                Q = insertQ(Q,d,v)

    printResult(pi,d)
                
            
def insertQ(Q,d,v):
    insert=0
    if len(Q)==0:
        Q.append(v)
        return Q
    else:
        for element in Q:
            if (d[element]<d[v]):
                insert+=1
            else:
                Q.insert(insert,v)
                return Q
    Q.append(v)
    return Q
        
def printResult(pi,d,Source="1",Destination="50"):
    result=[]
    cost=0
    while(pi[Destination]!=0):
        result.insert(0,Destination)
        cost += Cost[str(pi[Destination])+","+str(Destination)]
        Destination = pi[Destination]
    
    # final cost from source to the next node
    cost += Cost[str(Source)+","+str(result[0])]
    
    print("The shortest path for task1 is:")
    print(str(Source),end="")
    for element in result:
        print("->" + (str(element)), end ="")
    print()
    print("Shortest distance:",end="")
    print(d["50"])
    print("Cost of path:"+str(cost))

# starts from here
print("TASK1")
Source="1"
Destination="50"
DijkstraTask1(Coord,Dist,Cost,G,Source,Destination)



