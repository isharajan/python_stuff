# BUBBLE SORT

def bubble_sort(l):
	length = len(l)
	for i in range(length):
		for j in range(length -1):
			#print(l[j],l[j+1])
			#print l
			if(l[j]>l[j+1]):
				l[j] ,l[j+1] = l[j+1],l[j]
				#print l 
	print ("sorted list : ",l)

l = [30,40,5,10,2]
bubble_sort(l)
