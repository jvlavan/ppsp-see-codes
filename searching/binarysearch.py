def binarysearch(n,val):
    low=0
    high=len(n)-1
    while(low<=high):
        mid=(low+high)//2
        if(n[mid]<val):
            low=mid+1
        elif(n[mid]>val):
            high=mid-1
        else:
            return(mid)

    return -1        
a=[4,5,8,9,12,34,76] 
val=12
print(binarysearch(a,val))
print("The element found at {}".format(binarysearch(a,val)+1))            

