from sys import stdin

#MAX = 100
visited = None
adj = None
inc = None
name, code = list(), dict()
topo = []


def encode(s):
    global name, code
    if s not in code:
        code[s] = len(code)
        name.append(s)
    return code[s]

def topoSort(p):
  global inc, visited, topo
  
  if p < len(adj):
    r, i = -1, 0
    while i < len(adj) and r == -1:
      if visited[i] == 0 and inc[i] == 0: r = i
      i += 1
    if r != -1:
      for v in adj[r]:
        inc[v] -= 1
      visited[r] = 1
      topo.append(r)
      topoSort(p + 1)


def main():
  global adj, topo, visited, inc, name, code
  cont = 0
  line = stdin.readline()
  while(line != ""):
    numberCases = int(line)
    # print("numero de casos:", numberCases)
    name = list()
    code = dict()
    adj = [[] for _ in range(numberCases)]
    topo = []
    visited, inc = [0 for _ in range(numberCases)], [0 for _ in range(numberCases)]
    for i in range(numberCases):
      beverages = stdin.readline().strip()
      # print(beverages)
      encode(beverages)
      # print(beverages)
    numberConnections = int(stdin.readline())
    # print("Conexiones:", numberConnections)
    # print(len(inc))
    for i in range(numberConnections):
      duoBeverages = stdin.readline()
      tok = duoBeverages.split()
      b1 = encode(tok[0])
      b2 = encode(tok[1])
      # print("b2:", b2)
      adj[b1].append(b2)
      inc[b2] += 1
    topoSort(0)
    # print("len de name:", len(name))
    # print(len(topo))
    print("Case #%i: Dilbert should drink beverages in this order:" % (cont + 1), end = '')
    for i in range(len(topo)):
      print(" %s" % name[topo[i]], end = '')
    print('.')
    print()
    cont += 1
    stdin.readline().strip()
    line = stdin.readline()
    

main()