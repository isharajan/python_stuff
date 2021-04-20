def partition(arr,low,high):
	pi = arr[low]
	i=low
	j=high

	while(i<j):
		while(arr[i]<pi):
			i = i+1
		while(arr[j]>pi):
			j = j-1
		if(i<j):
			arr[i],arr[j] = arr[j],arr[i]
	arr[pi],arr[j] = arr[j],arr[pi]
	return j


def qksort(arr,low,high):
	if(low<high):
		pi = partition(arr,low,high)
		qksort(low,pi)
		qksort(pi+1,high) 


arr = [12,100,23,45,60,90,700,1000,2]
qksort(arr,len(arr))
print arr