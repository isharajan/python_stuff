def partition(arr,low,high):
	pivot = arr[high]
	pi_index = low
	for i in range(low,high):
		if(arr[i] <= pivot):
			arr[pi_index],arr[i] = arr[i],arr[pi_index]
			pi_index = pi_index + 1
	arr[pi_index], arr[high] = arr[high],arr[pi_index]
	return pi_index

def quicksort(arr,low,high):
	if(low<high):
		pi = partition(arr,low,high)
		quicksort(arr,low,pi-1)
		quicksort(arr,pi+1,high)


arr = [30,40,10,20,45,68,100,25]
quicksort(arr,0,len(arr)-1)
print arr