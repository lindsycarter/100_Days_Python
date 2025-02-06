

def calculate_love_score(name1, name2):
    name_combo = name1 + name2
    lower_combo_string = name_combo.lower()

    t = lower_combo_string.count("t")
    r = lower_combo_string.count("r")
    u = lower_combo_string.count("u")
    e = lower_combo_string.count("e")
    true = t + r + u + e

    l = lower_combo_string.count("l")
    o = lower_combo_string.count("o")
    v = lower_combo_string.count("v")
    e = lower_combo_string.count("e")
    love = l + o + v + e
    score = int(str(true) + str(love))

    if (score < 10) or (score > 90):
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif (score >= 40) and (score <= 50):
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}.")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

calculate_love_score(name1, name2)



