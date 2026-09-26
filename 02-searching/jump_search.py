import math
def jump_search(a,target):
    n=len(a); step=max(1,int(math.sqrt(n))); prev=0
    while prev<n and a[min(prev+step,n)-1]<target: prev+=step
    for i in range(prev,min(prev+step,n)):
        if a[i]==target:return i
    return -1

if __name__=="__main__": print(jump_search([1,2,3,4,5,6,7],6))