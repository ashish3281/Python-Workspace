a=[1,2,3,4]
b=[5,6,7,8]
merge_list=[]
for i in range(len(a)):
    merge_list.append(a[i])
    merge_list.append(b[i])
print(merge_list)
#[1,5,2,6,7,4,8]
#count even and odd number in a list
# list1=[1,2,3,4,5,6,7,8]
# countEven=0
# countOdd=0
# for i in range(0,8):
#     if(i%2==0):
#         countEven = countEven+1
#     else:
#         countOdd =countOdd+1
# print(countEven)
# print(countOdd)
# #reversing the list

# print(list1[ ::-1])
# list1.reverse()
# print(list1)
# #python count occurence of an number
# list2 = [1,2,3,2,2,4,5,6,7,2,3,4]
# x = 2
# count = 0
# for i in list2:
#    if (i == x):
#        count =count+1
# print(count)
# #swapping in list
# list3=[1,2,3,4,5,6,7,8,9,10]
# temp=list3[0]
# list3[0]=list3[6]
# list3[6]=temp
# print(list3)