# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWNcJ2sapZMDFAV8&categoryId=AWNcJ2sapZMDFAV8&categoryType=CODE&problemTitle=4408&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    cor = [0]*401
    for _ in range(N):
        a,b = map(int,input().split())
        if  a>b:
            a,b = b,a
        
        if a%2:
            a += 1
            
        if b%2:
            b += 1
            
        for i in range(a,b+1):
            cor[i] += 1
            
    print('#{} {}'.format(test_case,max(cor)))
