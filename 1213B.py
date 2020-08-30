for awww in range(int(input())):
    a=int(input())
    b=list(map(int,input().split()))
    c=0
    for i in range(a):
        if(b[i]>=a):
            c+=1
    print(c)
