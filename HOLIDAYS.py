for i in range(int(input())):
    m,p=map(int,input().split())
    li=list(map(int,input().strip().split()))
    li.sort()
    sum=0
    while True:
        sum+=li[-1]
        li.pop()
        if sum>=p:
            break
    print(len(li))
