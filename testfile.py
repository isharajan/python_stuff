fname = input("Enter file name: ")
fh = open(fname)
#r = fh.read()
lst = []
for line in fh:
    word = line.split()
    print(word)
    for w in word:
        #print(w)
    	if(w not in lst):
        	lst.append(word)
print(lst.sort())

