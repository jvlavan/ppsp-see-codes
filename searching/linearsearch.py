def linearsearch(n,sh):
    for i in range(len(n)):
        if(n[i]==sh):
            return(i+1)
    return(-1)   



size=int(input("Enter the list size:"))
arr=[]
for f in range(size):
    f=int(input("Enter the element:"))
    arr.append(f)
sh=int(input("Enter the search element:"))
a=linearsearch(arr,sh)
if(a!=-1):
    print("Element found at:",a)
else:
    print("element not found")
