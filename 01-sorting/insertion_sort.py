def insertion_sort(a):
    a=a.copy()
    for i in range(1,len(a)):
        x=a[i]; j=i-1
        while j>=0 and a[j]>x: a[j+1]=a[j]; j-=1
        a[j+1]=x
    return a

if __name__=="__main__": print(insertion_sort([5,2,9,1]))