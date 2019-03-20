a=int(input())
b=[]
d=[]
s=0
for i in range(a):
    c=input()
    b.append([j for j in c])
    d.append((b[i].count("("))-(b[i].count(")")))
    if(c[-1]=="(" and c[0]==")"):
        d[i]=999
e=sorted(list(set(d)))
d=sorted(d)
for i in range(len(e)):
    if(e[i]*(-1) in e and (e[i]*(-1)<0) ):
        s+=1
s+=d.count(0)//2
print(s)
