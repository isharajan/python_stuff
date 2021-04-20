booklib = {1: {"id" :1 ,"name":'tamil',"author":'narendar'}, 
	2:{"id":2,"name":'english',"author":'surendar'},
	3:{"id":3,"name":'maths',"author":'ravi'}
		
}

class book():
	booklst =[]	
	def __init__(self,bname,ids,author):
		self.bname = bname
		self.ids = ids
		self.author = author

#def listing():


def search():
	bookname =input("enter the bookname :")
	for book in booklib:
		if(booklib[book] is bookname):
			print (book,booklib[book])
		
	#print(len(booklib))
#search()

def borrow():
	bookid = int(input("enter bookid : "))
	booklib.pop(bookid)
	print ('the borrowed book {} is removed from library')
	print booklib
#borrow()

def update():
	bookid = int(input("enter bookid to update : "))
	bookname = input("enter bookname of bookid to update :")
	booklib.update({bookid:bookname})
	#booklib[bookid]	= bookname
	print ("library updated successfully")
	print booklib
#update()

def submit():
	bookid = int(input("enter bookid to submit : "))
	bookname = input("enter baaokname of bookid to submit : ")
	booklib[bookid] = bookname
	print('book is submitted')
	print booklib
#submit()
	

