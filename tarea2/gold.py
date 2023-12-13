from sys import stdin
from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

adj = None
visitado = []
n, col, gold = int(), int(), int()

def dfsAux(playerPos):
    global gold, visitado
    # print(playerPos)
    xP = playerPos[0]
    yP = playerPos[1]
    if((adj[xP][yP] == 'G') and (visitado[xP][yP] != True)):
        gold += 1
    visitado[xP][yP] = True
    if((adj[xP + 1][yP] != 'T') and (adj[xP - 1][yP] != 'T') and (adj[xP][yP + 1] != 'T') and (adj[xP][yP - 1] != 'T')):
        if((xP != n) and (adj[xP + 1][yP] != '#') and (visitado[xP + 1][yP] != True)):
            dfsAux((xP + 1, yP))
        if((xP != 0) and (adj[xP - 1][yP] != '#') and (visitado[xP - 1][yP] != True)):
            dfsAux((xP - 1, yP))
        if((yP != col) and (adj[xP][yP + 1] != '#') and (visitado[xP][yP + 1] != True)):
            dfsAux((xP, yP + 1))
        if((yP != 0) and (adj[xP][yP - 1] != '#') and (visitado[xP][yP - 1] != True)):
            dfsAux((xP, yP - 1))



def dfs(playerPos):
    dfsAux(playerPos)


def solve():
    global n, col
    playerPos = None
    i = 1
    flag = True
    while(flag == True):
        j = 1
        while((flag == True) and (j < col)):
            if(adj[i][j] == 'P'):
                # print(adj[i][j])
                playerPos = (i, j)
                flag = False
                # print(playerPos)
            j += 1
        i += 1
    # print(playerPos)
    dfs(playerPos)


def main():
    global n, col, gold, visitado, adj
    line = stdin.readline()
    while(line != ""):
        gold = 0
        adj = []
        tok = line.split()
        col = int(tok[0])
        n = int(tok[1])
        for i in range(n):
            lineM = stdin.readline()
            adj.append(lineM)
        # print(adj)
        visitado = [[False for _ in range(col)] for l in range(n)]
        # print(visitado)
        solve()
        print(gold)
        line = stdin.readline()
        # print(line)

main()