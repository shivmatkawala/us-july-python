# Functional Programming Paradigm:
    # Functions are block of codes which can be reused
    # Functions are base for object oriented programming

# How to create a function:
    #Header:
        # Function always starts with "def" keyword
        # then "function_name"
        # then (input_parameters)
        # then :

    #Body:
        # After indentation of 4 empty spaces
        # the code written after header will be treated 
        # as a block of code of that function


# def function_name(input_parameter):  #Header
#   print(input_parameter)             # Body

# Write a function to print "Hello World"

# def greet():
#     print("Hello World")

# Functions must be called in order to execute them

# greet()
# greet()


# Functions Types:
    # No Argument Function
# def get_1_to_10_numbers():
#     for i in range(1, 11):
#         print(i)

# get_1_to_10_numbers()

# get_1_to_10_numbers()

# get_1_to_10_numbers()

#-----------------------------
# def square_of_5():
#     print(5 ** 2)

# square_of_5()
# square_of_5()
#-----------------------------

    # Positional Argument Function

# def my_info(name, age, gender, salary):
#     print(f'''
#         My Name is {name}
#         My Age is {age}
#         My Gender is {gender}
#         My Slary is {salary}
#     ''')

# my_info("Siva Kumaran", 34, "Male", 30000)

    # Default Argument Function
def greet(name="Buddy"):
    print(f"Hello {name}")

# greet()
# greet("The Great Imran Khan")
# greet()

# greet(100)

    # Keyword Argument Function
# def signup(firstname, lastname, dob, city, country):
#     import time
#     print(f"""
#         Firstname: {firstname}
#         Lastanme:  {lastname}
#         DOB:       {dob}
#         City:      {city}
#         Contry:    {country}
#     """)
#     time.sleep(3)
#     print("Singnup Successful..!")


# signup(city="Los Angeles", lastname="Rivers", firstname="Richard", dob="5/7/2001", country="USA")


    # Variable length argument function
# def addition(*args):
#     print(f"Sum: {sum(args)}")

# addition(3, 4, 5, 6, 7, 8, 9)
# addition(8, 2)

# addition(3, 4, 5)
# addition(6, 6)
# addition(7, 8, 9, 5)


    # Variable length keyword argument function

# def total_marks(**kwargs):
    # marks = list(kwargs.values())
    # total = sum(marks)
    # print(total)

# total_marks(mack=45, sara=67, david=34, vimal=90)
# d1 = {"Raj":55, "kiran":90, "sama":66, "fama":33}
# total_marks(**d1)
# 


#*********************PRACTICE********************************
# Write a function to print cube's of all numbers
# in between 1 to 11  (No argument Function)

# def cubes():
#     for i in range(1, 11):
#         print(i**3)

# cubes()

# def cubes():
#     count = 1
#     while count < 11:
#         print(count **3)
#         count+=1

# cubes()

# def cubes():
#     c = [num**3 for num in range(1, 11)]
#     print(c)

# cubes()

# def cubes():
#     c = list(map(lambda num: num**3, [i for i in range(1, 11)]))
#     print(c)

# cubes()

#--------------------------------------------------


# Write a function which takes an argument
# a list of marks.
# and print total count of marks less than 40.

# marks = [23, 67, 90, 40, 33, 12, 67, 100, 34]

# def failed(m:list):
#     count = 0
#     for i in m:
#         if i < 40:
#             count+=1
#     print(f"Total {count} marks are less than 40")


# failed(marks)

# def failed(m:list):
#     total = 0
#     index = 0
#     while count < len(m):
#         if m[index] < 40:
#             total+=1
#         count+=1
#     print(f"Total {total} marks are less than 40")

# failed(marks)

#--------------------------------------------

# def failed(m:list):
#     f = len(list(filter(lambda num: num if num < 40 else None, m)))
#     print(f)

# failed(marks)

#-------------------------------------

# def failed(m):
#     f = [(mark if mark < 40 else None) for mark in m]
#     print(len(f) - f.count(None))
    
# failed(marks)

#------------------------------------------------------

# Write a function which ll display list of 
# all students who failed in exam.

stud_marks = {"Sharmishta": 45, "Laxmi": 60, "Ajain": 30, "Dev": 20, "Imran": 12, "Amit": 90, "Viquar": 100}
