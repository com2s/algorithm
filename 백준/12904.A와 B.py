# https://www.acmicpc.net/problem/12904
# 113112	116
S = input()
T = input()

while len(T) > len(S):
    if T[-1] == 'A':
        T = T[:-1]

    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]

    else:
        print(0)
        break

if S == T:
    print(1)
else: print(0)
