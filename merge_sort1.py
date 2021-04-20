def my_merge_sort(mylist):
	if(len(mylist) > 1):
		mid = len(mylist)//2
		left_arr = mylist[:mid]
		right_arr = mylist[mid:]

		my_merge_sort(left_arr)
		my_merge_sort(right_arr)

		i=0
		j=0
		k=0

		while (i<len(left_arr) and j<len(right_arr)):
			if(left_arr[i] < right_arr[j]):
				mylist[k] = left_arr[i]
				i = i+1
			else:
				mylist[k] = right_arr[j]
				j = j+1

			k = k+1
			
		while i < len(left_arr):
			mylist[k] = left_arr[i]
			i = i+1
			k = k+1

		while j < len(right_arr):
			mylist[k] = right_arr[j]
			j = j+1
			k = k+1

mylist = [4,0,78]
my_merge_sort(mylist)
print mylist


