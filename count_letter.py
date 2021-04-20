mystr =raw_input("enter string : ")
print("====")
di = {}
def count_letter(mystr):
	for k in mystr:
		try:
			di[k] = di[k]+1
		except KeyError:
			di[k] = 1
	print di
count_letter(mystr)



fruits = {1:"apple",2:"orange",3:"banana"}
def update_dict():
	for k in fruits:
		if(fruits[k]=="pine"):
			fruits[k] = 'mango'
		fruits[3]='xxx'
	print fruits
update_dict()


numbers = {1:10,2:20,3:30,4:40,5:50}
def update_no():
	for k in numbers:
		print  numbers[k]
		if(numbers[k] >40):
			print numbers[k]                        
update_no()




	



