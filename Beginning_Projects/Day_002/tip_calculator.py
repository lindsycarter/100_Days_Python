#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

# Welcome the user to the tip calculator
print("Welcome to the tip calculator.")

# 2 - What is the bill total?
bill = float(input("What is the total bill amount? $"))
# FOR TESTING print total of bill to 2 decimal precision
#print("%.2f" % bill)

# 3 - What tip amount would you like to give? 10 / 12 / 15 % | other
# popular tip options are...
tip = int(input("Please select your tip amount: 10% / 12% / 15%  "))
# FOR TESTING print total of bill to 2 decimal precision
#print(f"You have selected " "%.0f" % tip + "%")
tipPercent = tip / 100

# 4 - How many people will be splitting the bill?
numPeople = int(input("How many people will be splitting the bill? "))
# FOR TESTING print total of bill to 2 decimal precision
#print(numPeople)

# 5 - What is the total amount due / # of people to split with?
# and round to 2 places
totalDue = round(((bill + (bill * tipPercent)) / numPeople), 2)

# 6 - Print what each person should pay
print(f"Each person must pay: ${totalDue}")