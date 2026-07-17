# Operators:
    # Expression 
    # x + 5 = 10  
        # Operators: +, =
        # Operands: 
                # Variables: x
                # Constants: 5, 1

    # Any expression is formed using operators and operands.

    # Types of Operators :
        # Arithmetic Operators:
            # Addition +
            # Substraction -
            # Multiplication *
            # True Division /
            # Floor Division //
            # Exponentiation (Power) **
#             # Modulus (Mod) %
# x = 5
# y = 3

# print(f"Addition: {x+y}")
# print(f"Substraction: {x-y}")
# print(f"Multiplication: {x * y}")
# print(f"True Division: {x / y}")
# print(f"Floor Division: {x // y}")
# print(f"Power: {x ** y}")
# print(f"Mod: {x % y}")

        # Comparision Operators:
            # Greter than >
            # Lesser than <
            # Greter than or equal to >=
            # Lesser than or equat to <=
            # Not equal to !=,  <>
            # Equal to ==
# print(x > y)
# print(x < y)
# print(x == y)
# print(x != y)
# print(x >= y)   # x can be greater or x can be equal to y
# print(x <= y)

        # Assignement Operators:
            # Assign =
            # Add and Assign +=
            # Substract and Assign -=
            # Multiply and assign *=
            # True Divide and assign /=
            # Floor divide and assign //=
            # exponentition and assign **=
            # mod and assign %=
# p = 4

# p+=2
# p-=1
# p*=3
# p/=4
# p//=2
# p%=10
# print(p)

        # Indentity Operators:
            # is
            # is not
# Refference
x = [1, 2, 3, [10, 20]]
# y = x
# y[0] = 450
# print(x, id(x))
# print(y, id(y))





# Shallow Copy

# y = x.copy()
# y[0] = 450
# y[3][0] = 600

# print(x, id(x))
# print(y, id(y))

# Deep Copy
# from copy import deepcopy

# y = deepcopy(x)

# y[0] = 450
# y[3][0] = 600

# print(x, id(x))
# print(y, id(y))

# x = 10
# y = x
# print(x is y)

# x = [10, 20, [1, 2]]
# y = x.copy()

# print(x is y)
# from copy import deepcopy
# x = [1, 2, [10, 20]]
# y = deepcopy(x)
# print(x is y)

# x = [[1, 2], [3, 4]]
# y = x.copy()
# print(f"x: {id(x)}\ny:{id(y)}")

# print(x is y)


        # Membership Operators:
            # in
            # not in

# s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(9 in s1)
# print(11 in s1)


        # Logical Operators:
            # and 
            # or
            # not
# print(True and True and True)
# print(True and True and False)
# print(False and False and False)

# print(True or True or False)
# print(False or False or False )

# print(True or False and False or True and True)
# print(False or True and not(False) and True)

        # Ternary Operator:
# fav_prim_color = input("Enter your favourate primary color: ")
# result = "Peace" if fav_prim_color == "Blue" else "Sacrifice" if fav_prim_color == "Red" else "Nature" if fav_prim_color == "Green" else "Invalid color"
# print(result)

# Write a program to check eligiblity to get married.
# Gender = "F" and Age >= 18 ==> Eligible
# Gender = "M" and Age >= 22 ==> Elibilbe

# gender = input("Enter your gender: ")
# age = int(input("Enter your age: "))

# result = "Eligible" if (gender == "F" and age >= 18) or  (gender == "M" and age >= 22) else "Not Eligible"
# print(result)


        # Bitwise Operators:
            # & (AND)

print(10 & 23)  # 2

            # | (OR)
print(10 | 23)

            # ^ (XOR)
print(10 ^ 23)

