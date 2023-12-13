from sys import stdin, setrecursionlimit

setrecursionlimit(99999)

G = None
visited = None
low = None
p = None
bridgesSet = None
bridgesArray = None
arrayCont = None
ans = None
t, n = int(), int()


def bridgesTarjan():
    global low, visited, p
    for i in range(n):
        low[i] = visited[i] = p[i] = -1

    for i in range(n):
        if visited[i] == -1:
            bridgesAux(i)


def bridgesAux(v):
    global low, visited, p, bridgesSet, t, bridgesArray
    t += 1
    visited[v] = low[v] = t

    for w in G[v]:
        if(visited[w] == -1):
            p[w] = v
            bridgesAux(w)
            low[v] = min(low[v], low[w])

            if(low[w] > visited[v]):
                bridgesArray[v].append(w)
                bridgesArray[w].append(v)
                bridgesSet.add((v, w))
                
        elif(w != p[v]):
            low[v] = min(low[v], visited[w])


def dfs():
    cont = 0
    for i in range(n):
        visited[i] = -1

    for i in range(n):
        if(visited[i] == -1):
            dfsAux(i, cont)
        cont += 1


def dfsAux(v, cont):
    global ans, arrayCont
    visited[v] = 1
    arrayCont[v] = cont
    for w in bridgesArray[v]:
        if(visited[w] == -1):
            dfsAux(w, cont)


def main():
    global G, n, visited, low, p, bridgesArray, bridgesSet, arrayCont
    
    r, c, q = map(int, stdin.readline().split())
    while((r != 0) and (c != 0) and (q != 0)):
        n = r
        G = [[] for _ in range(r)]
        visited = [False for _ in range(r)]
        low = [-1 for _ in range(r)]
        p = [-1 for _ in range(r)]
        bridgesArray = [[] for _ in range(r)]
        bridgesSet = set()
        arrayCont = [-1 for _ in range(r)]

        for i in range(c):
            u, v = map(int, stdin.readline().split())
            G[u - 1].append(v - 1)
            G[v - 1].append(u - 1)
        
        bridgesTarjan()
        dfs()
        
        for i in range(q):
            s, t = map(int, stdin.readline().split())
            if(arrayCont[s - 1] == arrayCont[t - 1]):
                print("Y")
            else:
                print("N")
        r, c, q = map(int, stdin.readline().split())
        print("-")
main()