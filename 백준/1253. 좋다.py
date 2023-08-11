# https://www.acmicpc.net/problem/1253

N = int(input())

lst = list(map(int, input().split()))
ans = []
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        elif lst[i] - lst[j] in lst:
            arr = lst[:] # pop에서 인덱스가 꼬이지 않도록 경우 구분
            if i > j:
                arr.pop(i)
                arr.pop(j)
            else:
                arr.pop(j)
                arr.pop(i)

            if lst[i] - lst[j] in arr:
                ans.append(lst[i])
                break
#print(ans)
print(len(ans))
