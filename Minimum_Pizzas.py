n=int(input())
for _ in range(n):
    N,X=map(int,input().strip().split())
    a=(N*X)/4
    b=(N*X)//4
    if a>b:
        print(b+1)
    else:
        print(int(a))
