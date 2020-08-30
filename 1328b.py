for aiosd in range(int(input())):
    a,b=[*map(int,input().split())]
    c=(a*(a-1))//2
    d=b%a
    e=(1+((8*b)**0.5))//2
    print(d,e)
