
# SELECTION SORT
def find_min(l):
	minimum = l[0]
	for i in range (len(l)):
		if(l[i] < minimum):
			minimum = l[i]
	return minimum

def find_max(l):
	maximum = l[0]
	for i in range (len(l)):
		if(l[i] > maximum):
			maximum = l[i]
	return maximum

def sort_ascending(l):
	sorted_li_as = []
	for i in range(len(l)):
		min_val = find_min(l)
		sorted_li_as.append(min_val)
		l.remove(min_val)
	return sorted_li_as
	

def sort_descending(l):
	sorted_li_des = [] 
	for i in range(len(l)):
		max_val = find_max(l)
		sorted_li_des.append(max_val)
		l.remove(max_val)
	return sorted_li_des
	


l = [10,5,6,25,90,3]
#list1 = sort_ascending(l)
#print  ("ascending order ",list1)
        
list2 = sort_descending(l)
print ("descending order ",list2)

#print("================ selection sort ==============")


#def selecction_sort(l):
#	for i in range(len(l)):
#		min_val = min(l)
#		new_list.append(min_val)
#		l.remove(min_val)
#	print new_list

#l = [10,5,6,25,90,3]
#new_list = []
#sselecction_sort(l)


