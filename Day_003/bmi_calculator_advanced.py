# Calculate the BMI using height and weight
# dividing weight by height squared
# bmi = round(weight / height ** 2)
# round to 2 decimal places

weight = float(input("What is your weight?\n"))
height = float(input("What is your height?\n"))

bmi = round(weight / (height ** 2), 2)

if bmi >= 25:
    print(f"Your bmi is: {bmi}. You are overweight.")
elif bmi >= 18.5:
    print(f"Your bmi is: {bmi}. You are normal weight")
else:
    print(f"Your bmi is: {bmi}. You are underweight")
