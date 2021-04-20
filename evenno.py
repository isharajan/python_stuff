
#Given an array of integers A sorted in non-decreasing order, 
#return an array of the squares of each number, also in sorted non-decreasing order.

#program g

d=[]
def evenno(n):
	if(n>10):
		Q = n/10
		r = n%10
		d.append(r)
		#print (l)
		if(Q>10):
			evenno(Q)
		else:
			d.append(Q)
			#print(l)
	else:
		d.append(n)
	
	return len(d)
        


def counteven1(lst):
	count =0
	for n in lst:
		if(n%2 ==0):
			count = count+1
	return count

def counteven(a):
	lst =[]
	for n in a:
		res = evenno(n)
		lst.append(res)
	cut = counteven1(lst)
	return cut


a=[3456,22,33,5,23,4,44,25]
output = counteven(a)
print("output",output)
