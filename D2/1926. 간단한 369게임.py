# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
N = int(input())

def f(n):
    n = str(n) # count 메서드 대신 한 번에 3,6,9를 다 찾는 것이 더 빠를 수도 있다.
    c1 = n.count('3')
    c2 = n.count('6')
    c3 = n.count('9')
    if c1 or c2 or c3:
        return '-'*(c1+c2+c3)
    else:
        return n
    
for i in range(1,N+1):
    print(f(i),end=' ')
