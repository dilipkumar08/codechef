n=int(input())
for _ in range(n):
    A,B,X,Y=map(int,input().strip().split())
    if A*B>X*Y:
        print("NO")
    else:
        print('YES')
