from sys import stdin
from heapq import heappush,heappop

INF = float('inf')
distBHOF = None
visited = None

def dijkstraComputeDist(G, s, t):
    global distBHOF
    dist = [ INF ]*len(G) ; dist[s] = 0
    pqueue, found = list(), False
    heappush(pqueue, (dist[s], s))
  
    while((len(pqueue) != 0) and (not found)):
        du, u = heappop(pqueue)
        if(u == t):
            found = True
        else:
            if(dist[u] == du):
                for v, duv in G[u]:
                    if(du + duv < dist[v]):
                        dist[v] = du + duv
                        heappush(pqueue, (dist[v], v))

    distBHOF = dist[t]

def dijkstraMarkNodes(G, s, t):
    global visited
    visited = [False for _ in range(len(G))]
    visited[t], visited[s] = True, True
    dist = [ INF ]*len(G) ; dist[s] = 0
    pred = [-1] * len(G)
    pqueue = list()
    heappush(pqueue, (dist[s], s))
  
    while(len(pqueue) != 0):
        du, u = heappop(pqueue)
        if(dist[u] == du):
            for v, duv in G[u]:
                markNode = u
                if(du + duv <= dist[v]):
                    dist[v] = du + duv
                    pred[v] = u
                    heappush(pqueue, (dist[v], v))
                if((du + duv == distBHOF) and (v == t)):
                    while(markNode != s):
                        visited[markNode] = True
                        markNode = pred[markNode]

def dijkstraMarket(G, s, t):
    global distBHOF
    dist = [ INF ]*len(G) ; dist[s] = 0
    pqueue = list()
    heappush(pqueue, (dist[s], s))
  
    while((len(pqueue) != 0)):
        du, u = heappop(pqueue)
        if(dist[u] == du):
            for v, duv in G[u]:
                if((du + duv < dist[v]) and (visited[v] == False)):
                    dist[v] = du + duv
                    heappush(pqueue, (dist[v], v))

    return dist[t]

def main():
    line = stdin.readline()
    while(line != ""):
        inputList = list(map(int, line.split()))
        P = inputList[0]
        R = inputList[1]
        BH = inputList[2] - 1
        OF = inputList[3] - 1
        YH = inputList[4] - 1
        M = inputList[5] - 1
        G = [[] for _ in range(P)]

        for i in range(R):
            u, v, weight = map(int, stdin.readline().split())
            G[u - 1].append((v - 1, weight))
            G[v - 1].append((u - 1, weight))

        if((BH == YH) or (BH == M) or (OF == YH) or (OF == M)):
            print("MISSION IMPOSSIBLE.")
        else:
            dijkstraComputeDist(G, BH, OF)
            dijkstraMarkNodes(G, BH, OF)
            if(visited[YH] != True):
                distMarket = dijkstraMarket(G, YH, M)
                if(distMarket != INF):
                    print(distMarket)
                else:
                    print("MISSION IMPOSSIBLE.")
            else:
                print("MISSION IMPOSSIBLE.")

        line = stdin.readline()

main()