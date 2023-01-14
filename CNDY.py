for _ in range(int(input())):
    res="YES"
    N=int(input())
    li=list(map(int,input().split()))
    s=set(li)
    for i in s:
        if li.count(i)>2:
            res="NO"
            break
    print(res)
