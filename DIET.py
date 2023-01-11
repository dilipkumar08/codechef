for _ in range(int(input())):
    days,protein=map(int,input().split())
    li=list(map(int,input().split()))
    temp=0
    res="YES"
    for i in range(1,days+1):
        temp+=li[i-1]
        if temp>=protein:
            temp=temp-protein
        else:
            res="NO"+" "+str(i)
            break
    print(res)
