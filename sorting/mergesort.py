#merge sort
def mergesort(n):
    if(len(n)>1):
        mid=len(n)//2
        left=n[:mid]
        right=n[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while(i<len(left)and(j<len(right))):
            if(left[i]<right[j]):
                n[k]=left[i]
                i+=1
                k+=1
            else:
                 n[k]=right[j] 
                 k+=1
                 j+=1  
        while(i<len(left)):
            n[k]=left[i] 
            k+=1
            i+=1      
        while(j<len(right)):
            n[k]=right[j]
            j+=1
            k+=1
a=[39,12,11,9,1]
mergesort(a)
print(a)            
