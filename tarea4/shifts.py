"""
Segment Tree Implementation
Carlos Ramírez
Noviembre 7 de 2020

"""

from sys import stdin

#Segment tree is represented as a list
n, MAXN = int(), 100000
tree = [0 for _ in range(MAXN * 2)]

#build the segment tree
def build(a, v, l, r):
    global tree
    if l == r:
        tree[v] = a[l]
    else:
        m = l + ((r - l) >> 1)
        build(a, v + 1, l, m)
        build(a, v + 2 * (m - l + 1), m + 1, r)
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - l + 1)])

#sum query
def getMin(v, L, R, l, r):
    ans = None
    if l > r:
        ans = float('inf')
    elif l == L and r == R:
        ans = tree[v]
    else:
        m = L + ((R - L) >> 1)
        ans = min(getMin(v + 1, L, m, l, min(r, m)), getMin(v + 2 * (m - L + 1), m + 1, R, max(l, m + 1), r))
    return ans

#update query
def update(v, L, R, pos, h):
    if L == R:
        tree[v] = h
    else:
        m = L + ((R - L) >> 1)
        if pos <= m:
            update(v + 1, L, m, pos, h)
        else:
            update(v + 2 * (m - L + 1), m + 1, R, pos, h)
        tree[v] = min(tree[v + 1], tree[v + 2 * (m - L + 1)])

def main():
    n, q = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    build(arr, 0, 0, n - 1)
    for i in range(q):
        inputList = stdin.readline()
        if(inputList[0] == 'q'):
            numbers = list(map(int, inputList[6:-2].split(',')))
            numA = numbers[0] - 1
            numB = numbers[1] - 1
            min = getMin(0, 0, n - 1, numA, numB)
            print(min)
        else:
            numbers = list(map(int, inputList[6:-2].split(',')))
            for j in range(len(numbers)):
                if(j != len(numbers) - 1):
                    update(0, 0 , n - 1, numbers[j] - 1, arr[numbers[j + 1] - 1])
                    arr[numbers[j] - 1], arr[numbers[j + 1] - 1] = arr[numbers[j + 1] - 1], arr[numbers[j] - 1]
                else:
                    update(0, 0 , n - 1, numbers[j] - 1, arr[numbers[j] - 1])

main()