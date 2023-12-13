from sys import stdin, setrecursionlimit
from fractions import Fraction

setrecursionlimit(1000000)
MAX = 100000
visitado = [0 for i in range(MAX)]
adj = [[] for i in range(MAX)]
name, code = list(), dict()

def encode(s):
    global name, code
    if s not in code:
        code[s] = len(code)
        name.append(s)
    return code[s]

def solve(c0, c1):
    ans = None
    tupleAns = dfs(c0, c1)
    ans = tupleAns[0]
    # print(ans)
    return ans

def dfsAux(node, goal, saveAns, base):
    global visitado
    visitado[node] = 1
    flag = 0
    ans = saveAns
    for tuple in adj[node]:
        if(tuple[0] == goal):
            ans *= tuple[-1]
            flag = 1
            visitado[tuple[0]] = 1
    if(flag == 0):
        for tuple in adj[node]:
            if((visitado[tuple[0]] == 0) and (flag == 0)):
                # print("ans antes de mult = ", ans)
                # print("valor a mult: ", tuple[-1])
                ans *= tuple[-1]
                # print("valor después de multiplicar = ", ans)
                (ans, flag) = dfsAux(tuple[0], goal, ans, base)
                if(flag == 0):
                    visitado[tuple[0]] = 0
                    # print("Se reinicio ans")
                    # print("save ans:", saveAns)
                    ans = saveAns
                
    return (ans, flag)

def dfs(node, goal):
    global visitado
    for i in range(len(name)):
        visitado[i] = 0
    ans = 1
    base = node
    ans = dfsAux(node, goal, ans, base)
    return ans

def main():
    line = stdin.readline()
    while(len(line) > 2):
        tok = line.split()
        if(tok[0][0] == '!'):
            v0, c0, v1, c1 = int(tok[1]), encode(tok[2]), int(tok[4]), encode(tok[5])
            adj[c0].append((c1, Fraction(v1, v0)))
            adj[c1].append((c0, Fraction(v0, v1)))
            # a = Fraction(v1, v0)
            # b = Fraction(v0, v1)
            # print("guardado.")
            # print(a.denominator, name[c0], "=", name[c1], a.numerator)
            # print(b.denominator, name[c1], "=", name[c0], b.numerator)
            # print("fin guardado.")
        else:
            c0, c1 = encode(tok[1]), encode(tok[3])
            ans = solve(c0, c1)
            value0, value1 = ans.denominator, ans.numerator
            if(visitado[c1] == 1):
                print(value0, name[c0], "=", value1, name[c1])
            else:
                print("?", name[c0], "= ?", name[c1])

        line = stdin.readline()
    # print(code)
    # print(name)
    # print(adj)
    # print(ans)


#ord('5') - ord('0')

main()