names=["a","b","c","d","e"]
#print(len(names)) #length of the list
#for i in range(len(names)): i mean iterator: con chayj
#    print(names[i])

#foreach
no=1
for n in names:
    #print(no,". ", n,sep="")
    #string format
    message="{0}.  {1}".format(no,n)
    print(message)
    no=no+1 # no +=1
# for i (cach khac)
