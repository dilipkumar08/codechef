from collections import Counter
T=int(input())
for _ in range(T):
    N=int(input())
    li=list(map(int,input().strip().split()))
    c=Counter(li)
    m=max(c.values())
    print(sum(c.values())-m)
        
