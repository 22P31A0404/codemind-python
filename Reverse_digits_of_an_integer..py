n=int(input())
temp=n
r=0
while n>0:
    rem=n%10
    n=n//10
    r=r*10+rem
print(r)