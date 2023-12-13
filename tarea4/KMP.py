def precompute(P, N):      # P = "ABACABA"   lps = [0, 0, 1, 0, 1, 2, 3]
  lps = [None for _ in range(N)]
  size = 0 
  lps[0] = 0
  i = 1
  while i < N:
    if P[i] == P[size]:
      size += 1
      lps[i] = size
      i += 1
    else:
      if size != 0:
        size = lps[size - 1]
      else:
        lps[i] = 0
        i += 1
  return lps

def KMP(P, T):
  N = len(P)
  M = len(T)
  lps = precompute(P, len(P))
  j = 0  # índice para P
  i = 0  # índice para T

  ans = False
  
  while not ans and (M - i) >= (N - j):
    if P[j] == T[i]:
      i += 1
      j += 1
    if j == N:
      ans = True
      #j = lps[j-1]
    elif i < M and P[j] != T[i]:
      if j != 0:
         j = lps[j-1]
      else:
        i += 1
  return ans

#c = "ABACABAA"
c = "ABABCABAB"
# lps = precompute(c, len(c))
# print(lps)
print(KMP("ABABCABAB", c))