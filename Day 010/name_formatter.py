# can use inputs to use later like:
# formated_string = format_name(f_name, l_name)
# f_name = input("What is your first name? ")
# l_name = input("What is your last name? ")


def format_name(f_name, l_name):
    # if a user does not enter any characters, an empty string is passed
    # you want to end the function if this happens
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs. "
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    # return needed to capture the output of the function
    # return signals the end of the function, nothing below will be processed
    return f"{formatted_f_name} {formatted_l_name}"

# formated_string = format_name(f_name, l_name)
# or you can directly add the inputs here instead of variables
formated_string = format_name(input("What is your first name? "), input("What is your last name? "))
print(formated_string)
