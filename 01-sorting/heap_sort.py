import heapq
def heap_sort(a):
    h=a.copy(); heapq.heapify(h); return [heapq.heappop(h) for _ in range(len(h))]

if __name__=="__main__": print(heap_sort([5,2,9,1]))