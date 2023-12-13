from sys import stdin, setrecursionlimit

setrecursionlimit(999999)

adj = None
montesco = None
capuleto = None
sinFamilia = None
cycleFlag = None
visited = None
ans = None
n = int()

def dfs():
    global visited, montesco, capuleto, cycleFlag, ans
    for i in range(n):
        visited[i] = -1
    
    guardarMontesco, guardarCapuleto = montesco, capuleto
    for i in range(n):
        if(visited[i] == -1):
            guardarMontesco, guardarCapuleto = montesco, capuleto
            dfsAux(i, 0)
            if(cycleFlag == True):
                montesco, capuleto = guardarMontesco, guardarCapuleto
                cycleFlag = False
            ans += max(montesco, capuleto)
            montesco, capuleto = 0, 0

def dfsAux(v, familia):
    global visited, capuleto, montesco, cont, cycleFlag, sinFamilia, ans
    # print("Nodo:", v)
    if(len(adj[v]) == 0):
        montesco += 1
        capuleto += 1
        visited[v] = 2
    else: 
        visited[v] = familia
        if(visited[v] == 0):
            # print("Nodo:", v)
            montesco += 1
        elif(visited[v] == 1):
            capuleto += 1
        for w in adj[v]:
            if(visited[w] == -1):
                if(visited[v] == 0):
                    dfsAux(w, 1)
                else:
                    dfsAux(w, 0)
            elif(visited[w] == visited[v]):
                # print("montesco y me encuentro en:", v, w)
                cycleFlag = True

def main():
    global adj, visited, n, montesco, capuleto, sinFamilia, cycleFlag, componentes, ans
    cases = int(stdin.readline())
    for i in range(cases):
        stdin.readline()
        n = int(stdin.readline())
        montesco = 0
        capuleto = 0
        sinFamilia = 0
        cycleFlag = False
        ans = 0
        adj = [[] for _ in range(n)]
        visited = [-1 for _ in range(n)]
        for j in range(n):
            listaNodos = list(map(int, stdin.readline().split()))
            if((listaNodos[0] == 1) and (listaNodos[1] - 1 < n) and (listaNodos[1] - 1 not in adj[j])):
                adj[j].append(listaNodos[1] - 1)
                adj[listaNodos[1] - 1].append(j)
            else:
                for k in range(1, listaNodos[0] + 1):
                    if((listaNodos[k] - 1 < n) and (listaNodos[k] - 1 not in adj[j])):
                        adj[j].append(listaNodos[k] - 1)
                        adj[listaNodos[k] - 1].append(j)
        # print(adj)
        dfs()
        # print(cycleFlag)
        # print(visited)
        # print("montesco:", montesco)
        # print("capuleto", capuleto)
        # if(cycleFlag == True):
        #     print(sinFamilia)
        # else:
        # if(montesco >= capuleto):
        #     print(montesco)
        # else:
        #     print(capuleto)
        print(ans)

main()