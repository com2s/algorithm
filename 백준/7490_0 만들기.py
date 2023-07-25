# 이렇게 해도 되는 걸까...
# 결과 얻은 후 정렬하는 것을 잊지 않기

chance = [[],[],[],[],[],[],[],[]]
for a in ' -+':
    chance[0].append(''.join([a]))
    for b in ' -+':
        chance[1].append(''.join([a,b]))
        for c in ' -+':
            chance[2].append(''.join([a,b,c]))
            for d in ' -+':
                chance[3].append(''.join([a,b,c,d]))
                for e in ' -+':
                    chance[4].append(''.join([a,b,c,d,e]))
                    for f in ' -+':
                        chance[5].append(''.join([a,b,c,d,e,f]))
                        for g in ' -+':
                            chance[6].append(''.join([a,b,c,d,e,f,g]))
                            for h in ' -+':
                                chance[7].append(''.join([a,b,c,d,e,f,g,h]))
                                
T = int(input())

for case in range(1,T+1):
    Num = int(input())
    Nums = list(reversed((range(1,Num+1))))
    opslst = chance[Num-2]
    ans = []

    for ops in opslst:
        TNums = Nums[:]
        count = 1
        for i in range(Num-1):
            op = ops[i]
            
            if op == ' ':
                TNums[i+1] = TNums[i+1]*(10**count)
                count += 1

            elif op == '+':
                count = 1

            elif op == '-':
                for j in range(count):
                    TNums[i-j] = -TNums[i-j]
                count = 1
            
        if sum(TNums) == 0:
            ans.append(ops)

    Nums = Nums[::-1]
    sols = []
    for i in range(len(ans)):
        ans[i] = ans[i][::-1]
        sol = '1'
        for j in range(Num-1):
            sol += ans[i][j] + str(Nums[j+1])

        sols.append(sol)
        
    sols.sort()

    for i in range(len(sols)):
        print(sols[i])

    print()
