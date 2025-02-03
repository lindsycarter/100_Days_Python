def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Is Leap Year")
            else:
                print("Is NOT Leap Year")
        else:
            print("Is Leap Year")
    else:
        print("Is NOT Leap Year")


is_leap_year(int(input("Which year do you want to check? ")))
