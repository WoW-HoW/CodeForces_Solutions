a,b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=1
for i in range(a-1):
    if((i+1+c[i])==b):
        print("YES")
        d=0
        break
if(d==1):
    print("NO")
        
