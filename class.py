class Student():
	def _init_(self,m1,m2,m3,m4,m5):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
		self.m4 = m4
		self.m5 = m5

	def total(self):
		total = self.m1+self.m2+self.m3+self.m4+self.m5
		return total

cl = Student(10,10,10,10,10) 
cl.total()
print(cl.total)