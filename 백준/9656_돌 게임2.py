# 규칙을 발견한다면...

N = int(input())

if N%2 == 0:
    print('SK')
    
else:
    print('CY')

# 더 쉽게 표현한다면...

print('SK' if int(input())%2 == 0 else 'CY')


# 그러나 아마 문제의 의도는 아래 방식?

import sys
N = int(sys.stdin.readline())
dp = [-1]*1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
for i in range(4, N+1):
    if dp[i-1] or dp[i-3]: # 0은 False, 그 외 숫자는 True
        dp[i] = 0
    else:
        dp[i] = 1
print('SK' if dp[N] == 0 else 'CY')
