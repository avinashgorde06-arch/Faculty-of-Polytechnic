#problem1
def ask_text():
    while True:
        name = input("What is your name? ")
        if name == "":
            return("Can't be empty. Try again.")
        else:
            return(name)
            break
    while True:
        sub_name = input("Enter subject name? ")
        if sub_name == "":
            return("Can't be empty. Try again.")
        else:
            return(sub_name)
            break
          #probem2
          def ask_marks(): 
    while True: 
        user_input = input("Enter your marks 1-100: ") 
        if user_input.isdigit(): 
            return(user_input)
            break
        else: 
            return("Enter whole number only")
ask_marks()
#problem3
def ask_y_n():
    while True:
        user_input=input("do you want to add another subject:-")
        if user_input == "y":
            return(True)
            break
        elif user_input == "n":
            return(False)
            break
        else:
            print("type only y/n only")
ask_y_n()
#problem4
def collect_one_subject():
    name = ask_text("Subject name: ")
    m1 = ask_mark("  Mark 1 (0-100): ")
    m2 = ask_mark("  Mark 2 (0-100): ")
    m3 = ask_mark("  Mark 3 (0-100): ")

    return (name, m1, m2, m3)
