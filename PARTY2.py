n=int(input())
for _ in range(n):
    N,X,K=map(int,input().strip().split())
    if K>=N*X:
        print("YES")
    else:
        print("NO")
