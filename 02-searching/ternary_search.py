def ternary_search(a,target):
    lo,hi=0,len(a)-1
    while lo<=hi:
        d=(hi-lo)//3; m1=lo+d; m2=hi-d
        if a[m1]==target:return m1
        if a[m2]==target:return m2
        if target<a[m1]:hi=m1-1
        elif target>a[m2]:lo=m2+1
        else:lo,hi=m1+1,m2-1
    return -1

if __name__=="__main__": print(ternary_search([1,2,3,4,5,6,7],5))