# Calculate the BMI using height and weight
# dividing weight by height squared
# bmi = round(weight / height ** 2)
# round to 2 decimal places

weight = float(input("What is your weight?\n"))
height = float(input("What is your height?\n"))

bmi = round(weight / (height ** 2), 2)

print(f"Your bmi is: {bmi}.")