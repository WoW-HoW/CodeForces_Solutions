n,pos,l,r=[*map(int,input().split())]
if(l==1 and r==n):
    print(0)
elif(l==1):
    print((abs(r-pos))+1)
elif(r==n):
    print(abs(pos-l)+1)
elif(pos==r and l==r):
    print(1+1)
elif(pos<=l):
    print(l-pos+1+(r-l)+1)
elif(pos>=r):
    print(pos-r+1+(r-l)+1)
else:
    print(min(abs(pos-l)+r-l+2,abs(r-l)+abs(r-pos)+2))
