#linear data type,collection of hetrogeneous data,ordered,changeable,mutable
mylist=[1,2,3,4,5,6]#ordered means same output obtained eg set {1,2,3,4,2} output is {1,4,3,2}
#append --only one element can be append
a=[1,2,3,4]
a.append([5,6])
print("after append ",a)

b=[1,2,3,4]
b.append(5)
print(b)
#extend
c=[1,2,3,4]
c.extend([5,6,7])
print("after expend ",c)

x=[1,2,3,4]
y=[]
for i in range(len(x)):
    y.extend([a[i]*a[i]])
print(y)
###################################################################################
# #index
# print(mylist[ :len(mylist)])
# #print begining to end
# print(mylist[0: ])
# #from 0 to end point
# #mylist[start:end]
# #mylist[ : ]  print whole list
# #reversing the list
# print(mylist[ ::-1]
      
# #also do reversing (a[ :-index])
# # x =['a','b','c']
# # x.remove("b")
# # print(x)

# # if element is not present in the list then give an error
#######################################################################
#list comprehension--simplify the code in one line
p=[]
q=[1,2,3,4,5,6,7,89,8]
r=[i for i in range(100)]
print(r)
import string as str
for i in str.ascii_lowercase:
    
    print(i)
g=[x**2 for x in range(10)]
print(g)
t=[x**2 for x in range(10) if x%2==1]
print(t)
##################################################################################
#check number is present or not
j=[x for x in range(10)]
element=5
for i in j:
    if i==element:
        print("yes")
        break
    else:
        continue
########################################################################################
#sorting
k=[3,54,566,343,87]
k.sort()    
print(k)
k.sort(reverse=True)
print("reversing of k",k)    

#######################################################################################
#find the max and min element in a list
l=[312,464,656,5,56,45]
max=0
min=l[0]
for i in l:
    if (i>max):
        max=i
print(max)
for i in range(len(l)):
    if (l[i]<min):
        min=l[i]
print(min)
#mylist=[343,5,65,6]
#max=0
#for i in range(len(mylist))
#if mylist[i]>max
#max=mylist[i].copy()
# print(max)

######################################################################################
#average
c=[2,34,545,4546,4]
sum=0
average=0
for i in range(len(c)):
    sum=sum+c[i]
    average=sum/len(c)
print(sum)
print(average)
    
