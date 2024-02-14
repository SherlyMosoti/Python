# Exceptions

try :
    print(x)
except :
    print("An error occurred")
finally:
    print("Success")

num1 = 20
num2 = 0

try :
   print (num1 / num2)
except :
   print("ZeroDivisionError occurred")
finally :
    print("Success")


# User-Defined Functions
try:
   def multiply( number1,number2) :
    print (number1*number2)
except:
    print("An error occurred")
finally:
    print("Success")

multiply(6,5)
