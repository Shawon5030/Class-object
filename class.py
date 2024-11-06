# class myclass:
#     def __init__(self):
#         print(10)
# p1 = myclass()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self)
        print(self.name)
        print(self.age)
        print("init exji...")
    def __str__(self):
        return "{self.name}""{self.age}"`
        
p1 = Person("Shawon" , 20)

p2 = Person("mahmudul" , 19)
