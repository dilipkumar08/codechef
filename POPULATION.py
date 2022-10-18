n=int(input())
 
for _ in range(n):
    X,Y,Z=map(int,input().strip().split())
    print((X-Y)+Z)
