n=int(input())
for _ in range(n):
    X,N=map(int,input().strip().split())
    print((X//10)*N)
