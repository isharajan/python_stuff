# passing with named perameter

def get_last2nos(l,n2=2):
	last_2no = l[-n2:]
	return last_2no

def get_first3nos(l,n1=3):
	first_3no =l[:n1]
	return first_3no

my_l = [10,100,1000,20,200,2000,3,50,60,70]
result = get_last2nos(n2=2,l=my_l)
print(result)
print("")
result = get_first3nos(my_l,2)
print(result)