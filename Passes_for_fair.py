n=int(input())
for _ in range(n):
    N,k=map(int,input().strip().split())
    if N>=k:
        print("NO")
    else:
        print("YES")
