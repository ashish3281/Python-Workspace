l1=[1,2,3,4,5,6,7,8]
l2=[2,4,7]
list=[]
for i in l1:
        if i not in l2:
            list.append(i)
print(list)
    
    
s1={1,2,3,4}
s2={2,3}
for i in s1:
    if i not in s2:
        print(i)