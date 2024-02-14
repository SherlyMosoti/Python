temperature = 32

if temperature > 37 :
    print("It is hot")
else:
     print("It is cold")

# A program that prints out the largest  number among
num1 = 45
num2 = 97
num3 =  32

if num1 > num2 and num1 >num3:
    print(num1 , "is the largest number")
elif num2 > num1 and num2 >num3 :
    print(num2 ,"is the largest number")
else :
    print(num3 ,"is the largest number")

# A program that checks whether a  number is even or odd
number = 84
if number % 2 == 0 :
    print(number,"is even")
else :
     print(number,"is odd")

 # A program that checks whether a number is prime or not

num = int(input("Enter a number : "))
if num > 1:
    for i in range (2 , num):
        if num % i == 0 :
            print("is not  a prime number")
            break
    else : print("a prime number")
else : print("not  a prime number")