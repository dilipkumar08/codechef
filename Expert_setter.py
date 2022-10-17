n=int(input())
for _ in range(n):
    X,Y=map(int,input().strip().split())
    if Y>=X/2:
        print("YES")
    else:
        print("NO")
