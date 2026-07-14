# Datatpes:
    # 1) Int => Integer
        # Integers are numbers without decimal point including 0
        # Integers can be +ve , -ve

# x = 6
# print(x)
# print(type(x))   #<class 'int'>

# y = 0
# print(y)
# print(type(y))

# z = 4.0
# print(z)
# print(type(z))


    # 2) Float => Float
        # A number with decimal point is float
        # float can be _ve, +ve

# a = 7.5
# print(a)
# print(type(a))

# b = 0.0000
# print(b)
# print(type(b))

    # 3) Complex => Complex
        # A combination of Real numbers and Imaginary numbers.
            # Real:
                # All Integers and Floats are real numbers.
            # Imaginary:
                # A number which comes with 'j' suffix

            # 5+5j => Complex
# p = 4-8j
# print(p)
# print(type(p))


    # 4) String
        # String is a sequence of charecters (alphabetic, numeric, special)
        # collection of charecters is enclosed by quotes.
        # Types of quotes used for string formation:
            # ''  => Single quotes
            # ""  => Double quotes
            # ''' ''' => Tripple single quotes
            # """ """ => Tripple double quotes

# Examples:
# str1 = 'Hello'
# print(str1, type(str1))   # str

# str2 = "Apple"
# print(str2, type(str2))

# str3 = "Kumar@123"
# print(str3, type(str3))

# str4 = '''This is a new car..!'''
# print(str4, type(str4))

# str5 = """My dear friend Mr. Bean."""
# print(str5, type(str5))

# Sara is the most 'Beatiful' women in the town.
# str6 = "Sara is the most 'Beatiful' women in the town."
# print(str6, type(str6))

# str7 = '''
# Hello brother stephan..!
# welcome to "church"..
# may "god" bless you with all the 'happiness' and 'welth'..
# '''
# print(str7, type(str7))

# Built in methods (functions)
# str100 = "Hello"
# str200 = "my dear friend"
# str300 = "INDIA IS MY COUNTRY"
# Case manipulation functions:
        # .upper()
# print(str100.upper())   #HELLO

        # .lower()
# print(str100.lower())   #hello

        # .capitalize()
# print(str200.capitalize()) #My dear friend
# print(str300.capitalize()) #India is my country

        # .title()
# print(str200.title())      #My Dear Friend
# print(str300.title())      #India Is My Country

        # .swapcase()
# str400 = "Nigeria IS NIce"
# print(str400.swapcase())   #nIGERIA is niCE

# Indexing:
    # Positive Indexing => starts from 0
    # Negative Indexing => starts from -1
str1 = "APPLE"

# print(str1)
# print(str1[0])
# print(str1[-5])

# print(str1[1])
# print(str1[-4])

# print(str1[4])
# print(str1[-1])

# -------------------------------
# SLICING:
# print(str1[0:3:1])
# print(str1[2::1])
# print(str1[0::2])
# print(str1[0:5:3])

# print(str1[-5::2])
# print(str1[-1::-2])

#--------------------------------
# str2 = '1234'
# str3 = 'amma@123'
# str4 = "     "

# print(str2, type(str2))

# is methods of string:
    # .isalpha()
# print(str2.isalpha())
# print(str1.isalpha())
# print(str3.isalpha())


    # .isdigit()
# print(str1.isdigit())
# print(str2.isdigit())
# print(str3.isdigit())

    # .isspace()
# print(str1.isspace())
# print(str4.isspace())

    # .isalnum()
# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())
# print(str4.isalnum())

# s1 = "app le"
# print(s1.isalpha())
# print(s1.isspace())
#----------------------------------------------------------------
    # 5) Boolean
        # It represents True or False.
        # Always True has numeric value 1
        # Always False has numeric value 0

# print(True + True + True)
# print(5 * False)
# print((True * True - True +False) * True + (False -True))


    # 6) List
    # 7) Tuple
    # 8) Set
    
    # 9) Range

    # 10) Dict