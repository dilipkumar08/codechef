a=["a","e","i","o","u"]
T=int(input())
for _ in range(T):
    N=int(input())
    s=str(input())
    temp=4
    i=0
    res="YES"
    while i<N:
        if s[i] not in a:
            temp-=1
        else:
            temp=4
        if temp==0:
            res="NO"
            i=N
        i+=1
    print(res)
        
