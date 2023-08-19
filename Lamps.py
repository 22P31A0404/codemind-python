n,k,x,y=map(int,input().split())
a=n*x
b=k*x+(n-k)*y
if(x<y):
    print(a)
else:
    print(b)