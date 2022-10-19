n=int(input())
for _ in range(n):
    A,B,C=map(int,input().strip().split())
    if (A+B)%2!=0 or (A+C)%2!=0 or (B+C)%2!=0:
        print("YES")
    else:
        print("NO")
