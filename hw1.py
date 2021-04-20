def get_upper(l):
	nlu = []
	for ch in range(len(l)):
		if(l[ch].isupper()):
			nlu.append(l[ch])
	return nlu


def get_lower(l):
	nlo = []
	for ch in range(len(l)):
		if(l[ch].islower()):
			nlo.append(l[ch])
	return nlo

def get_digit(l):
	nld = []
	for ch in range(len(l)):
		if(l[ch].isdigit()):
			nld.append(l[ch])
	return nld

l = ["1","2","3","a","A","b","B","d","D"]
result = get_upper(l)
print("The upper case are :",result)
print("length of uppercase",len(result))
print("")

result = get_upper(l)
print("The upper case are :",result)
print("length of uppercase",len(result))
print("")

result = get_lower(l)
print("The lower case are :",result)
print("length of lowercase",len(result))
print("")


result = get_digit(l)
print("The digits are :",result)
print("length of digit",len(result))
print("")



