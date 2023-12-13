from sys import stdin

MAX = 1000
visitado = [0 for i in range(MAX)]
adj = [[] for i in range(MAX)]
n = int()

def main():
    global n, adj
    n = int(stdin.readline())
    while(n != 0):
        flag = 0
        linea = stdin.readline()
        nodos = list(map(int, linea.split()))
        # print(nodos)
        conectarNodos(nodos)
        # print(adj)
        dfs()
        for i in range(n):
            if(visitado[i] != 1):
                flag = 1
        if(flag == 0):
            print("All stations are reachable.")
        else:
            print("There are stations that are unreachable.")
        for i in range(n):
            adj[i].clear()
        n = int(stdin.readline())


def dfsAux(u):
    global visitado
    visitado[u] = 1
    # print(u)

    for v in adj[u]:
        if visitado[v] == 0:
            dfsAux(v)

def dfs():
    global visitado
    for i in range(n):
        visitado[i] = 0
            
    dfsAux(0)

def obtenerDistancia(x0, y0, x1, y1):
    ans = (((x1 - x0)**2) + ((y1 - y0)**2))**2
    return ans

def conectarNodos(nodos):
    global adj
    for i in range(0, len(nodos), 2):
        # print(i)
        if(((i == 0) and (len(adj[i]) < 2)) or (((len(adj[i - (i // 2)]) < 2) and (i != 0)))):
            menor1 = None
            menor2 = None
            # print(i)
            for j in range(0, len(nodos), 2):
                # print("j =", j)
                if((j != i)):
                    if(menor1 == None):
                        menor1 = j
                    elif(menor2 == None):
                        menor2 = j
                    else:
                        if(obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor2], nodos[menor2 + 1]) < obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor1], nodos[menor1 + 1])):
                            menor1, menor2 = menor2, menor1                            
                        elif(obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor2], nodos[menor2 + 1]) == obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor1], nodos[menor1 + 1])):
                            if(nodos[menor2] < nodos[menor1]):
                                # print("Cambio de menores")
                                menor1, menor2 = menor2, menor1
                            elif(nodos[menor2 + 1] < nodos[menor1 + 1]):
                                # print("cambio de menores")
                                menor1, menor2 = menor2, menor1
                        # print("x1", nodos[i])
                        # print("y1", nodos[i + 1])
                        # print("x2", nodos[j])
                        # print("y2", nodos[j + 1])
                        # print("xmenor2", nodos[menor2])
                        # print("ymenor2", nodos[menor2 + 1])
                        # print("distancia j con i", obtenerDistancia(nodos[i], nodos[i + 1], nodos[j], nodos[j + 1]))
                        # print("distancia menor2 con i", obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor2], nodos[menor2 + 1]))
                        if(obtenerDistancia(nodos[i], nodos[i + 1], nodos[j], nodos[j + 1]) < obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor2], nodos[menor2 + 1])):
                            menor2 = j
                        elif(obtenerDistancia(nodos[i], nodos[i + 1], nodos[j], nodos[j + 1]) == obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor2], nodos[menor2 + 1])):
                            # print("entro con: ", i)
                            if(nodos[j] < nodos[menor2]):
                                menor2 = j
                            elif(nodos[j + 1] < nodos[menor2 + 1]):
                                menor2 = j
                        elif(obtenerDistancia(nodos[i], nodos[i + 1], nodos[j], nodos[j + 1]) < obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor1], nodos[menor1 + 1])):
                            menor1, menor2 = j, menor1
                        elif(obtenerDistancia(nodos[i], nodos[i + 1], nodos[j], nodos[j + 1]) == obtenerDistancia(nodos[i], nodos[i + 1], nodos[menor1], nodos[menor1 + 1])):
                            if(nodos[j] < nodos[menor1]):
                                menor2 = menor1
                                menor1 = j
                            elif(nodos[j + 1] < nodos[menor1 + 1]):
                                menor2 = menor1
                                menor1 = j
            # print("menor1" , menor1)
            # print("menor2", menor2)
            if((menor1 != None) and (len(adj[menor1 - (menor1 // 2)]) < 2)):
                if(i == 0):
                    adj[i].append(menor1 - (menor1 // 2))
                    adj[menor1 - (menor1 // 2)].append(i)
                    # print("i == 0\nMenor1")
                    # print(adj[i])
                    # print(adj[menor1 - (menor1 // 2)])
                else:
                    adj[i - (i // 2)].append(menor1 - (menor1 // 2))
                    adj[menor1 - (menor1 // 2)].append(i - (i // 2))
                    # print("i != 0\nMenor1")
                    # print(adj[i - (i // 2)])
                    # print(adj[menor1 - (menor1 // 2)])
            if(((menor2 != None) and (len(adj[menor2 - (menor2 // 2)]) < 2)) and (((i == 0) and (len(adj[i]) < 2)) or ((i != 0) and (len(adj[i - (i // 2)]) < 2)))):
                if(i == 0):
                    adj[i].append(menor2 - (menor2 // 2))
                    adj[menor2 - (menor2 // 2)].append(i)
                    # print("i == 0\nMenor2")
                    # print(adj[i])
                    # print(adj[menor2 - (menor2 // 2)])
                else:
                    adj[i - (i // 2)].append(menor2 - (menor2 // 2))
                    adj[menor2 - (menor2 // 2)].append(i - (i // 2))
                    # print("i != 0\nMenor2")
                    # print(adj[i - (i // 2)])
                    # print(adj[menor2 - (menor2 // 2)])

main()