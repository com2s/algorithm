#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_case = int(input())
    X = list(map(int, input().split()))
    
    X.sort()
    
    n=0
    m=0
    Y = []
    while m < 1000:
        if X[n] == X[m]:
            m += 1
                
        else:
            Y.append(X[n:m])
            n = m
                
    y = len(Y)
    a = 0
    ans = 0
    for i in range(y):
        if len(Y[a]) <= len(Y[i]):
            ans = Y[i][0]
            a = i
     
    print('#{} {}'.format(test_case, ans))
