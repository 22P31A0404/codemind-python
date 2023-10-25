m=int(input())
n=int(input())
a=0
b=0
for i in range(1,m):
    if m%i==0:
        a=a+i
for i in range(1,n):
    if n%i==0:
        b=b+i
if(a==n and b==m):
    print("Amicable")
else:
    print("Not Amicable")
    