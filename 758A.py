a=int(input())
b=list(map(int,input().split()))
c=max(b)
d=0
for i in range(a):
   d+=(c-b[i])
print(d)
