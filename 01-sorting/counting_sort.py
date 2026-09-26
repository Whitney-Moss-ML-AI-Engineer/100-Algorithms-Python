def counting_sort(a):
    if not a:return []
    lo,hi=min(a),max(a); c=[0]*(hi-lo+1)
    for x in a:c[x-lo]+=1
    return [i+lo for i,n in enumerate(c) for _ in range(n)]

if __name__=="__main__": print(counting_sort([4,2,2,8,3,3,1]))