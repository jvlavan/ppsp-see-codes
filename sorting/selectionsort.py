#selection sort 

def selectionsort(n):
    for i in range(len(n)-1):
        min_index=i
        for j in range(i+1,len(n)):
            if(n[min_index]>n[j]):
                min_index=j
        n[i],n[min_index]=n[min_index],n[i]
size=int(input("Enter the list size:"))
arr=[]
for f in range(size):
    f=int(input("Enter the element:"))
    arr.append(f)
print("The orginal list:",arr)
selectionsort(arr)
print("The sorted list:",arr)
