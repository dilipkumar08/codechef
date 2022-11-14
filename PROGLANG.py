T=int(input())
for _ in range(T):
    A,B,A1,B1,A2,B2=map(int,input().split())
    res=0
    if A==A1 and B==B1 or B==A1 and A==B1:
        res=1
    if A==A2 and B==B2 or B==A2 and A==B2:
        res=2
    print(res)
