###############################################################
#simple method to define a class

# class Dog:
#     att1="mammal"
#     att2="dog"
#     def fun(self):
#         print("I am a",self.att1)
#         print("I am a ",self.att2)
# rodger=Dog()
# print(rodger.att1)
# rodger.fun()

###############################################################
#init  method

# class Person:
#     def __init__(self,name): 
#         self.name=name
#     def say_hi(self):
#         print("Hello, my name is ",self.name)
# p=Person('Ashish')
# p.say_hi()           

#################################################################
class Dog:
    animal="dog"
    def __init__(self,breed,color):
        self.breed=breed
        self.color=color
rodger=Dog("pub","brown")
buzo=Dog("bulldog","black")
print("rodger details :")
print("rodger is a ",rodger.animal)
print("breed",rodger.breed)
print("color",rodger.color)
print("buzo details :")
print("buzo is a ",buzo.animal)
print("breed",buzo.breed)
print("color",buzo.color)
print(Dog.animal)