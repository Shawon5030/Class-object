# class myclass:
#     def __init__(self):
#         print(10)
# p1 = myclass()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        print("init exji...")
        
p1 = Person("Shawon" , 20)
print(p1.name)