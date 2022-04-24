n=43
flag=False
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
if flag:
    print(n,"this is not a prime number")  
else:
    print(n,"this is a prime number")    