#Given an array arr of integers, check if there exists two integers N and M such that
# N is the double #of M ( i.e. N = 2 * M).


def isdbl(dbl_lst,a):
	for d in dbl_lst:
		for i in a:
			if(i == d):
				return True
	return False


def dbl(m):
	n = 2*m
	return n


a =[-2,3,4,2]
dbl_lst =[]
for m in a:
	res = dbl(m)
	dbl_lst.append(res)
output = isdbl(dbl_lst,a)
print("output",output)
