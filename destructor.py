# class employee:
#     def __init__(self):
#        print("emploee created")
#     def __del__(self):
#         print("destructer called")
# def create_obj():
#     print("making obj")
#     obj=employee()
#     print("function end")
#     return obj
# print("calling create_obj() function")
# obj = create_obj()
# print("program end")
#########################################################################
class A:
    def __init__(self,bb):
        self.b=bb
class B:
    def __init__(self):
            self.a=A(self)
    def __init__(self):
            print("die")
def fun():
    b=B()
fun()