user_age = int(input("How old are you? "))


def life_in_weeks(user_age):
    total_weeks = 90 * 52
    weeks_left = total_weeks - (user_age * 52)

    print(f"You have {weeks_left} weeks left.")


life_in_weeks(user_age)
