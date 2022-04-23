class a:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return self.a +b.a
obj1=a(1)
obj2=a(2)
obj3=a("ashish")
obj4=a("goyal")
print(obj1+obj2)
print(obj3+obj4)

#########################################################################
class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a+other.a , self.b+other.b
obj1=complex(1,6)
obj2=complex(2,3)
obj3=obj1+obj2
print(obj3)

##################################################################################
class a:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
obj1=a(2)
obj2=a(6)
if(obj1>obj2):
    print("obj1 is greater")
else:
    print("obj2 is greater")