def linear_search(a,target):
    for i,x in enumerate(a):
        if x==target:return i
    return -1

if __name__=="__main__": print(linear_search([4,2,7,1],7))