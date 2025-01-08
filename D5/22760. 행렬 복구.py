# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZK3q5q6BdMDFAXk
import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
T = int(sys.stdin.readline().strip())

# 모든 원소가 서로 다른 원래 행렬과 전치행렬이 섞여있다.
# (i,i) 원소는 변하지 않으므로 이것으로 행렬을 찾을 수 있다.

for test_case in range(1, T+1):
    # N = int(input())
    N = int(sys.stdin.readline().strip())
    B = []
    used = set()
    ans = list([0] * N for _ in range(N))
    check = [0] * N
    for i in range(2*N):
        # B.append(list(map(int, input().split())))
        B.append(list(map(int, sys.stdin.readline().strip().split())))
        
    for r in range(2*N):
        isUsed = False
        for c in range(N):
            # 각 원소는 단 하나만 존재하므로 이미 사용된 원소인지 확인
            if B[r][c] in used:
                isUsed = True
                break
            
        if isUsed:
            continue
        
        check = B[r]
        for rr in range(2*N):
            if rr == r:
                continue
            isAns = False
            for c in range(N):
                
                if check[c] == B[rr][c]:
                    ans[c] = check
                    # B[r]의 모든 원소를 used에 추가
                    for i in check:
                        used.add(i)
                        
                    isAns = True
                    break
                
            if isAns:
                break
                
    for a in ans:
        print(' '.join(map(str, a)))
