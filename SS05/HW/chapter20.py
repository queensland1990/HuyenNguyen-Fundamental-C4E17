letter_count={}
letter=['a','a','b','c','c','d','e','g','h','g','h']
for i in letter:
    letter_count[i]=letter_count.get(i,0)+1
#print(letter_count)
for key, value in letter_count.items():
    print(key,value)
