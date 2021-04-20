def listofbooks():
	print("list of books in library:")
	print("1.tamil")
	print("2.tamil")
	print("3.english")
	print("4.english")
	print("5.maths")
	print("6.maths")
	print("7.science")
	print("8.science")
	print("9.social")
	print("10.social")

def getbook():
	n = int(input("enter book id:"))
	library.pop(n)
	print("you got the book")

def selectoption():
	print("1.list out books")
	print("2.get books")
	print("3.return book")
	print("4.exit")
	choice=int(input("enter your choice:"))



library ={101:"tamil",102:"tamil",103:"english",104:"english",105:"maths",106:"maths",107:"science",108:"science",109:"social",110:"social"}
selectoption()

if(choice==1):
	listofbooks()
else:
	print("some problem")



