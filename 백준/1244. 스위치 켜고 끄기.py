# https://www.acmicpc.net/problem/1244
N = int(input())
bulb = list(map(int, input().split()))
M = int(input())
switch_lst = [list(map(int, input().split())) for _ in range(M)]


def change(bulb, switch):
    if switch[0] == 1: # 남학생
        for i in range(switch[1] - 1, N, switch[1]):
            bulb[i] += 1 # 켜고끄기
            bulb[i] %= 2
    else:  # 여학생
        bulb[switch[1] - 1] = 1 - bulb[switch[1] - 1]
        for i in range(1, min(switch[1], N - switch[1] + 1)):
            if bulb[switch[1] - 1 - i] == bulb[switch[1] - 1 + i]:
                bulb[switch[1] - 1 - i] += 1
                bulb[switch[1] - 1 - i] %= 2
                bulb[switch[1] - 1 + i] += 1
                bulb[switch[1] - 1 + i] %= 2
            else:
                break
    return bulb


for switch in switch_lst:
    bulb_now = change(bulb, switch)

for i in range(1,N+1): # 출력형식에 맞춰서
    print(bulb_now[i - 1], end=' ')
    if i%20 == 0:
        print()
