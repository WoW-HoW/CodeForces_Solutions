a=int(input())
b=[]
c=0
for i in range(a):
    b.append(int(input()))

if(sum(b)%360==0):
    c=1
    print("YES")
else:
    for j in range(a):
        d=b[-1]
        del b[-1]
        b=[d]+b
        if(c==1):
            break
        for i in range(a-2,-1,-1):
            if(sum(b[:i+1])==sum(b[i+1:])):
                c=1
                print("YES")
                break

if(c==0):
    print("NO")
