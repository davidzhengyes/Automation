import ast

file=open("visited.txt","w")

mySet={1,2,3,4,5,6,7}

file.write(str(mySet))
file.close()


file=open("visited.txt","r")
newset=ast.literal_eval(file.read())
file.close()

###fFILES CANNOT BE EMPTY.
print(newset)
newset.add(12)
print(newset)


