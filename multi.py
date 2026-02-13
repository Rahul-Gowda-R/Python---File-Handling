#working with multiple files

#master file and transaction file
#master file and detail file
#parent file and child file

#master file will have unique data with id's 
#trasnaction file uses the data of master file

#ex.master file:101,Amar
#in trans file:
    #101,2000
    #101,2000

#whwn workingf with multiple files all files should have at least one common column

#1.read all master file and create dictionary

dfile=open("dep.txt")

dhead=dfile.readline()
ddata=dfile.readlines()
dfile.close()

depdict={}

for x in ddata:
    d=x.strip().split(',')
    depdict[d[0]]=d[1]
print(depdict)



#read the data from empfile.txt AND MAP DNO WITH DEPDICT TO GET DEPNAME


efile=open("dep.txt")
ehead=efile.readline()
edata=efile.readlines
efile.close()

flist=[]

for x in data:
    #print(x)
    w=x.strip().split(',')
    #print(w)
    depname=depdict.get(w[-1])
    tup=(w[0],w[1],w[2],w[3],depname)
    flist.append(tup)

for x in list:
    print()

