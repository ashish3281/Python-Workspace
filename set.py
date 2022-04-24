#unordered,unchangeable,do not allow duplicate,imutable,primitive
a={1,2,3}
#a[1]=5#error

print (a)
b={1,2,3,2,3}
b.add(8)
print(b)
#b.add(6,7)
#print(b)  gine an error
#b.add([9,6])
#print(b) give an error
b.add((9,7))#tuple is mutable
print(b)
c={343,546,5766}
d=[1,2,3,546]
c.update(d)
print(c)
#access an set
#we can not use index method to access the set because they are unordered
f={1,2,3,4}
for i in f:
    print(i)
#remove an element
f.remove(3)  #remove 8 but it is not present give an error
print(f)
f.discard(8)
print(f)#not given an error
g={1,2,3,4,5}
g.pop()#any element can get pop because it is unorderd
print(g)
g.clear()
print(g)
############################################################################
#frozen set--no change are allowed
a=frozenset({1,2,3})