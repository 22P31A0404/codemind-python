s=int(input())
rs=s%3600
h=s//3600
m=rs//60
rs=rs%60
print(f"H:M:S-{h:}:{m:}:{rs:}")