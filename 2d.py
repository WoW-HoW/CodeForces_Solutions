a=[]
sm=-81
for i in range(6):
    a.append([*map(int,input().split())])
#print(a)
for i in  range(4):
    for j in range(4):
        s=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
#        print(s)
#        print(a[i][j], a[i][j+1], a[i][j+2], a[i+1][j+1], a[i+2][j], a[i+2][j+1], a[i+2][j])
        if(s>sm):
            sm=s
print(sm)
