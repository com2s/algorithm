# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=1959&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = map(int, input().split())
    D = M - N
    if D < 0:
        A = list(map(int, input().split())) #A에 긴 벡터
        B = list(map(int, input().split())) #B에 짧은 벡터
        D = -D
    else:
        B = list(map(int, input().split()))
        A = list(map(int, input().split()))
        N, M = M, N # N에 더 긴 값 할당
    
    sums = []
    for i in range(D+1):
        sum = 0
        for j in range(M):
            sum += A[i+j]*B[j]
            
        sums.append(sum)
        
    result = max(sums)
    print('#{} {}'.format(test_case, result))
