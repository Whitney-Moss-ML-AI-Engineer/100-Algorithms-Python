def selection_sort(a):
    a=a.copy()
    for i in range(len(a)):
        k=min(range(i,len(a)),key=a.__getitem__); a[i],a[k]=a[k],a[i]
    return a

if __name__=="__main__": print(selection_sort([5,2,9,1]))