booklib = {1:"tamil", 2:"english",3:"maths",4:"science",5:"social",6:"tamil", 7:"english",8:"maths",9:"science",10:"social"}
def listing():
	for book in booklib:
		print (book,booklib[book])
listing()

def search():
	bookname =input("enter the bookname :")
	for book in booklib:
		if(booklib[book] is bookname):
			print (book,booklib[book])
		
	#print(len(booklib))
search()

def borrow():
	bookid = int(input("enter bookid : "))
	booklib.pop(bookid)
	print ('the borrowed book {} is removed from library')
	print (booklib)
borrow()

def update():
	bookid = int(input("enter bookid to update : "))
	bookname = input("enter bookname of bookid to update :")
	booklib.update({bookid:bookname})
	#booklib[bookid]	= bookname
	print ("library updated successfully")
	print (booklib)
update()

def submit():
	bookid = int(input("enter bookid to submit : "))
	bookname = input("enter baaokname of bookid to submit : ")
	booklib[bookid] = bookname
	print('book is submitted')
	print (booklib)
submit()
	



























