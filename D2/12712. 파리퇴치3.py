# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AXuARWAqDkQDFARa&categoryId=AXuARWAqDkQDFARa&categoryType=CODE

T = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
ddi = [1, 1, -1, -1]
ddj = [1, -1, -1, 1]
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
        x = i + m 
        for j in range(N):
            y = j + m
            sum1 = sum2 = B[x][y]
            for k in range(1, m+1):
                for l in range(4):
                    nx = x + k*di[l]
                    ny = y + k*dj[l]
                    sum1 += B[nx][ny]

                    nnx = x + k*ddi[l]
                    nny = y + k*ddj[l]
                    sum2 += B[nnx][nny]
                    
            sums.append(sum1)
            sums.append(sum2) 
        
    sum_max = 0
    for i in range(2*N**2):
    	if sums[i] > sum_max:
            sum_max = sums[i]

    print('#{} {}'.format(test_case, sum_max))
            sum_max = sums[i]

    print('#{} {}'.format(test_case, sum_max))
