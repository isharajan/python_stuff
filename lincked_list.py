class Node():
    def __init__(self,data):
        self.data = data
        self.nxt =None

    @staticmethod
    def display(head):
        temp=head
        while(temp.nxt!=None):
            print("%s-->"%(temp.data),end=" ")
            temp = temp.nxt
        print("%s-->"%(temp.data))


    @staticmethod
    def insert_lst(data,head):
        node = Node(data)
        temp=head
        while(temp.nxt!= None):
            temp=temp.nxt
        temp.nxt = node
        Node.display(head)
        return head

    @staticmethod
    def insert_fst(data,head):
        node = Node(data)
        node.nxt = head
        head = node
        Node.display(head)
        return head


    @staticmethod
    def remove_fst(head):
        temp = head
        head = head.nxt
        temp.nxt = None
        Node.display(head)
        return head


    @staticmethod
    def remove_lst(head):
        temp = head
        if(temp.nxt==None):
            return None
        while(temp.nxt.nxt!=None):
            temp = temp.nxt
        temp.nxt = None
        Node.display(head)
        return head

head = Node(10)
head=Node.insert_lst(20,head)
head=Node.insert_lst(30,head)
head=Node.insert_lst(40,head)
head=Node.insert_lst(50,head)
head=Node.insert_lst(60,head)

head=Node.insert_fst(9,head)
head = Node.insert_fst(8,head)

head=Node.remove_lst(head)
head=Node.remove_lst(head)

head = Node.remove_fst(head)
head = Node.remove_fst(head)