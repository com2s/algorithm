# from numpy import dot
# 코딩 테스트에서 사용불가

def dot(a, b):
    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

gan = [1,2,3,3,4,10]
sau = [1,2,2,2,3,5,10]

T = int(input())

for i in range(T):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    gan_score = dot(A, gan)
    sau_score = dot(B, sau)

    if sau_score > gan_score:
        print(f"Battle {i+1}: Evil eradicates all trace of Good")

    elif gan_score > sau_score:
        print(f"Battle {i+1}: Good triumphs over Evil")

    else:
        print(f"Battle {i+1}: No victor on this battle field")
