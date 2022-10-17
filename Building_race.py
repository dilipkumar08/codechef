n=int(input())
for _ in range(n):
    A,B,X,Y=map(int,input().strip().split())
    if A/X>B/Y:
        print("Chefina")
    elif A/X<B/Y:
        print("Chef")
    else:
        print("Both")
