T=int(input())
for _ in range(T):
    N,K=map(int,input().strip().split())
    money=list(map(int,input().strip().split()))
    res=""
    for i in range(N):
        if money[i]<=K:
            res+="1"
            K-=money[i]
        else:
            res+="0"
    print(res)
    
