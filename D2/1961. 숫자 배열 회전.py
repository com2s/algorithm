T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
   
    n = int(input())
    S = []
    for i in range(n):
        S.append(list(map(int, input().split())))
    
    r90 = []
    r180 = []
    r270 = []
    
    for i in range(n):
        for j in range(n):
            r90.append(S[-j-1][i])
            r180.append(S[-i-1][-j-1])
            r270.append(S[j][-i-1])
            
    print('#{}'.format(test_case))
    for i in range(n):
        for j in range(n):
            print(r90[n*i+j], end='')
            
        print(' ',end='')
        for j in range(n):
            print(r180[n*i+j], end='')
            
        print(' ',end='')
        for j in range(n):
            print(r270[n*i+j], end='')
            
        print()
