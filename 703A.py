a=int(input())
d=0
e=0
for i in range(a):
    b,c=list(map(int,input().split()))
    if(b>c):
        d+=1
    elif(b<c):
        e+=1
#print(d,e)
if(d>e):
    print("Mishka")
elif(d<e):
    print("Chris")
else:
    print("Friendship is magic!^^")
