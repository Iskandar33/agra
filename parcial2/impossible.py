from sys import stdin, setrecursionlimit
visited, disc, fin, time = None, None, None, None
flag = None
sccFlag = None
MAX = 50000

setrecursionlimit(99999999)

def reverse(G):
  ans = [list() for _ in G]
  for u in range(len(G)):
    for v in G[u]:
      ans[v].append(u)
  return ans

def dfs(G, order):
    global visited, disc, fin, time, sccFlag
    ans = list()
    visited, disc, fin, time = list(), list(), list(), 0
    for _ in G:
        visited.append(0)
        disc.append(None)
        fin.append(None)
    i = 0
    while((sccFlag == True) and (i < len(G))):
    # for u in order:
        if(visited[order[i]] == 0):
            ans.append(list())
            dfs_visit(G, order[i], ans[-1])
        if((len(ans) >= 2) and (flag == True)):
            sccFlag = False
        i += 1
    return ans
    
def dfs_visit(G, u, comp):
    global visited, disc, fin, time
    visited[u], disc[u], time = 1, time, time + 1
    comp.append(u)
    for v in G[u]:
        if(visited[v] == 0):
            dfs_visit(G, v, comp)
    visited[u], fin[u], time = 2, time, time + 1

def main():
    global flag, sccFlag
    line = stdin.readline()
    while(line != ""):
        n, m = map(int, line.split())
        adj = [[] for i in range(n)]
        flag = False
        sccFlag = True
        for i in range(m):
            listaNodos = list(map(int, stdin.readline().split()))
            if(listaNodos[0] == 1):
                adj[listaNodos[1] - 1].append(listaNodos[2] - 1)
            else:
                # print(listaNodos)
                # print(listaNodos[1:])
                for j in range(1, listaNodos[0]):
                    adj[listaNodos[j] - 1].append(listaNodos[j + 1] - 1)
                    adj[listaNodos[j + 1] - 1].append(listaNodos[j] - 1)
                    # adj[listaNodos[j] - 1] += [x - 1 for x in listaNodos[1:] if(x - 1 != listaNodos[j] - 1)]
        # print("ADJ:", adj)
        dfs(adj, range(len(adj)))
        flag = True
        tmp = list(zip( [ u for u in range(len(adj)) ], fin))
        tmp.sort(key = lambda x: -x[1])
        order = [x[0] for x in tmp]
        GT = reverse(adj)
        scc = dfs(GT, order)
        # print(scc)
        if(len(scc) == 1):
            print("YES")
        else:
            print("NO")
        line = stdin.readline()

main()