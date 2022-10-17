n=int(input())
for _ in range(n):
    A,B,C=map(int,input().strip().split())
    if A!=0 and B!=0 and C!=0 and A+B+C==180:
        print("YES")
    
    else:
        print("NO")
