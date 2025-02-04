# when we cant catch something that can't convert to integer
# try/catch block
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have typed an invalid number. Please try again with numbers only. ")
    age = int(input("How old are you? "))
if age > 18:
    print(f'You can drive at age {age}.')
else:
    print("You are not old enough to drive.")
