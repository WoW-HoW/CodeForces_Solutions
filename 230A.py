a,aww=[*map(int,input().split())]
b=[]
e=[]
flag=0
for i in range(aww):
    b.append([*map(int,input().split())])
b.sort()
for i in range(aww):
    if(b[i][0]<a):
        a+=b[i][1]
    else:
        flag=1
        break
if(flag==0):
    print("YES")
else:
    print("NO")
