#readlines() : reads all the data from the file and returns the data
#as list, each line will be the list element.

#filevariable.readlines()

file1 = open("E:/Rahul/Demo.txt")
data = file1.readlines()
file1.close()
#print(data)
for x in data:
    #print(x)
    print(x.strip())