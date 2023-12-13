from heapq import heappush,heappop
from sys import stdin
from math import sqrt
from collections import deque

INF = float('inf')

G = None
c = None
p = None
habitantsList = None
visited = None

def prim(G):
    global c, p
    visited = [False for i in range(len(G))]
    c = [ INF ]*len(G) ; c[0] = 0
    p = [-1] * len(G)
    pqueue = list()
    heappush(pqueue, (c[0], 0))
    while len(pqueue)!=0:
        du,u = heappop(pqueue)
        visited[u] = True
        if c[u] == du:
            for v,duv in G[u]:
                if not visited[v] and duv<c[v]:
                    if(duv < c[u]):
                        c[v] = c[u]
                    else:
                        c[v] = duv
                    p[v] = u
                    heappush(pqueue, (c[v], v))

def computeDays():
    time, habSum, acum, habAcum = 0, 0, 0, 0
    for i in range(len(c)):
        time = c[i]
        habSum = habitantsList[i]
        acum += time * habSum
        habAcum += habitantsList[i]
    days = (acum) / (habAcum)
    return days


def computeDists(dists):
    global G
    for i in range(len(dists)):
        for j in range(i + 1, len(dists)):
            dist = sqrt(((dists[j][0] - dists[i][0]) ** 2) + ((dists[j][1] - dists[i][1]) ** 2))
            G[i].append((j, dist))
            G[j].append((i, dist))

def main():
    global G, habitantsList
    n = int(stdin.readline())
    i = 1
    while(n != 0):
        G = [[] for _ in range(n)]
        habitantsList = [0 for _ in range(n)]
        dists = []
        for j in range(n):
            x, y, habitants = map(int, stdin.readline().split())
            habitantsList[j] = habitants
            dists.append((x, y))
        computeDists(dists)
        prim(G)
        # print(G)
        # print(c)
        days = computeDays()
        print("Island Group: %i" %i, "Average", end = " ")
        print("{:.2f}".format(days))
        # print(days)
        print()
        i += 1
        n = int(stdin.readline())
main()