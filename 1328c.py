def asfd(b,a):
    c=''
    d=''
    for i in range(a):
        if(b[i]=='2'):
            c+='1'
            d+='1'
        elif(b[i]=='1'):
            c+='1'
            d+='0'
        else:
            c+='0'
            d+='0'
    return [c,d]
for aiosd in range(int(input())):
    a=int(input())
    b=input()
    c=''
    d=''
    f=0
    e1=a
    e2=a
    e3=a
    e4=a
    if('12' in b):
        e3=b.index('12')
        f=1
    if('11' in b):
        e1=b.index('11')
        f=1
    if('10' in b):
        e2=b.index('10')
        f=1

    
        
    if(f==0):
        c,d=asfd(b,a)
    else:
        e=min(e3,e1,e2,e4)
        c,d=asfd(b[:e+1],e+1)
        c+=(a-e-1)*'0'
        d+=b[e+1:]
    
        
    print(c)
    print(d)
