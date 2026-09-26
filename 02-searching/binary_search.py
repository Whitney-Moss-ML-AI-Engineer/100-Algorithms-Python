def binary_search(a,target):
    lo,hi=0,len(a)-1
    while lo<=hi:
        m=(lo+hi)//2
        if a[m]==target:return m
        if a[m]<target:lo=m+1
        else:hi=m-1
    return -1

if __name__=="__main__": print(binary_search([1,2,4,7,9],7))