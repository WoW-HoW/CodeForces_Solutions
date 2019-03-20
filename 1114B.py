b,c,d=list(map(int,input().split()))
a=list(map(int,input().split()))
e=[]
f=[]
g=list(sorted(a))
for i in range(1,d):
    e.append(a[1:-1].index(g[-i]))
print(e)
