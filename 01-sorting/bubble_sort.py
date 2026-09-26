def bubble_sort(a):
    a=a.copy()
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if a[j]>a[j+1]: a[j],a[j+1]=a[j+1],a[j]
    return a

if __name__=="__main__": print(bubble_sort([5,2,9,1,5]))