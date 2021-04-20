#def get_key(n):
	#k=d1.get(n)
	#print k

def my_key(m):
	f = False
	for key in d1:
		if(key==m):
			f = True
			print d1[key]

	if(f):
		print(d1[key])
	else:
		print("key not found")




d1 = {1:"tamil",2:"english",3:"maths",4:"science",5:"social"}
print("keys : ")
for k in d1:
	print k

#n = int(input("enter the key :"))
m = int(input("enter your key :"))
#get_key(n)
my_key(m)
