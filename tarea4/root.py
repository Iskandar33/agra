from sys import stdin, setrecursionlimit
from collections import deque

setrecursionlimit(999999)

G = None
worstRoots = None
n = None
visited = None
radio = None

def dfs(centros):
    global visited
    
    for i in range(len(centros)):
        visited = [0 for _ in range(n)]
        # print("HOLA")
        dfsAux(centros[i], 0)

def dfsAux(u, dist):
    global visited, worstRoots
    # print("nodo: ", u + 1)
    dist += 1
    visited[u] = 1
    for v in G[u]:
        if(visited[v] == 0):
            dfsAux(v, dist)
    # print("nodo: ", u + 1)
    # print("distancia:", dist)
    if((dist > radio)):
        worstRoots.append(u)

def center():
    global hojas
    nivelMax = 0
    nivel = [0 for _ in range(len(G))]
    grado = [len(G[v]) for v in range(len(G))]
    queue = deque()
    nodosCentro = set()

    for i in range(len(G)):
        if grado[i] == 1:
            queue.append(i)

    while len(queue) > 0:
        v = queue.popleft()
        for w in G[v]:
            grado[w] -= 1
            if grado[w] == 1:
                queue.append(w)
                nivel[w] = nivel[v] + 1
                nivelMax = max(nivelMax, nivel[w])
    for i in range(len(G)):
        if nivel[i] == nivelMax:
            nodosCentro.add(i)
    if(len(nodosCentro) == 2):
        radio = nivelMax + 1
    else:
        radio = nivelMax 
#   radio = nivelMax + 1 if len(nodosCentro) == 2 else  nivelMax
    if len(nodosCentro) == 2: 
        diametro = 2 * radio - 1
    else: 
        diametro = 2 * radio

    return radio, diametro, nodosCentro


def main():
    global G, worstRoots, hojas, n, diametro, radio
    line = stdin.readline()
    while(line != ""):
        n = int(line)
        G = [[] for _ in range(n)]
        worstRoots = []
        for i in range(n):
            listaNodos = list(map(int, stdin.readline().split()))
            if(listaNodos[0] == 1 and (listaNodos[1] - 1 not in G[i])):
                G[i].append(listaNodos[1] - 1)
                G[listaNodos[1] - 1].append(i)
            else:
                for j in range(1, len(listaNodos)):
                    if(listaNodos[j] - 1 not in G[i]):
                        G[i].append(listaNodos[j] - 1)
                        G[listaNodos[j] - 1].append(i)

        radio, diametro, nodosCentro = center()
        # print(radio)
        # print(diametro)
        nodosCentroList = list(map(int, nodosCentro))
        nodosCentroList.sort()
        dfs(nodosCentroList)
        print("Best Roots  :", end = " ")
        for j in range(len(nodosCentroList)):
            if(j != len(nodosCentro) - 1):
                print(nodosCentroList[j] + 1, end = " ")
            else:
                print(nodosCentroList[j] + 1)
        
        worstRoots.sort()
        
        print("Worst Roots :", end = " ")
        for j in range(len(worstRoots)):
            if(j != len(worstRoots) - 1):
                print(worstRoots[j] + 1, end = " ")
            else:
                print(worstRoots[j] + 1)

        line = stdin.readline()


main()