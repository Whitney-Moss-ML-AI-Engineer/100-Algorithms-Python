def merge_sort(a):
    if len(a)<=1:return a
    m=len(a)//2; L=merge_sort(a[:m]); R=merge_sort(a[m:]); out=[]; i=j=0
    while i<len(L) and j<len(R): out.append(L[i] if L[i]<=R[j] else R[j]); i+=L[i]<=R[j]; j+=L[i-1]>R[j-1] if i and j else 0
    return out+L[i:]+R[j:]

if __name__=="__main__": print(merge_sort([5,2,9,1,3]))