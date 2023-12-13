from sys import stdin
from sys import stdin, setrecursionlimit

setrecursionlimit(1000000)

distances = None
houses = None
accesPoints = int()
minDistance = None

def verifyDistances(mid):
    global houses, accesPoints
    takenHouses = 0
    i = 0
    # print(mid)
    while((i < accesPoints) and (takenHouses < len(houses))):
        flag = True
        house = houses[takenHouses]
        posWifi = house + mid
        while((flag == True) and (takenHouses < len(houses))):
            house = houses[takenHouses]
            if(posWifi >= house):
                takenHouses += 1
                # print(posWifi)
            else:
                flag = False
        i += 1

    return takenHouses



def binarySearch(low, high):
    global distances, houses, accesPoints, minDistance
    if((low + 1) == high):
        minDistance = high / 2
        # print(minDistance)
    else:
        mid = (low + high) // 2
        if(verifyDistances(mid) != len(houses)):
            binarySearch(mid, high)
        elif(verifyDistances(mid) == len(houses)):
            binarySearch(low, mid)



def main():
    global distances, houses, accesPoints, minDistance
    numberCases = int(stdin.readline())
    for i in range(numberCases):
        minDistance = int()
        houses = []
        line = stdin.readline()
        tok = line.split()
        accesPoints = int(tok[0])
        cantHouses = int(tok[1])
        for j in range(cantHouses):
            house = int(stdin.readline())
            houses.append(house)
        houses.sort()
        if(accesPoints == 0):
            minDistance = (houses[-1] - houses[0]) / 2
        elif(accesPoints >= cantHouses):
            minDistance = 0
        else:
            # print(houses)
            binarySearch(0, houses[-1])
        print(f'{minDistance:.1f}')

main()

