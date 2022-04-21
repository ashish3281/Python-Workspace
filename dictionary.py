# collection of data Value in the form of key value paired
# 3.7 python --dictionary Ordered
# store key value pair 
# {rollno:1}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict[4] ="d"#new key and value
print(thisdict)
thisdict["brand"]="swift"#update value
print(thisdict)
x=thisdict.get("brand")
print(x)
#########################################################################################
#dictionary in dictionary
y={"name":"ashish","rollno":206010,"z":{"name":"rohit","rollno":232242}}
print(y)
print(y["z"])
print(y["z"]["name"])
#############################################################################################
#deleting element in dictionay
del thisdict["model"]
print(thisdict)
del y["z"]["rollno"]
print(y)
z=thisdict.pop("brand")#pop will take key and store it in the new value
#z=thisdict.pop()#pop expected at least one argument
print(z)
q=thisdict.popitem()
print(q)
thisdict.clear()
print(thisdict)