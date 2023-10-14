a=int(input())
b=list(map(int,input().split()))
s=0
n=0
for i in range(0,a-2):
    if b[i]%2!=0 and b[i+2]%2==0:
        s+=1
    elif b[i]%2==0 and b[i+2]%2!=0:
        n+=1
print(s+n)