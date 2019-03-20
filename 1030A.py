a=int(input())
b=input().split()
c=0
for i in range(a):
    if(b[i]=='0'):
        c+=1
if(a-c>=1):
    print("HARD")
else:
    print("EASY")
