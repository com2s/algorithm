# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=%EB%B0%B1%EB%A7%8C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1
# 처음 시도한 느린 방법
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    n = int(input())
    prices = list(map(int,input().split()))
    money = 0
    
    while len(prices) > 1:
        m = -1

        while prices[m] != max(prices):
            m -= 1
            
        money += (n+m)*prices[m] - sum(prices[:m])
        prices = prices[n+m+1:]
        n = -m-1

    print(f'#{test_case} {money}')


# 실제 정답 (전자에 비해 매우 빠름)

T = int(input())
 
for test_case in range(1, T + 1):
     
    N = int(input())
    N_list = list(map(int, input().split()))
    profit = 0
     
    while(len(N_list)!=0):
        max_num = max(N_list)
        max_index = N_list.index(max_num)       
        profit += max_num*max_index - sum(N_list[:max_index])
        N_list = N_list[max_index+1:]
         
         
    print("#%d"%(test_case), profit)
