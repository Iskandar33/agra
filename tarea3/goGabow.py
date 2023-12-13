from sys import stdin

MAX = 2000
adj = None
visitado = None
sccInd = None
n, t, numSCC = None, None, None
sccNodos, pilaS, pilaP = None, None, None

def gabow():
    global sccInd, visitado, n
    for i in range(n):
        sccInd[i], visitado[i] = -1, -1
    
    for i in range(n):
        if visitado[i] == -1:
            gabowAux(i)

def gabowAux(v):
    global t, numSCC, adj, sccInd, visitado, sccNodos, pilaP, pilaS
    t += 1
    visitado[v] = t
    pilaS.append(v)
    pilaP.append(v)

    for i in range(len(adj[v])):
        w = adj[v][i]
        if visitado[w] == -1:
            gabowAux(w)
        elif sccInd[w] == -1:
            while visitado[pilaP[-1]] > visitado[w]:
                pilaP.pop()

    if v == pilaP[-1]:
        numSCC += 1
        sccNodos.append([])
        # print("SCC con indice %d: " % numSCC, end = '')
        while pilaS[-1] != v:
            a = pilaS.pop()
            # print("%d " % a, end = '')
            sccInd[a] = numSCC - 1
            sccNodos[numSCC - 1].append(a)

        a = pilaS.pop()
        # print("%d " % a)
        sccInd[a] = numSCC - 1
        sccNodos[numSCC - 1].append(a)
        pilaP.pop()

def main():
    global n, adj, visitado, sccInd, sccNodos, t, numSCC, pilaP, pilaP, pilaS
    n, m = list(map(int, stdin.readline().split()))
    
    while((n != 0) and (m != 0)):
        adj = [[] for i in range(MAX)]
        visitado = [0 for i in range(MAX)]
        sccInd = [-1 for i in range(MAX)]
        t, numSCC = 0, 0
        sccNodos, pilaS, pilaP = [], [], []
        for i in range(m):
            v, w, p = list(map(int, stdin.readline().split()))
            if(p == 2):
                adj[v - 1].append(w - 1)
                adj[w - 1].append(v - 1)
            else:
                adj[v - 1].append(w - 1)
        gabow()

        if(len(sccNodos) == 1):
            print("1")
        else:
            print("0")
        n, m = list(map(int, stdin.readline().split()))


main()
