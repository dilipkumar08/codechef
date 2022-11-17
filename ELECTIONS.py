T=int(input())
for _ in range(T):
    A,B,C=map(int,input().strip().split())
    if A>50 and A>B and A>C:
        print("A")
    elif B>50 and B>A and B>C:
        print("B")
    elif C>50 and C>A and C>B:
        print("C")
    else:
        print("NOTA")
