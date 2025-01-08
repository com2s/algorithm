# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AZD8M-IKyFEDFAVs

T = int(input())
     
for test_case in range(1, T + 1):
     
    Wx1, Wy1, Wx2, Wy2 = map(int, input().split())
    Bx1, By1, Bx2, By2 = map(int, input().split())
    Bx3, By3, Bx4, By4 = map(int, input().split())        
     
    if (Bx1 <= Wx1 and Wx2 <= Bx2) and (By1 <= Wy1 and Wy2 <= By2):
        print('NO')
        continue
     
    if (Bx3 <= Wx1 and Wx2 <= Bx4) and (By3 <= Wy1 and Wy2 <= By4):
        print('NO')
        continue
     
    if Bx1 > Bx3:
        Bx1, By1, Bx2, By2, Bx3, By3, Bx4, By4 = Bx3, By3, Bx4, By4, Bx1, By1, Bx2, By2
     
    if Bx1 <= Wx1 <= Bx2 and By1 <= Wy1 <= By2:
        if By1 <= Wy2 <= By2:
            if Bx3 <= Wx2 <= Bx4 and By3 <= Wy2 <= By4:
                if By3 <= Wy1 <= By4:
                    if Bx2 >= Bx3:
                        print('NO')
                        continue
                 
        elif Bx1 <= Wx2 <= Bx2:
            if Bx3 <= Wx2 <= Bx4 and By3 <= Wy2 <= By4:
                if Bx3 <= Wx1 <= Bx4:
                    if By2 >= By3:
                        print('NO')
                        continue
                     
    if Bx1 <= Wx1 <= Bx2 and By1 <= Wy2 <= By2:
        if Bx1 <= Wx2 <= Bx2:
            if Bx3 <= Wx1 <= Bx4 and By3 <= Wy1 <= By4:
                if Bx3 <= Wx2 <= Bx4:
                    if By4 >= By1:
                        print('NO')
                        continue
     
    print('YES')
