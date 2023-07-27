# pypy3 보다 python3 가 더 빠르고 메모리도 훨씬 적게 소모함
# 모든 케이스를 탐색할 필요 없이 우선 K보다 작은지 큰지만 알아내는 것이 중요
# 코드 자체는 쉬우나 위처럼 하지 않으면 시간 초과로 실패함

Num, K = map(int,input().split())

check = 0
for i in range(2,K):
    if Num%i == 0:
        check = 1
        print('BAD', i)
        break

if not check:
    print('GOOD')
