for aww in range(int(input())):
    len1,len2=[*map(int,input().split())]
    arr1=[*map(int,input().split())]
    arr2=[*map(int,input().split())]
    me=max(max(arr1),max(arr2))
    a=[0 for i in range(me+1)]
    
