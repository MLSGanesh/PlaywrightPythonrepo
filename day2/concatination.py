#concatincation  +
#When we use + between 2 numeric values, it will perform addition
print(10+10) #20 valid
print(10.5+12.0) #22.5 valid
print(10+10.5) #20.5 valid

#When we use + between 2 strings, it will perform concatination
print("Welcome"+' Python') #Welcome Python

#When we use + between one boolean and numeric values, it will perform addition
print(True+5) #6 numeric value of True=1 and False=0
print(False+5) #5
print(True+True) #2

#When we use + between numeric and string values, it is not valid
print(10+"Welcome") #not valid because both are different types,Type error:

print(10.5+'Welcome') #not valid because both are different types,Type error:
print(True+'Welcome') #not valid because both are different types,Type error: