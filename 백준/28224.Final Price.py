# https://www.acmicpc.net/problem/28224

T = int(input())

prices = []
for tc in range(1, T + 1):
    prices.append(int(input()))

print(sum(prices))
