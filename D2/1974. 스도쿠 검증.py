# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=%EC%8A%A4%EB%8F%84%EC%BF%A0&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    S = []
    result = 1
    for i in range(9):
        S.append(list(map(int, input().split())))
        
    for i in range(9):
        if len(set(S[i])) != 9:
            result = 0
            
    for i in range(9):
        D = []
        for j in range(9):
            D.append(S[j][i])
            
        if len(set(D)) != 9:
            result = 0        
                   
    K = []
    for i in range(9):
        K.append(S[i][0:3])
        K.append(S[i][3:6])
        K.append(S[i][6:9])
          
    for i in range(3):
        for j in range(3):
            U = []
            U = K[j+9*i] + K[j+3+9*i] + K[j+6+9*i]
            if len(set(U)) != 9:
                result = 0
                
        
    print('#{} {}'.format(test_case, result))
