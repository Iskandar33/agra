from sys import stdin, setrecursionlimit
visited, disc, fin, time = None, None, None, None

setrecursionlimit(99999)


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
    global visited, disc, fin, time
    visited[u], disc[u], time = 1, time, time + 1
    comp.append(u)
    for v in G[u]:
        if(visited[v] == 0):
            dfs_visit(G, v, comp)
    visited[u], fin[u], time = 2, time, time + 1

def main():
    n, m = map(int, stdin.readline().split())
    
    while((n != 0) and (m != 0)):
        adj = [[] for i in range(n)]
        for i in range(m):
            v, w, p = map(int, stdin.readline().split())
            if(p == 2):
                adj[v - 1].append(w - 1)
                adj[w - 1].append(v - 1)
            else:
                adj[v - 1].append(w - 1)
        # print(adj)
        dfs(adj, range(len(adj)))
        tmp = list(zip( [ u for u in range(len(adj)) ], fin))
        tmp.sort(key = lambda x: -x[1])
        order = [x[0] for x in tmp]
        GT = reverse(adj)
        scc = dfs(GT, order)

        if(len(scc) == 1):
            print("1")
        else:
            print("0")
        n, m = map(int, stdin.readline().split())

main()