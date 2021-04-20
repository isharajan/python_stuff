def mergesort(arr):
	if (len(arr)>1):
		mid = len(arr)//2
		lhs = arr[:mid]
		rhs = arr[mid:]

		mergesort(lhs)
		mergesort(rhs)

		i=0
		j=0
		k=0

		while(i<len(lhs) and j<len(rhs)):
			if (lhs[i] > rhs[j]):
				arr[k] = lhs[i]
				i = i+1
			else:
				arr[k] = rhs[j]
				j = j+1
			k = k+1

		while(i<len(lhs)):
			arr[k] = lhs[i]
			i = i+1
			k = k+1

		while(j<len(rhs)):
			arr[k] = rhs[j]
			j = j+1
			k = k+1
arr = [45,80,30,100,2,34,98,700,20,40,52,20]
mergesort(arr)
print arr




