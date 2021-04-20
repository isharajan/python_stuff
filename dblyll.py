class Node():
	def __init__(self,data,nxt,prev):
		self.data  = data
		self.nxt = None
		self.prev = None

	@staticmethod
	def insert_lst(data,head):
		node = Node(data)
		temp = head
		while(temp.nxt!=None):
			temp=temp.nxt
		temp.nxt = node
		node.prev = temp
		temp.nxt = null




