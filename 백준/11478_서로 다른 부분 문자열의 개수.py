s = input()
ss = []
for i in range(len(s)):
    for j in range(len(s)-i):
        ss.append(s[i:j+i+1])

print(len(set(ss)))
