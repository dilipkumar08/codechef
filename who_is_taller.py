n=int(input())
for _ in range(n):
    X,Y=map(int,input().strip().split())
    if X>Y:
        print("A")
    else:
        print("B")
