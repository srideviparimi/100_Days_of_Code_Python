def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
#looping through 1 to 19 as the last boundary is not included in the range
# 2. When is the function meant to print "You got it"?
# since we can only print "You got it" when the i=20, we will not get this output at all
# 3. What are your assumptions about the value of i?
# the i values are only from 1 to 19
# instead I changed the outer range to 21 instead of 20, so the last time the i value will be 20 and we print the output once
