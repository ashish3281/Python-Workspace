
#########single inheritance###############

# class person(object):
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
# class employee(person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#         person.__init__(self,name,idnumber)
# a=employee("rahul",8860,2000000,"intern")
# a.display()


# #############################################################################
###### multiple inheritance############

# class base1(object):
#     def __init__(self):
#         self.str1="ashish"
#         print("base1")
# class base2(object):
#     def __init__(self):
#         self.str2="goyal"
#         print("base 2")
# class derived (base1,base2):
#     def __init__(self):
#         base1.__init__(self)
#         base2.__init__(self)
#         print("derived")
#     def printstrs(self):
#         print(self.str1,self.str2)
# obj=derived()
# obj.printstrs()


###################################################################
####### multilevel inheritance#########

# class base(object):
#     def __init__(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
# class child(base):
#     def __init__(self,name,age):
#         base.__init__(self,name)
#         self.age=age
#     def getage(self):
#         return self.age
    
# class grandchild(child):
#     def __init__(self,name,age,address):
#         child.__init__(self,name,age)
#         self.address=address
#     def getaddress(self):
#         return self.address
# g=grandchild("ashish",20,"Haryana")
# print(g.getname(),g.getage(),g.getaddress())


######################################################################################
############ hierarchical inhertance #################

# class parent:
#     def func1(self):
#         print("this function is in parent class")
# class child1(parent):
#     def func2(self):
#         print("this function is in child1")
# class child2(parent):
#     def func3(self):
#         print("this function is child 2")
# object1 = child1()
# object2 = child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


##############################################################################
##### hybrid inheritance #####

# class school:
#     def func1(self):
#         print("this func is in school")
# class student1(school):
#     def func2(self):
#         print("this function is in student1")
# class student2(school):
#     def func3(self):
#         print("this function is in student 2")
# class student3(student1,student2):
#     def func4(self):
#         print("this function is in student3")
# object=student3()
# object.func1()
# object.func2()
# object.func3()
# object.func4()
