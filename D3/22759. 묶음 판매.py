# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZK3fpuaBJwDFAXk

T = int(input())

for test_case in range(1, T + 1):
     
    a, b = map(int, input().split())
    ans = 'no'
    c = a/(b+1)
    if c >= 0.5:
        ans = 'yes'
         
    print(ans)
