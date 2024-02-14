class Person :
    def __init__(self,Firstname,age,gender):
        self.Firstname = Firstname
        self.age = age
        self.gender = gender

    def details (self):
        print(self.Firstname,"is studying")

teacher = Person("Joe",33,"Male")
accountant = Person("Esta""Kate",24,"Female")
lawyer = Person("Cynthia",29,"Female")


accountant.details()
print(teacher.Firstname,teacher.age,teacher.gender)
print('My name is',teacher.Firstname,'.I am',teacher.age,'years old','.My gender is ',teacher.gender,'.')
