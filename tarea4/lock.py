from heapq import heappush,heappop
from sys import stdin
INF = float('inf')

G = None

def prim(G):
    visited = [False for i in range(len(G))]
    c = [ INF ]*len(G) ; c[0] = 0
    p = [-1] * len(G)
    pqueue = list()
    zeroQueue = list()
    heappush(pqueue, (c[0], 0))
    while len(pqueue)!=0:
        du,u = heappop(pqueue)
        visited[u] = True
        if c[u] == du:
            for v,duv in G[u]:
                if not visited[v] and duv<c[v]:
                    if(u == 0):
                        heappush(zeroQueue, (duv, v))
                    else:
                        c[v] = duv
                        p[v] = u
                        heappush(pqueue, (c[v], v))
            if(u == 0):
                duv, v = heappop(zeroQueue)
                c[v] = duv
                p[v] = 0
                heappush(pqueue, (duv, v))

    return c

def computeDists(keys):
    global G
    i = 0
    for i in range(len(keys)):
        arrKey = []
        number = keys[i]
        arrKey.append(number // 1000)
        number = number % 1000
        arrKey.append(number // 100)
        number = number % 100
        arrKey.append(number // 10)
        number = number % 10
        arrKey.append(number // 1)
        # print(arrKey)
        for j in range(i + 1, len(keys)):
            number = keys[j]
            arrKeyTarget = []
            arrKeyTarget.append(number // 1000)
            number = number % 1000
            arrKeyTarget.append(number // 100)
            number = number % 100
            arrKeyTarget.append(number // 10)
            number = number % 10
            arrKeyTarget.append(number // 1)
            # print(arrKeyTarget)
            dist = 0
            dist1 = 0
            dist2 = 0
            for k in range(4):
                dist1 = abs(arrKeyTarget[k] - arrKey[k])
                dist2 = 10 - dist1
                dist += min(dist1, dist2)

            if((i, dist) not in G[j]):
                G[i].append((j, dist))
                G[j].append((i, dist))


def main():
    global G
    cases = int(stdin.readline())
    for i in range(cases):
        input = stdin.readline().split()
        numbers = list(map(int, input))
        n = numbers[0]
        numbers[0] = 0
        G = [[] for _ in range(n + 1)]
        # print(numbers)
        computeDists(numbers)
        # print(G)
        c = prim(G)
        cost = 0
        for j in range(len(c)):
            cost += c[j]
        print(cost)

main()