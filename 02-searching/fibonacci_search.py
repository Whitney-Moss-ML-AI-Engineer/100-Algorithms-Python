def fibonacci_search(a,target):
    fib2,fib1=0,1; f=fib1+fib2
    while f<len(a): fib2,fib1=fib1,f; f=fib1+fib2
    off=-1
    while f>1:
        i=min(off+fib2,len(a)-1)
        if a[i]<target:f,fib1,fib2=fib1,fib2,f-fib1; off=i
        elif a[i]>target:f,fib1,fib2=fib2,fib1-fib2,fib2-(fib1-fib2)
        else:return i
    return off+1 if fib1 and off+1<len(a) and a[off+1]==target else -1

if __name__=="__main__": print(fibonacci_search([1,2,4,8,16],8))