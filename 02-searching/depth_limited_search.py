def depth_limited_search(graph,start,target,limit):
    def dfs(v,d):
        if v==target:return [v]
        if d==0:return None
        for n in graph.get(v,[]):
            r=dfs(n,d-1)
            if r:return [v]+r
    return dfs(start,limit)

if __name__=="__main__": print(depth_limited_search({'A':['B'],'B':['C']},'A','C',2))