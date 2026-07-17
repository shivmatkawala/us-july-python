# Conditional Statements:
    # if  => For only first condition
    # elif  => All the rest of the conditions
    # else  => default condtion / if all conditions return false then else block will be executed

# Write a program to ask for age 
# and return wether he/ she is 
# Kid, young, old
# 0-10, 10-25, 25->
# 

age = int(input("Enter your age: "))

if age > 0 and age <= 10:
    print("Kid")

elif age > 10 and age <= 25:
    print("Young")

elif age > 25:
    print("Old")

else:
    print("Invalid age")
