# if

# Example 1: age>= 18 eligable

# age=17
# if age>=18:
#     print("eligible for vote")

# Example 2: check amount value after discount

# amount = 1500
# discount = 0
#
# if amount>=1000:
#     discount=amount*10/100
# print("Actual amount after discount:", amount-discount)

# if else condition

# Example 1: Check eligable & Ineligability to vote

# age=20
# if age>=18:
#     print("eligible for vote")
# else:
#     print("Not eligible for vote")

# Example 2: Check the number is even or odd

# num=20
#
# if num%2==0:
#     print(num,"is an Even number")
# else:
#     print(num, "is an Odd number")

# if elif else

# Example 1 for elif else
# Suppose there are multiple slabs of discount on a purchase
# 20% on amount exceeding 10000,
# 10% on amount between 5000-10000,
# 5% on amount between 1000-10000,
# No discount if amount <1000,

# amount = 1000
# discount=0
# print("Actual amount", amount)
#
# if amount>10000:
#     discount=amount*20/100
# elif amount>5000:
#     discount = amount * 10/100
# elif amount>=1000:
#     discount = amount * 5/100
# else:
#     discount=0
#
# print("Payment amount after discount:",amount-discount)

# Example 2: 1-sunday 2-monday

# weekno = 9
#
# if weekno==1:
#     print("Sunday")
# elif weekno==2:
#     print("Monday")
# elif weekno==3:
#     print("Tuesday")
# elif weekno==4:
#     print("Wednesday")
# elif weekno==5:
#     print("Thursday")
# elif weekno==6:
#     print("Friday")
# elif weekno==7:
#     print("Saturday")
# else:
#     print("Invalid Weekno", weekno)


# nested if else statements
# num divisible by 2 and 3
# num divisible by 2 not 3
# num divisible by 3 not 2
# num divisible by not 2 not 3

# num = 9
# print("Number:", num)
# if num%2==0:
#     if num%3==0:
#         print("Number is divisible by both 2 and 3")
#     else:
#         print("Number is divisible by 2 but not 3")
# else:
#     if num%3==0:
#         print("Number is divisible by 3 but not 2")
#     else:
#         print("Number is not divisible by 2 or 3")

# short hand if

# a,b = 10,20
# if a>b:
#     print(a, "is greater")

# if a<b: print(a, "is smaller") # writing same condition in single line

# short hand ifelse (ternary operator)
# a,b=20,10

# if a>b:
#     print(a, "is greater than", b)
# else:
#     print(b, "is greater than", a)

# print(a, "is greater than", b) if a>b else print(b, "is greater than", a) # ternary operator


# And (logical operator) with if elif else
# find largest of numbers
# a,b,c
# a>b and a>c then a is largest
# b>a and b>c then b is largest
# c is largest
# a, b, c= 10,20,30
#
# if a>b and a>c:
#     print("a is largest", a)
# elif b>a and b>c:
#     print("b is largest", b)
# else:
#     print("c is largest", c)


# pass
a=10
b=100
if a>b:
    pass    # pass is used when there is no condition to specify
print(a,b)