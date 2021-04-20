def mergeSort(nlist):
   # print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        #print ("lefthalf",lefthalf)
        righthalf = nlist[mid:]
        #print ("righthalf",righthalf)
 
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0      
        #for e in lefthalf:
         #   print ("---e-----",e)
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                #print("lefthalf[i]",lefthalf[i])
                #print("righthalf[j]",righthalf[j])
                #print("====================================")
                nlist[k]=lefthalf[i]
                i=i+1
                #print("i =",i)
                #print("==========================================")
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1
 
        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
           # print("------nlist[k]---------",nlist[k])
            i=i+1
            k=k+1
 
        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",nlist)
 
#nlist = [3,1,4,1,5,9,2,6,5,4]
nlist = [3000,30,300,3,10]
mergeSort(nlist)
print(nlist)
