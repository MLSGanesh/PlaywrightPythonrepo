# match statement is used to perform different actions based on different conditions
# Instead of writing many if else statements, user can use match statements

# Example 1

# day=10
# match day:
#     case 1:print("Sunday")
#     case 2:print("Monday")
#     case 3:print("Tuesday")
#     case 4:print("Wednesday")
#     case 5:print("Thursday")
#     case 6:print("Friday")
#     case 7:print("Saturday")
#     case _:print("Invalid week day")

# Example 2: combine values
# use pipe character(|) as an operator in case evaluation to check for more than one value match in one case:

day = 6
match day:
    case 2|3|4|5|6:print("Weekday")
    case 1|7:print("Weekend")
    case _:print("Invalid week day")