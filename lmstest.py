class Book():
	bkid = 0
	def __init__(self,bname):
		self.bname = bname
		self.bid = Book.bkid
		Book.bkid = Book.bkid+1
		self.current_owner = None

	def __repr__(self):
		 return self.bname


class Person():
	pid = 0
	def __init__(self,name):
		self.name = name
		self.pid = Person.pid
		Person.pid = Person.pid +1
		self.books =[]


class Library():

	admin = Person('admin')
	def __init__(self,books=[]):
		self.books = []
		for book in books:
			book.current_owner = Library.admin
			self.books.append(book)

	def buy_book(self,book_name,person):
		for bk in self.books:
			if(bk.bname == book_name and bk.current_owner is Library.admin):
				bk.current_owner = person
				person.books.append(bk)
				return True
		return False

	def submit(self,person,book):
		book.current_owner = Library.admin
		person.books.remove(book)

	def add(self,book):
		book.current_owner = Library.admin
		self.books.append(book)


	def get_availablebooks(self):
		available_books =[]
		for bk in self.books:
			if(bk.current_owner is Library.admin):
				available_books.append(bk) 
		return available_books

	def get_bookstatus(self):
		for book in self.books:
			print (book.bname,book.current_owner.name)


	def __repr__(self):
		 return self.book_name

booklst =['tamil','english','maths','science','social']
objlst =[]
for book_name in booklst:
	bo=Book(book_name)
	objlst.append(bo)


p = Person('isha')
l = Library(objlst)
