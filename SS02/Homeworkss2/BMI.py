m=float(input("your weight ? "))
h=float(input("your height in cm? "))
BMI=m/((h/100)**2)
if BMI<16:
    print("severely underweight")
elif BMI<=18.5:
    print("underweight")
elif BMI<=25:
    print("normal")
elif BMI<=30:
    print("overweigt")
else:
    print("obese")
