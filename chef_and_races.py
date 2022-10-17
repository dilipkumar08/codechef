n=int(input())
for _ in range(n):
    X,Y,A,B=map(int,input().strip().split())
    if X==A and Y==B or X==B and Y==A:
        print("0")
    elif X==A or X==B or Y==A or Y==B:
        print("1")
    else:
        print("2")
