def bucket_sort(a,buckets=10):
    if not a:return []
    lo,hi=min(a),max(a); out=[[] for _ in range(buckets)]
    for x in a: out[min(buckets-1,int((x-lo)/(hi-lo+1e-12)*buckets))].append(x)
    return [x for b in out for x in sorted(b)]

if __name__=="__main__": print(bucket_sort([.42,.32,.33,.52,.37,.47,.51]))