a=int(input())
d=[]
e=[]
for i in range(a):
    b,c=input().split()
    d.append(b)
    e.append(int(c))
f=list(set(d))
g=[0]*len(f)
for i in range(len(f)):
    for j in
for i in range(len(f)):
    for j in range(a):
        if(d[j]==f[i]):
            g[i]+=e[j]
    print(g,f)
print(f[g.index(max(g))])
