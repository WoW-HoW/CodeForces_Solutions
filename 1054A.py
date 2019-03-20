x,y,z,t1,t2,t3=list(map(int,input().split()))
a=t1*abs(x-y)
b=t2*abs(x-z)+t3*3+t2*abs(x-y)
if(b<=a):
    print("YES")
else:
    print("NO")
