# class myclass:
#     def __init__(self):
#         print(10)
# p1 = myclass()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#         print("init exji...")
#     def __str__(self):
#         return f" name is {self.name} age is {self.age}"

# p1 = Person("Shawon" , 20)

# p2 = Person("mahmudul" , 19)

# print(p1)

#create a new class

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def AnimalName(self):
        return self.name
    def AnimalAge(self):
        return self.age


firstAnimale = Animal("dog" , 2)
firstAnimale.AnimalAge()