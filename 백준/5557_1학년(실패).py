# 메모리 초과

T = int(input())
# 11
lst = list(map(int,input().split()))
# 8 3 2 4 8 7 2 4 0 8 8

# X를 2진법으로 바꾸는 함수
def binary(X):
    if X == 0:
        return 0
    else:
        return (X%2) + 10*binary(X//2)
    
X = 2**(T-2)

bn = []
for i in range(X):
    bn.append(binary(i))

count = 0
for test_int in bn:
    test = str(test_int).rjust(T-2,'0')
    num = lst[0]
    
    for i in range(T-2):
        if test[i] == '1':
            num += lst[i+1]

        else:
            num -= lst[i+1]

        if not (0 <= num <= 20):
            break

    if num == lst[-1]:
        count += 1

print(count)

#############
# 시간 초과 (ChatGPT 가 조금 바꾼 코드)
T = int(input())
# 11
lst = list(map(int,input().split()))
# 8 3 2 4 8 7 2 4 0 8 8

# X를 2진법으로 바꾸는 함수
def binary(X):
    binary_list = []
    while X > 0:
        binary_list.append(X % 2)
        X //= 2
    return binary_list

X = 2**(T-2)
count = 0

for i in range(X):
    test_int = binary(i)
    test_int += [0] * (T - 2 - len(test_int))  # 이진수의 길이를 T-2로 맞춰줍니다.
    test_int.reverse()  # 이진수의 순서를 뒤집습니다.
    num = lst[0]
    
    for j in range(T-2):
        if test_int[j] == 1:
            num += lst[j+1]
        else:
            num -= lst[j+1]
            
        if not (0 <= num <= 20):
            break

    if num == lst[-1]:
        count += 1

print(count)
