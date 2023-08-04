# https://www.acmicpc.net/problem/1541
# 113112	128
seq = input().split('-') 
ans = sum(map(int, seq[0].split('+')))
for i in range(1, len(seq)):
    ans -= sum(map(int, seq[i].split('+')))

print(ans)
