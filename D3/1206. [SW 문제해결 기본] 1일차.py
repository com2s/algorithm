T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    B = list(map(int, input().split()))
    good = 0
    
    i = 2
    while i < N-2:
        bs = sorted(B[i-2:i+3])
        if B[i] == bs[-1]:
            good += bs[-1] - bs[-2]
            i += 3
            
        else:
            i += 1
            
    print(f'#{test_case} {good}')
