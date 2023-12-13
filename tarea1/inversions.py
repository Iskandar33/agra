from sys import stdin
### C - How many inversions?

def main():
    tamaño = int(stdin.readline())
    while(tamaño != 0):
        A = []
        tmp = []
        for i in range(tamaño):
            num = int(stdin.readline())
            A.append(num)
            tmp.append(0)
        #tmp = [0 for _ in range(tamaño)]
        inv = mergesort(A, 0, tamaño, tmp)
        print(inv)
        tamaño = int(stdin.readline())

def mergesort(A, low, high, tmp):
    inv = 0
    if(low + 1 < high):
        mid = low + ((high - low) >> 1)
        inv += mergesort(A, low, mid, tmp)
        inv += mergesort(A, mid, high, tmp)
        inv += merge(A, low, mid, high, tmp)
        #print("inv mergesort: ", inv)
    return inv 

def merge(A, low, mid, high, tmp):
    inv = 0
    #print("low:", low)
    for i in range(low, high):
        tmp[i] = A[i]
    l, r = low, mid
    #print("Tmp:", tmp)
    for n in range(low, high):
        #print("N:", n)
        #print("A[n] : ", A[n])
        if(l == mid):
            A[n] = tmp[r]
            r += 1
            #print("Se acabó izq")
        elif(r == high):
            A[n] = tmp[l]
            l += 1
            #print("Se acabó der")
        else:
            if(tmp[l] <= tmp[r]):
                A[n] = tmp[l]
                #print("Derecha mayor q izquierda")
                #print("der:", tmp[r])
                #print("izq:", tmp[l])
                l += 1
            else:
                A[n] = tmp[r]
                #print("Izquierda mayor q derecha")
                #print("izq:", tmp[l])
                #print("der:", tmp[r])
                #print("mid: ", mid)
                #print("l: ", l)
                inv += mid - l
                #print("inv:", inv)
                r += 1
    #print("inv retorna:", inv)
    return inv

main()
