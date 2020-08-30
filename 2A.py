n,p,q=int(input()),[],{}
for i in range(n):
    a,b=(input().split())
    q[a]=q.get(a,0)+int(b)
    p.append([a,q[a]])
print(p)
m=max(q.values())
for i,j in p:
    print(i,j)
    if q[i]==m and int(j)>=m:
	    print(i)
	    break
