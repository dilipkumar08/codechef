n=int(input())
for _ in range(n):
    X,Y,Z=map(int,input().strip().split())
    temp=0
    while Y>0:
        if Y>0:
            temp+=1
            Y=Y-Z
    print(X*temp)
    
