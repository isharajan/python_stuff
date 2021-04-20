#Given an array of integers A sorted in non-decreasing order,
# return an array of the squares of each number, also in sorted non-decreasing order.
def sqrofno(n):
	return n*n

def sqrarr(a):
	sqrl =[]
	for n in a:
		res = sqrofno(n)
		sqrl.append(res)
	return sorted(sqrl)


a =[-4,-1,0,3,10]
output = sqrarr(a)
print(output)