def insertionsort(n):
    for i in range(1,len(n)):
        loc=i
        temp=n[loc]
        while((n[loc-1]>temp)and(loc!=0)):
            n[loc]=n[loc-1]
            loc-=1
        n[loc]=temp 
size=int(input("Enter the list size:"))
arr=[]
for f in range(size):
    f=int(input("Enter the element:"))
    arr.append(f)
print("The orginal list:",arr)
insertionsort(arr)
print("The sorted list:",arr)
              
