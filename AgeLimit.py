n=int(input())
for i in range(n):
    l=list(map(int,input().strip().split()))
    if l[2]>=l[0] and l[2]<l[1]:
        print("YES")
    else:
        print("NO")
