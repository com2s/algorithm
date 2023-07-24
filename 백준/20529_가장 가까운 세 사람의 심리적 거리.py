# 더 나은 방법이 있을 것 같으니 찾아보자
def trans(a):
    result = []
    one = ['E','S','T','J']
    for i in a:
        if i in one:
            result.append(1)

        else:
            result.append(-1)

    return result

def ftn(a, b):
    result = 0
    for i in range(len(a)):
        if a[i] * b[i] == -1:
            result += 1

    return result

T = int(input())

for case in range(1,T+1):
    dist = []
    N = int(input())
    A = list(map(trans,input().split()))
    for i in range(N-2):
        for j in range(i+1,N):
            for k in range(j+1,N):
                ans = ftn(A[i],A[j]) + ftn(A[j],A[k]) + ftn(A[k],A[i])
                dist.append(ans)
                if not ans:
                    break
            if not ans:
                break
        if not ans:
            break
                
    print(min(dist))
