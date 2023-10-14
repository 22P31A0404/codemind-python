a=int(input())
n=list(map(int,input().split()))
z=int(input())
s=0
for i in range(a):
    if z==n[i]:
        s=s+1
print(s)