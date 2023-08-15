BS=int(input())
if BS<=10000:
    GS=BS+(0.8*BS)+(0.2*BS)
elif BS>10000 and BS<20000:
    GS=BS+(0.9*BS)+(0.25*BS)
elif BS>20000:
    GS=BS+(0.95*BS)+(0.30*BS)
print("%0.2f"%GS)