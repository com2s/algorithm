T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    
    N, M = map(int, input().split())    
    m = M - 1
    A = []
    for n in range(N):
        A.append(list(map(int, input().split())))
        
    
    B = []
    for i in range(N+2*m):
        b = []
        for j in range(N+2*m):
            if m <= i < N+m and m <= j < N+m:
                b.append(A[i-m][j-m])
                
            else:
                b.append(0)
            
        B.append(list(b))
        
    sums = []
    for i in range(N):
        for j in range(N):
            sum = B[i+m][j+m]
           
            for k in range(1, m+1):
                sum += B[i+m-k][j+m]
                sum += B[i+m+k][j+m]
                sum += B[i+m][j+m-k]
                sum += B[i+m][j+m+k]
            
            sums.append(sum)
            
            sum = B[i+m][j+m]
           
            for k in range(1, m+1):
                sum += B[i+m-k][j+m-k]
                sum += B[i+m+k][j+m-k]
                sum += B[i+m+k][j+m+k]
                sum += B[i+m-k][j+m+k]
            
            sums.append(sum)
 
        
    sum_max = 0
    for i in range(2*N**2):
    	if sums[i] > sum_max:
            sum_max = sums[i]

    print('#{} {}'.format(test_case, sum_max))
