class Book:

	BID = 0

	def __init__(self,name):
		self.name = name
		self.bid = Book.BID
		Book.BID+=1
		self.current_owner = None

class Lib():
	def __init__(self,books=[]):
		self.books = []

	def get_book(self, book_name, person):
		for book in self.books:
			if book.name == book_name:
				book.current_owner = person
				return True
		return False

class Person():
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.books = []


# class P():

# 	def __init__(self,x,y):
# 		self.x = x
# 		self.y = y

# 	def dist(self,p2):
# 		return ((p2.x-self.x)**2+(p2.y-self.y)**2)**0.5


# def dist(x1,y1,x2,y2):
# 	return ((x2-x1)**2+(y2-y1)**2)**0.5


