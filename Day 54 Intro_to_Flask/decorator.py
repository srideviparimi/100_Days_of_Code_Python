'''
Python functions are first order functions meaning
1. They can be passed as arguments into another functions.
2. They can be returned as arguments
3. They can be used as objects
'''
'''
Decorator functions are the functions which does additional actions along with 
the intended function 
'''
import time
def decorator_function(function):
    def wrapper_function(n1,n2):#inner function that has the additional actions along with the actual function invocation
        time.sleep(3)
        value=function(n1,n2) #the function sent as argument is invoked
        time.sleep(2)
        print(value)
        print("wrapper executed completely")
    return wrapper_function #returns the wrapper function without ()

'''
def add(n1,n2):
    return n1+n2

wrapper_function=decorator_function(add) #here we sent add function as variable and not add() as it becomes invocation
wrapper_function(2,3)#we got wrapper_function and is invoked explicitly
'''
#Instead of above 4 lines of code we can use a decorator as follows

@decorator_function
def add(n1,n2):
   return n1+n2

add(2,3)

#The @decorator_function replaces add with wrapper.
#When you call add(2, 3), you're really calling wrapper(2, 3).