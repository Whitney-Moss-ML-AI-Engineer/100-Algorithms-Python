def quick_sort(a):
    if len(a)<=1:return a
    p=a[len(a)//2]
    return quick_sort([x for x in a if x<p])+[x for x in a if x==p]+quick_sort([x for x in a if x>p])

if __name__=="__main__": print(quick_sort([5,2,9,1,3]))