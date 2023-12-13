from sys import stdin
from collections import deque

# def main():
#     #leer e imprimir inversions

#     tamArray = int(stdin.readline())
#     A = [0 for _ in range(tamArray)]
#     for i in range(tamArray):
#         numAgregar = int(stdin.readline())
#         A[i] = numAgregar
    
#     #leer e imprimir lap
#     linea = int(stdin.readline().split)
#     corredorA, corredorB = linea[0], linea[1]

#main()


### Lap

def lapSearch(corrA, corrB, low, high):
    if(high - low == 1):
        ans = low
    else:
        mid = low + high // 2
        if(((mid * corrB) - (mid * corrA)) == corrB):
            ans = mid
        elif(((mid * corrB) - (mid * corrA)) > corrB):
            lapSearch(corrA, corrB, low, mid)
        else:
            lapSearch(corrA, corrB, mid, high)
    return ans
    


    

### C - How many inversions?


def mergesort(A, low, high):
    inv = 0
    if(low < high):
        mid = (low + high)/2
        mergesort(A, low, mid)
        mergesort(A, mid + 1, high)
        inv += merge(A, low, mid, high)
    return inv


def merge(A, low, mid, high):
    inv = 0
    n1 = mid - low + 1
    n2 = high - mid
    L = [1 for _ in range(n1 + 1)]
    R = [1 for _ in range(n2 + 1)]
    for i in range(1, n1):
        L[i] = A[low + (i - 1)]
    for j in range(1, n2):
        R[j] = A[mid + j]
    L[n1 + 1] = float('inf')
    R[n2 + 1] = float('inf')
    i, j = 1, 1
    for k in range(low, high):
        if(L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            inv = inv + (n1 - i) + 1
    return inv



### A - 10-20-30


#Falta agregar  diccionario para verificar ciclos.
def juegoCartas(deck):
    endGame, win, cardsPlayed = 0, 0, 0
    pile0, pile1, pile2, pile3, pile4, pile5, pile6 = deque(), deque(), deque(), deque(), deque(), deque(), deque()
    i = 0
    while(endGame == 0):
        print("Cartas deck:", len(deck))
        if((len(deck) == 52) and (cardsPlayed >= 15)):
            print("Holi, ganaste")
            endGame = 1
            win = 1
        elif(len(deck) == 0):
            print("adiosito, perdiste")
            endGame = 1
        else:
            if(i == 0):
                print("pila 0")
                actualPile = pile0
            elif(i == 1):
                print("pila 1")
                actualPile = pile1
            elif(i == 2):
                print("pila 2")
                actualPile = pile2
            elif(i == 3):
                print("pila 3")
                actualPile = pile3
            elif(i == 4):
                print("pila 4")
                actualPile = pile4
            elif(i == 5):
                print("pila 5")
                actualPile = pile5
            else:
                print("pila 6")
                actualPile = pile6
            print("pila escogida")
            if((len(actualPile) != 0) or (cardsPlayed < 15)):
                print("Entro a pila")
                nextPile = 0
                card = deck[0]
                deck.popleft()
                cardsPlayed += 1
                actualPile.append(card)
                print("carta puesta")
                print("Cartas jugadas: ", cardsPlayed)
                while(nextPile == 0):
                    for j in range(len(actualPile)):
                        print("Carta: ", actualPile[j])
                    if(len(actualPile) < 3):
                        print("pila no tiene 3 cartas min")
                        nextPile = 1
                    else:
                        pileHead = actualPile[0]
                        pileSecond = actualPile[1]
                        pileLast = actualPile[-1]
                        if((pileHead + pileSecond + pileLast == 10) or (pileHead + pileSecond + pileLast == 20) or (pileHead + pileSecond + pileLast == 30)):
                            print("primer caso de puntos")
                            deck.append(pileHead)
                            deck.append(pileSecond)
                            deck.append(pileLast)
                            actualPile.popleft()
                            actualPile.popleft()
                            actualPile.pop()
                        else:
                            pileHead = actualPile[0]
                            pileLast = actualPile[-1]
                            pileSecondLast = actualPile[-2]
                            if((pileHead + pileSecondLast + pileLast == 10) or (pileHead + pileSecondLast + pileLast == 20) or (pileHead + pileSecondLast + pileLast == 30)):
                                print("segundo caso de puntos")
                                deck.append(pileHead)
                                deck.append(pileSecondLast)
                                deck.append(pileLast)
                                actualPile.popleft()
                                actualPile.pop()
                                actualPile.pop()
                            else:
                                pileLast = actualPile[-1]
                                pileSecondLast = actualPile[-2]
                                pileThirdLast = actualPile[-3]
                                if((pileThirdLast + pileSecondLast + pileLast == 10) or (pileThirdLast + pileSecondLast + pileLast == 20) or (pileThirdLast + pileSecondLast + pileLast == 30)):
                                    print("tercer caso de puntos")
                                    deck.append(pileThirdLast)
                                    deck.append(pileSecondLast)
                                    deck.append(pileLast)
                                    actualPile.pop()
                                    actualPile.pop()
                                    actualPile.pop()
                                else:
                                    print("nada")
                                    nextPile = 1
                        print("fuera puntos")
            i += 1
            if(i == 7):
                i = 0
    if(win == 1):
        print("Win :", cardsPlayed)
    else:
        print("Loss :", cardsPlayed)                        





A = deque([2, 6, 5, 10, 10, 4, 10, 10, 10, 4, 5, 10, 4, 5, 10, 9, 7, 6, 1, 7, 6, 9, 5, 3, 10, 10, 4, 10, 9, 2, 1, 10, 1, 10, 10, 10, 3, 10, 9, 8, 10, 8, 7, 1, 2, 8, 6, 7, 3, 3, 8, 2,])
B = deque([4, 3, 2, 10, 8, 10, 6, 8, 9, 5, 8, 10, 5, 3, 5, 4, 6, 9, 9, 1, 7, 6, 3, 5, 10, 10, 8, 10, 9, 10, 10, 7, 2, 6, 10, 10, 4, 10, 1, 3, 10, 1, 1, 10, 2, 2, 10, 4, 10, 7, 7, 10])
C = deque([10, 5, 4, 3, 5, 7, 10, 8, 2, 3, 9, 10, 8, 4, 5, 1, 7, 6, 7, 2, 6, 9, 10, 2, 3, 10, 3, 4, 4, 9, 10, 1, 1, 10, 5, 10, 10, 1, 8, 10, 7, 8, 10, 6, 10, 10, 10, 9, 6, 2, 10, 10])
juegoCartas(B)