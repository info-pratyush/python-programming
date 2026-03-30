#The match statement selcts one of many code blocks to be executed.

day = int(input("Enter a day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:             #default case if no other case matches
        print("Invalid day number")        