def create_dict(key,value):
	new_dict[key]=value
	print new_dict

def get_keys(n):
	for i in range(n):
		key = input("enter key : ")
		value = input("enter value : ")
		create_dict(key,value)

def use_dictfun():
	print("using dict() ")
	

new_dict = {}
n = int(input("enter the no.of. keys : "))
get_keys(n)

new_dict['fruit']='apple'
print new_dict


new_dict.update({2000:" holy "})
print new_dict


new_dict[100]=100
print new_dict

new_dict.update({3000:" holly "})
print new_dict
