a=input()
b=input().split()
c=0
for i in range(len(b)):
    if(a[0]==b[i][0] or a[1]==b[i][1]):
        c=1
        print("YES")
        break
if(c==0):
    print("NO")
