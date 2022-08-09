def toh(n,s,d,a):
    if (n==1):
        print("move disk from",s," to ",d)
    else:
        toh(n-1,s,a,d)
        print("move disk from",s," to ",d)
        toh(n-1,a,d,s) 
n=3
toh(n,1,2,3)
