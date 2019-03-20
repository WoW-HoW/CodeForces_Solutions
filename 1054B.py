a=int(input())
b=((list(map(int,input().split()))))
c=0
d=[]
if(b[0]==c):
    for i in range(a):
        if(b[i]==c):
            d.append(b[i])
            c+=1
        elif b[i] in d:
            c+=1
        else:
            print(c+1)
            break
    if(c==len(b)):
        print('-1')
else:
    print('1')
