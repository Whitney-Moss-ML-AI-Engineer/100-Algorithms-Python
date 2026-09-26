def exponential_search(a,target):
    if not a:return -1
    if a[0]==target:return 0
    i=1
    while i<len(a) and a[i]<target:i*=2
    lo,hi=i//2,min(i,len(a)-1)
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==target:return m
        if a[m]<target:lo=m+1
        else:hi=m-1
    return -1

if __name__=="__main__": print(exponential_search([1,2,4,8,16],16))