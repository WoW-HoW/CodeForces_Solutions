a,b=[*map(int,input().split())]
c=[*map(int,input().split())]
d=0
c.sort()
if(c[0]!=0):
    d=c[0]
for i in range(len(c)-1):
    if((c[i+1]-c[i])/2>d):
        d=(c[i+1]-c[i])/2
if(b-c[-1]>d):
    d=b-c[-1]
print(d)
