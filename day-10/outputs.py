def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    f_title = f_name.title()
    l_title = l_name.title()
    return f"{f_title} {l_title}"

print(format_name(input("What is your first name?"), input("What is your last name?")))
