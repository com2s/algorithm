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

#### 아래는 내장함수를 쓰지 않는 풀이 (아마 원래 의도?)

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def onetwo(lst):
    one = 0
    two = 0
    
    for i in lst:
        if i > one:
            two = one
            one = i
            
        elif i > two:
            two = i
            
    return one, two

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    B = list(map(int, input().split()))
    good = 0
    
    i = 2
    while i < N-2:
        bs = onetwo(B[i-2:i+3])
        if B[i] == bs[0]:
            good += bs[0] - bs[1]
            i += 3
            
        else:
            i += 1
            
    print(f'#{test_case} {good}')
