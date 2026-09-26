def interpolation_search(a,target):
    lo,hi=0,len(a)-1
    while lo<=hi and a[lo]<=target<=a[hi]:
        if a[hi]==a[lo]: return lo if a[lo]==target else -1
        p=lo+(target-a[lo])*(hi-lo)//(a[hi]-a[lo])
        if a[p]==target:return p
        if a[p]<target:lo=p+1
        else:hi=p-1
    return -1

if __name__=="__main__": print(interpolation_search([1,2,4,8,16],8))