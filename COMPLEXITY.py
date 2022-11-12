n=int(input())
for _ in range(n):
    A,B=map(int,input().strip().split())
    if A>B:
        print("YES")
    else:
        print("NO")
    
