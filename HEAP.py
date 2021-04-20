class heaparr():
    
    @staticmethod
    def adjust(arr,dindex):
        if(dindex!=1):
            
            pindex = dindex//2
            if(arr[pindex-1] < arr[dindex-1]):
                temp = arr[pindex-1]
                arr[pindex-1] = arr[dindex-1]
                arr[dindex-1] = temp
                heaparr.adjust(arr,pindex)
            
    @staticmethod        
    def swap(arr,pindex,dindex):
        temp = arr[pindex]
        arr[pindex] = arr[dindex]
        arr[dindex] = temp
        
        
    @staticmethod
    def insert(arr,data):
        arr.append(data)
        dindex = len(arr)
        heaparr.adjust(arr,dindex)
        print (arr)

    @staticmethod    
    def delete(arr):
        print(arr)
        if(len(arr) >0):
            lenth = len(arr)
            temp = arr[0]
            arr[0] = arr[lenth-1]
            arr[lenth-1] = temp
            arr.pop()
            return heaparr.deladjust(arr,1)
            
    @staticmethod       
    def deladjust(arr,pindex):
        lenth = len(arr)
        lindex = 2*pindex
        rindex = lindex+1
              
        if((lindex <= lenth and rindex<=lenth) and (arr[lindex-1]>=arr[rindex-1])):
            if(arr[lindex-1]>arr[pindex-1]):
                heaparr.swap(arr,pindex-1,lindex-1)
                heaparr.deladjust(arr,lindex)
                
        if((rindex <= lenth and lindex<=lenth) and (arr[rindex-1]>=arr[lindex-1])):
            if(arr[rindex-1]>arr[pindex-1]):
                heaparr.swap(arr,pindex-1,rindex-1)
                heaparr.deladjust(arr,rindex)
            
arr = []
heaparr.insert(arr,20)
heaparr.insert(arr,100)
heaparr.insert(arr,30)
heaparr.insert(arr,50)
heaparr.insert(arr,5)
heaparr.insert(arr,200)
heaparr.insert(arr,105)
heaparr.delete(arr)

