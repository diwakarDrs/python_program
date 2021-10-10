Weight = float(input("Enter you weight : "))
Height = float(input("Enter you height : "))
BMI = round((Weight / Height**2))

if BMI<18.5:
    print(f"Your BMI is {BMI} and you are Under weight")
elif BMI<25:
    print(f"Your BMI is {BMI} and You have Normal weight")
elif BMI<30:
    print(f"Your BMI is {BMI} and You have Older weight")
elif BMI<35:
    print(f"Your BMI is {BMI} and You have Obese")
else:
    print(f"Your BMI is {BMI} and you are clinically obese")
