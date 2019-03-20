a=int(input())
for i in range(a):
    b,c,d,e=[*map(int,input().split())]
    f=b//e#directly buys
    g=(f//c)*d
    print(f+g)
