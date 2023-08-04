# https://www.acmicpc.net/problem/10986
# 263556kb	504ms

N, M = map(int, input().split())
lst = list(map(int, input().split()))

sum_dict = {0: 1}

cur_sum = 0
ans = 0
# 시간 복잡도를 내리기 위해 딕셔너리를 사용, 나머지를 계산하면서 수를 센다.
for i in range(N): 
    cur_sum = (cur_sum + lst[i]) % M

    ans += sum_dict.get(cur_sum, 0)

    sum_dict[cur_sum] = sum_dict.get(cur_sum, 0) + 1

print(ans)
