# Datatype


number = 60  # int
num = 34.78  # float
greeting = "Hello there "  # str
is_Python_Interesting = True  # bool

# A variable   with multiple  values
languages = ["Python","php","Java","Kotlin"] # list
fruits = ("Watermelon", "Mango","Grapes","Pineapple") # Tuple
countries = {"Kenya","Turkey","Dubai"} # set

# Dictionary
details = {
 "firstname" : "Ashley",
 "course" : "MIT",
  "age": 18 ,
 "nationality ": "Kenya"
}
print(number)
print(num)
print(is_Python_Interesting)
print(greeting)
print(countries)
print(details)
print(details["firstname"])


# Determining the datatype of  a variable

print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting  - Converting one datatype to another
print(float(number))
print(int(num))