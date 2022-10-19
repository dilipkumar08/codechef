n=int(input())
for _ in range(n):
    l=int(input())
    binary=str(input())
    temp=0
    for i in range(0,l-1):
        if binary[i]==binary[i+1]:
            temp+=1
    print(temp)
        
