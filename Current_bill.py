u=int(input())
if(u<200):
    b=u*1.20
elif(u>200 and u<400):
    b=u*1.50
elif(u>=400 and u<600):
    b=u*1.80
else:
    b=u*2.00
if(u>=400):
    sr=b*0.15
    tb=b+sr
    print("%0.2f"%tb)
else:
    tb=b+100
    print("%0.2f"%tb)