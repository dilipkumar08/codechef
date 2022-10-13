n=int(input())
for i in range(n):
    x=list(map(int,input().split()))
    if x[0]>=x[1]:
        print("YES")
    else:
        print("NO")
