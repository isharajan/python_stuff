def mul_arg1(*a):
	return max(a) 
	       # return arguments as a tuple
result = mul_arg1(2,3,4,5,10)    # unknown no.of.arguments can be give as a input
print ("maximum is : ",result)
print("")

def mul_arg2(*a):
	return min(a) # return arguments as a tuple
result = mul_arg2(2,3,4,5,10)    # unknown no.of.arguments can be give as a input
print("minimum is : ",result)
print("")



def mul_arg3(**a):
	return max(a)         # return arguments as a dictionary by passing a named perameter
result = mul_arg3(a=10,b=20,c=30)
print ("maximum is : ",result)
print("")

def mul_arg4(**a):
	return min(a)         # return arguments as a dictionary by passing a named perameter
result = mul_arg4(a=10,b=20,c=30)
print("minimum is : ",result)

