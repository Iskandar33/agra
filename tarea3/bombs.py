from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

G = None
visited = None
low = None
p = None
pV = None
apNodes = set()
t, n = int(), int()

def ap():
    global low, visited, p
    for i in range(n):
        low[i] = visited[i] = p[i] = -1

    for i in range(n):
        if(visited[i] == -1):
            apAux(i)

def apAux(v):
    global low, visited, p, apNodes, t, pV
    numHijos = 1
    t += 1
    visited[v] = low[v] = t
    for w in G[v]:
        if(visited[w] == -1):
            numHijos += 1
            p[w] = v
            apAux(w)
            low[v] = min(low[v], low[w])

            if((p[v] != -1) and (low[w] >= visited[v])):
                apNodes.add(v)

            elif(p[v] != -1):
                numHijos -= 1
                
        elif(w != p[v]):
            low[v] = min(low[v], visited[w])

    if((p[v] == -1) and (numHijos > 1)):
        apNodes.add(v)
        numHijos -= 1

    pV.append((v, numHijos))


def main():
    global G, n, p, visited, low, pV
    
    n, m = map(int, stdin.readline().split())
    while((n != 0) and (m != 0)):
        G = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        low = [-1 for _ in range(n)]
        p = [-1 for _ in range(n)]
        i = 0
        u, v = map(int, stdin.readline().split())
        pV = list()
        while((u != -1) and (v != -1)):
            G[u].append(v)
            G[v].append(u)
            u, v = map(int, stdin.readline().split())    
        ap()
        pV.sort(key = lambda x: (x[1], x[0] * - 1), reverse = True)
        while(i < m):
            print(pV[i][0], pV[i][1])
            i += 1
        print()
        n, m = map(int, stdin.readline().split())
main()