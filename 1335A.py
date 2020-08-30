for aww in range(int(input())):
    a=int(input())
    print(max(0,a//2-1 if a%2==0 else a//2))
