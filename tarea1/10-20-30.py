from collections import deque
from sys import stdin

def main():
    mazo = deque(map(int, stdin.readline().split()))
    while(mazo[0] != 0):
        if(len(mazo) != 52):
            mazo = mazo + deque(map(int, stdin.readline().split()))
        else:
            juegoCartas(mazo)
            mazo = deque(map(int, stdin.readline().split()))

def juegoCartas(deck):
    endGame, win, cardsPlayed = 0, 0, 0
    cardsPile = []
    states = set()
    for l in range(7):
        pile = deque()
        cardsPile.append(pile)
    i = 0
    while(endGame == 0):
        #print("Cartas deck:", len(deck))
        if((len(cardsPile[i]) != 0) or (cardsPlayed < 15)):
            #print("Entro a pila")
            nextPile = 0
            card = deck[0]
            deck.popleft()
            cardsPlayed += 1
            cardsPile[i].append(card)
            #print("carta puesta")
            #print("Cartas jugadas: ", cardsPlayed)
            while(nextPile == 0):
                # for j in range(len(cardsPile[i])):
                #     print("Carta: ", cardsPile[i][j])
                if(len(cardsPile[i]) < 3):
                    #print("pila no tiene 3 cartas min")
                    nextPile = 1
                else:
                    pileHead = cardsPile[i][0]
                    pileSecond = cardsPile[i][1]
                    pileLast = cardsPile[i][-1]
                    if((pileHead + pileSecond + pileLast) % 10 == 0):
                        #print("primer caso de puntos")
                        deck.append(pileHead)
                        deck.append(pileSecond)
                        deck.append(pileLast)
                        cardsPile[i].popleft()
                        cardsPile[i].popleft()
                        cardsPile[i].pop()
                    else:
                        pileHead = cardsPile[i][0]
                        pileLast = cardsPile[i][-1]
                        pileSecondLast = cardsPile[i][-2]
                        if((pileHead + pileSecondLast + pileLast) % 10 == 0):
                            #print("segundo caso de puntos")
                            deck.append(pileHead)
                            deck.append(pileSecondLast)
                            deck.append(pileLast)
                            cardsPile[i].popleft()
                            cardsPile[i].pop()
                            cardsPile[i].pop()
                        else:
                            pileLast = cardsPile[i][-1]
                            pileSecondLast = cardsPile[i][-2]
                            pileThirdLast = cardsPile[i][-3]
                            if((pileThirdLast + pileSecondLast + pileLast) % 10 == 0):
                                #print("tercer caso de puntos")
                                deck.append(pileThirdLast)
                                deck.append(pileSecondLast)
                                deck.append(pileLast)
                                cardsPile[i].pop()
                                cardsPile[i].pop()
                                cardsPile[i].pop()
                            else:
                                #print("nada")
                                nextPile = 1
                    #print("fuera puntos")
            if((len(deck) == 52) and (cardsPlayed >= 15)):
                #print("Holi, ganaste")
                endGame = 1
                win = 1
            elif(len(deck) == 0):
                #print("adiosito, perdiste")
                endGame = 1
            elif(cardsPlayed > 14):
                tupleOfPiles = tuple(tuple(pile) for pile in cardsPile) + (tuple(deck),)
                #print("tupla: ", tupleOfPiles)
                if(tupleOfPiles in states):
                    #print("Empateeeeeeeee")
                    win = -1
                    endGame = 1
                else:
                    states.add(tupleOfPiles)
        i += 1
        if(i == 7):
            i = 0
    if(win == 1):
        print("Win :", cardsPlayed)
    elif(win == -1):
        print("Draw:", cardsPlayed)
    else:
        print("Loss:", cardsPlayed)                        




main()
# A = deque([2, 6, 5, 10, 10, 4, 10, 10, 10, 4, 5, 10, 4, 5, 10, 9, 7, 6, 1, 7, 6, 9, 5, 3, 10, 10, 4, 10, 9, 2, 1, 10, 1, 10, 10, 10, 3, 10, 9, 8, 10, 8, 7, 1, 2, 8, 6, 7, 3, 3, 8, 2,])
# B = deque([4, 3, 2, 10, 8, 10, 6, 8, 9, 5, 8, 10, 5, 3, 5, 4, 6, 9, 9, 1, 7, 6, 3, 5, 10, 10, 8, 10, 9, 10, 10, 7, 2, 6, 10, 10, 4, 10, 1, 3, 10, 1, 1, 10, 2, 2, 10, 4, 10, 7, 7, 10])
# C = deque([10, 5, 4, 3, 5, 7, 10, 8, 2, 3, 9, 10, 8, 4, 5, 1, 7, 6, 7, 2, 6, 9, 10, 2, 3, 10, 3, 4, 4, 9, 10, 1, 1, 10, 5, 10, 10, 1, 8, 10, 7, 8, 10, 6, 10, 10, 10, 9, 6, 2, 10, 10])
# D = deque([10, 5, 4, 3, 5, 7, 10, 8, 2, 3, 9, 10, 8, 4, 5, 1, 7, 6, 7, 2, 6, 9, 10, 2, 3 ,10, 3, 4, 4, 9, 10, 1, 1, 10, 5, 10, 10, 1, 8, 10, 7, 8, 10, 6, 10, 10, 10, 9, 6, 2, 10, 10])
# juegoCartas(D)