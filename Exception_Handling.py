# Exception Handling.

# There are 2 types of event that distrube the flow of execution of a program.

# Run time error ==> Exception
# - It is event that disturbe the normal flow of execution of program.
# - It occure at a run.
# - logical error and run time are the 2 type of exception.
# - it can be handle
#   - try # it a block where we write an logic in which we have a doubt.
#   - except # it a block where we write what to do if exception occure.
#   - else   # if something wanted to run if no exception occure.
#   - final  # it is block which runs always

# Logical Exception.
##def add(a, b):
##    print( a-b)
##add(2,3)


# Run time Exception
##try : 
##    a = 2/0
##    print(a)
##except :
##    print("something wrong")
##
##print("....")






# Cumpile time error ==> Error
# - It is an event the don't allow to execute the program.
# - While checking the syntax or compiling the program.
# - A Syntax Error
# - i can't be handle

##if :
##    print("Hello")
##else:
##    print("bye")
##print(",,,")

#-----------------------------------------------------------------------------

# Custom Exception: Making of own Exception.
# Step 1: Make custom exception class then inherit the Exception ( parent class of all the exceptions)
# Step 2 : use "raise" to call the exception
# Step 3 : Define the exception name with except.

class MyExceptionError(Exception):
    pass

def demo7():
    try :
        age = int(input("Enter age "))
        if age < 18 :
            raise MyExceptionError("This is custom exception...")

    except MyExceptionError as e :
        print(e)
    except :
        print("custom message...")

    else:
        print("Your over age........")
#------------------------------------------------------------------------------

# raise : it is a keyword use to call the exceptions
def demo6():
    try :
        age = int(input("Enter your age " ))
        if age < 18 :
            raise ZeroDivisionError("Under age")
        
    except ZeroDivisionError as e:
        print(e)

    else:
        print("Valid age...")


    
#------------------------------------------------------------------------------

# Exception : It is a parent(base) class of all the exceptions.
#            -it can handle all the type of exceptions.

def demo5():
    try :
        a = int(input("Enter number "))  
        b = int(input("Enter number 2 "))
        c = a/b
        print(d)
        
    except ZeroDivisionError as e:
        print( e)

    except Exception  as e:
        print("im exception")
        print( e)

        
    else:
        print("Division is ", c)

#-----------------------------------------------------------------------------

# Using exceptions in a single line.

def demo5():
    try :
        a = int(input("Enter number "))
        b = int(input("Enter number 2 "))
        c = a/b
        print(d)
        
    except (ZeroDivisionError,NameError,ValueError)  as e:
        print( e)
        
    else:
        print("Division is ", c)


        

# ---------------------------------------------------------------------------

# Handling different types of exceptions.
def demo4():
    try :
        a = int(input("Enter number "))
        b = int(input("Enter number 2 "))
        c = a/b
        print(d)
        
    except ZeroDivisionError as e:
        print( e)
        
    except NameError as e:
        print( e)

    except ValueError as e:
        print( e)     
    else:
        print("Division is ", c)
        


# ----------------------------------------------------------------------------

# Handling 2 different types of exceptions.

def demp3():
    a = int(input("Enter number "))
    b = int(input("Enter number 2 "))

    try : 
        c = a/b
        print(d)
    except ZeroDivisionError as e:
        print( e)
        
    except NameError as e:
        print( e)

    else: 
        print("Division is ", c)
    

    finally:
        print("Program ended.....")
    
#-------------------------------------------------------------------------------
        
# Handle ZeroDivision Exception or Handling Specific Exception only.
def demo2(): # for specific exception
    a = int(input("Enter number "))
    b = int(input("Enter number 2 "))

    try : 
        c = a/b 
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Division is ", c)
    finally:
        print("Program ended.....")

#-----------------------------------------------------------------------------       
# Showing basic structur of exception handling.
def demo1():
    a = int(input("Enter number "))
    b = int(input("Enter number 2 "))

    try : 
        c = a/b # line with doubt that it can cause exception.
    except :
        print("Trying to divide by zero")
        # what to do if exception occure.

    else:
        print("Division is ", c)
        # what to do if no exception.

    finally:
        print("Program ended.....")
        # if program ended.
        # runs even if exception occure or not.

#-----------------------------------------------------------------------------






























