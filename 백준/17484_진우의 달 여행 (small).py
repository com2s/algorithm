# 근데 이렇게 푸는 건 아닌 듯

x,y = map(int,input().split())

X = 3**(x-1)

def ternary(X):
    if X == 0:
        return 0
    else:
        return (X%3) + 10*ternary(X//3)
    
tn = []
for i in range(X):
    paded = str(ternary(i)).rjust(x-1,'0')
    tn.append(paded)

moves = []
for t in tn:
    check = 1
    for i in range(1,len(t)):
        if t[i] == t[i-1]:
            check = 0
            break

        
    if check:
        moves.append(t)
        
yy = [0]*y
road = [yy]*x

for i in range(x):
    road[i] = list(map(int,input().split()))

fuels = []
for i in range(y):
    for move in moves:
        count = 0
        fuel = road[0][i]
        k = i
        check = 1
        for n in move:
            if k == 0 and n == '0':
                check = 0
                break

            elif k == y-1 and n == '2':
                check = 0
                break

            else:
                if n == '0':
                    k -= 1

                elif n == '1':
                    pass

                elif n == '2':
                    k += 1

            count += 1
            fuel += road[count][k]
            # print(fuel)
        if check:
            fuels.append(fuel)

print(min(fuels))
