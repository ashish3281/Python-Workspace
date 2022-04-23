a=[1,2,3,4]
a.append([5,6])
print("after append ",a)

b=[1,2,3,4]
b.append(5)
print(b)

c=[1,2,3,4]
c.extend([5,6,7])
print("after expend ",c)

x=[1,2,3,4]
y=[]
for i in range(len(x)):
    y.extend([a[i]*a[i]])
print(y)
