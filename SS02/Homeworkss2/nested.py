r=float(input("revenue: "))

if r<1000:
    print("SME")
else:
    a=float(input("asset: "))
    if a<500:
        print("Middle Market")
    else:
        print("CIB")
