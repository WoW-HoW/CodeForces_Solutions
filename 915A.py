buckets,lenOfGarden=[*map(int,input().split())]
buck=[*map(int,input().split())]
buck.sort()
maxi=0
for i in range(buckets):
    if(lenOfGarden%buck[i]==0):
        maxi=lenOfGarden//buck[i]
print(maxi)
