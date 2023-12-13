from sys import stdin, setrecursionlimit

setrecursionlimit(99999)


G = None
visited, disc, fin, time = None, None, None, None
forward = None
flag = None


def reverse(G):
    ans = [list() for _ in G]
    for u in range(len(G)):
        for v in G[u]:
            ans[v].append(u)
    return ans


def dfs(G, order):
    global visited, disc, fin, time
    ans = list()
    visited, disc, fin, time = list(), list(), list(), 0
    for _ in G:
        visited.append(0)
        disc.append(None)
        fin.append(None)
    for u in order:
        if(visited[u] == 0):
            ans.append(list())
            dfs_visit(G, u, ans[-1])

    return ans
    

def dfs_visit(G, u, comp):
    global visited, disc, fin, time, forward
    visited[u], disc[u], time = 1, time, time + 1
    comp.append(u)
    for v in G[u]:
        if(visited[v] == 0):
            dfs_visit(G, v, comp)
        elif((visited[v] == 2) and (flag == True)):
            forward = True
    visited[u], fin[u], time = 2, time, time + 1
    

def main():
    global G, n, p, visited, low, ans, forward, flag
    
    numberCases = int(stdin.readline())
    for i in range(numberCases):
        n = int(stdin.readline())
        ans = True
        G = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        low = [-1 for _ in range(n)]
        p = [-1 for _ in range(n)]
        m = int(stdin.readline())
        forward = False
        flag = True
        for j in range(m):
            u, v = map(int, stdin.readline().split())
            G[u].append(v)    
        dfs(G, range(len(G)))
        tmp = list(zip( [ u for u in range(len(G)) ], fin))
        tmp.sort(key = lambda x: -x[1])
        order = [x[0] for x in tmp]
        GT = reverse(G)
        flag = False
        scc = dfs(GT, order)
        # print(forward)
        # print(len(scc))
        if((forward == False) and (len(scc) == 1)):
            print("YES")
        else:
            print("NO")
main()