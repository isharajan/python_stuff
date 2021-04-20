arr = [10,80,30,90,40,50,70]
#arr=[50,70,30,20,10.55,100,2]
i = -1
j = arr[0]
pi = arr[-1]
for e in range (len(arr)):
	#print(arr[e])
	if(arr[e] <= pi):
		#print arr[j]
		i = i+1
		arr[i],arr[e] = arr[e],arr[i]
arr[i],arr[e] = arr[e],arr[i]
	#else:
	#	j = j+1
print ("quick sort",arr)