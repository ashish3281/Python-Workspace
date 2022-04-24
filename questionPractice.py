l=[1,0,4,3,2,5,7,9,4,6]
indices={}
for i in range(len(l)):
    num1=l[i]
    for j in  range(i+1,len(l)):
        if num1+l[j]==5:
            indices[i]=j
print(indices)
#palindrome number
#nearest to the target
