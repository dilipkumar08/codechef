N=int(input())
for i in range(N):
    res="YES"
    n=int(input())
    s=str(input())
    if n%2!=0:
        res="NO"
    else:
        for j in set(s):
            if s.count(j)%2!=0:
                res="NO"
    print(res)
