##############################################
#local variable
def myfunc():
    x=300
    print(x)
myfunc()
################################################
#global variable
x=300
def myfunc():
    print(x)

myfunc()
print(x)
######################################################
x=300
def myfunc():
    x=200
    print(x)

myfunc()
print(x)
##############################################################
def mufunc():
    global x
    x=300
myfunc()
print(x)
##############################################################
x=300
def mufunc():
    global x
    x=200
myfunc()
print(x)
#############################################################
def myfunc():
    x=300
    def my_innerfunc():
        print(x)
    my_innerfunc()
myfunc()
    