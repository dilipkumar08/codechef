n=int(input())
for i in range(n):
    ch,ca=map(int,input().strip().split())
    if 2*ch>ca*5:
        print("Chocolate")
    elif 2*ch==ca*5:
        print("Either")
    else:
        print("Candy")
