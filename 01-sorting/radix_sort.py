def radix_sort(a):
    a=a.copy(); exp=1
    while max(a,default=0)//exp:
        b=[[] for _ in range(10)]
        for x in a:b[(x//exp)%10].append(x)
        a=[x for bucket in b for x in bucket]; exp*=10
    return a

if __name__=="__main__": print(radix_sort([170,45,75,90,802,24,2,66]))