a=int(input())
b=["I","hate"]
c=["I","love"]
d=["it","that"]
e=[]
for i in range(a):
    if(i%2!=0):
        e=e+c
    else:
        e+=b
    if(i!=a-1):
        e+=[d[1]]
e+=[d[0]]
print(" ".join(e))
