a=int(input())
n=list(map(int,input().split()))
s=0
c=0
for i in range(len(n)):
    if i%2==0:
        s+=n[i]
    elif i%2!=0:
        c+=n[i]
print(abs(s-c))