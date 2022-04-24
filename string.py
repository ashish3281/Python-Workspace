#array of bytes
#declare a strings="  "
#string are unicode representation like ascii-A=65,a=97
#slice take place because it is accesable (ordered)
# ######################################################################
# sting formatting
x="apple"
y='apple'
print(x)
print(y)
z="""apple"""
print(z)
s='hi i\'m ashish'#'hi i'm ashish'  give an error
print(s)
q='''hi i'am ashish'''
print(q)
q="she said,\"hello\""
print(q)
##################################################################################3
age = 20
txt = "My name is Ashish, and I am {} year old"
print(txt.format(age))
s={"i am {} year old".format(age)}
print(s)
s="{1} {0} {2} {3}".format("how","helo","are","you")
print(s)
s="{0:b}".format(10)#convert binary conversion
print(s)
s="{0:b}".format(2)
print(s)