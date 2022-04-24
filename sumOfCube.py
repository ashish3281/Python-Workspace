#for cube of n natural number
n=4   #n=int(input())
sum=0
for i in range(0,5):    #range(0,n+1)
    i=i*i*i
    sum=sum+i
print("square of sum is",sum)