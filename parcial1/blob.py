from sys import stdin, setrecursionlimit


adj = []
visitado = []
sizes = []
n, col, size = int(), int(), int()

def dfsAux(playerPos):
    global size, visitado, n, col, adj
    xB = playerPos[0]
    yB = playerPos[1]
    visitado[xB][yB] = True
    size += 1
    if((xB + 1 != n) and ((adj[xB + 1][yB] == '1') and (visitado[xB + 1][yB] != True))):
        dfsAux((xB + 1, yB))
    if((xB - 1 != -1) and ((adj[xB - 1][yB] == '1') and (visitado[xB - 1][yB] != True))):
        dfsAux((xB - 1, yB))
    if((yB + 1 != col) and ((adj[xB][yB + 1] == '1') and (visitado[xB][yB + 1] != True))):
        dfsAux((xB, yB + 1))
    if((yB - 1 != -1) and ((adj[xB][yB - 1] == '1') and (visitado[xB][yB - 1] != True))):
        dfsAux((xB, yB - 1))
    if(((xB + 1 != n) and (yB + 1 != col)) and ((adj[xB + 1][yB + 1] == '1') and (visitado[xB + 1][yB + 1] != True))):
        dfsAux((xB + 1, yB + 1))
    if(((xB + 1 != n) and (yB - 1 != -1)) and ((adj[xB + 1][yB - 1] == '1') and (visitado[xB + 1][yB - 1] != True))):
        dfsAux((xB + 1, yB - 1))
    if(((xB - 1 != -1) and (yB + 1 != col)) and ((adj[xB - 1][yB + 1] == '1') and (visitado[xB - 1][yB + 1] != True))):
        dfsAux((xB - 1, yB + 1))
    if(((xB - 1 != -1) and (yB - 1 != -1)) and ((adj[xB - 1][yB - 1] == '1') and (visitado[xB - 1][yB - 1] != True))):
        dfsAux((xB - 1, yB - 1))
    

def dfs(blobStart):
    dfsAux(blobStart)


def solve():
    global n, col, size, visitado, sizes, adj
    for i in range(n):
        for j in range(col):
            if((adj[i][j] == '1') and (visitado[i][j] != True)):
                size = 0
                blobStart = (i, j)
                # print("DFSSSS")
                dfs(blobStart)
                sizes.append(size)


def main():
    global n, col, visitado, adj, sizes
    cases = int(stdin.readline())
    stdin.readline()
    for i in range(cases):
        adj = []
        sizes = []
        visitado = []
        ans = 0
        n = 0
        col = 0
        lineM = stdin.readline().strip()
        # print(lineM)
        while(lineM != ""):
            adj.append(lineM)
            lineM = stdin.readline().strip()
        # print(adj)
        col = len(adj[0])
        n = len(adj)
        # print(n)
        # print(col)
        # print(adj)
        visitado = [[False for _ in range(col)] for l in range(n)]
        # print(visitado)
        # print("SOLVE")
        solve()
        for j in range(len(sizes)):
            # print(sizes[j])
            if(sizes[j] > ans):
                ans = sizes[j]
        # print(visitado)
        # print(sizes)
        print(ans)
        if(i != cases - 1):
            print()
        # print(line)

main()