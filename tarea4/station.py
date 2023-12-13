from heapq import heappush,heappop
from sys import stdin
INF = float('inf')

stations = None

def dijkstraStations(G):
    dist = [ INF ]*len(G) 
    pred = [-1] * len(G)
    pqueue = list()
    for station in stations:
        dist[station] = 0
        heappush(pqueue, (dist[station], station))

    while(len(pqueue) != 0):
        du, u = heappop(pqueue)
        if(dist[u] == du):
            for v, duv in G[u]:
               if(du + duv < dist[v]):
                    dist[v] = du + duv
                    pred[v] = u
                    heappush(pqueue, (dist[v], v))

    return dist

def dijkstra(G, s):
    dist = [ INF ]*len(G) ; dist[s] = 0
    pred = [-1] * len(G)
    pqueue = list()
    heappush(pqueue, (dist[s], s))
    for station in stations:
        dist[station] = 0
        heappush(pqueue, (dist[station], station))

    while(len(pqueue) != 0):
        du, u = heappop(pqueue)
        if(dist[u] == du):
            for v, duv in G[u]:
               if(du + duv < dist[v]):
                    dist[v] = du + duv
                    pred[v] = u
                    heappush(pqueue, (dist[v], v))

    return dist

def main():
    global stations

    cases = int(stdin.readline())
    stdin.readline()
    for k in range(cases):
        f, i = map(int, stdin.readline().split())
        G = [[] for _ in range(i)]
        stations = []

        for j in range(f):
            stations.append(int(stdin.readline()) - 1)

        line = stdin.readline()
        while(line != '\n' and line != ""):
            u, v, weight = map(int, line.split())
            G[u - 1].append((v - 1, weight))
            G[v - 1].append((u - 1, weight))
            line = stdin.readline()

        stationsDistance = dijkstraStations(G)
        maxStationDist = max(stationsDistance)
        node = 0
        for j in range(i):
            interList = dijkstra(G, j)
            maxInterDist = max(interList)
            if(maxInterDist < maxStationDist):
                node = j
                maxStationDist = maxInterDist
        print(node + 1)
        if(k != cases - 1):
            print()
main()