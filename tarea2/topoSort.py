"""
Implementación Algoritmo Orden Topológico
Agosto 17 de 2023

"""

from sys import stdin

G, topo = None, []
visited, inc = None, None

def topoSort(p):
  global inc, visited, topo
  
  if p < len(G):
    r, i = -1, 0
    while i < len(G) and r == -1:
      if visited[i] == 0 and inc[i] == 0: r = i
      i += 1
    if r != -1:
      for v in G[r]:
        inc[v] -= 1
      visited[r] = 1
      topo.append(r)
      topoSort(p + 1)

def main():
  global G, visited, inc, topo
  n, m = list(map(int, stdin.readline().split()))

  G, topo = [[] for _ in range(n)], []
  visited, inc = [0 for _ in range(n)], [0 for _ in range(n)]

  for i in range(n):
    A = list(map(int, stdin.readline().split()))
    c= A[0]
    for j in range(c):
      G[i].append(A[j + 1])
      inc[A[j + 1]] += 1

  print(G, inc)

  print("Grafo")
  for i in range(n):
    print("Nodo %d:" % i)
    for j in range(len(G[i])):
      print("%d" % G[i][j], end = ' ')
    print("")

  print("Ordenamiento Topológico:")
  topoSort(0)
  print(*topo)
  print(topo)
  #for i in range(n - 1, -1, -1):
      #print("%d" % topo[i], end = ' ')
  #print("")

main()