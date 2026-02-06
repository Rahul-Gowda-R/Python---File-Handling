#reading data from empfile.txt and separate header from the data

empfile=open("E:/Rahul/emp.txt")
header=empfile.readline()
data=empfile.readlines()
empfile.close()

totsal=0

for x in data:
    w=x.strip().split(',')
    totsal+=int(w[2])

print(f"Total salary of the employees:{totsal}")