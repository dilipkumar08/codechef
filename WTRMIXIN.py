# cook your dish here
T=int(input())
for _ in range(T):
    A,B,X,Y=map(int,input().split())
    if B>A:
        if A+X>=B:
            print("YES")
        else:
            print("NO")
    elif B<A:
        if A-Y<=B:
            print("YES")
        else:
            print("NO")
    else:
        print("YES") 
