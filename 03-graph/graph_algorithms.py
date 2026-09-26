from collections import deque
import heapq

def bfs(g,s):
 q=deque([s]); seen={s}; out=[]
 while q:
  u=q.popleft();out.append(u)
  for v in g.get(u,[]):
   if v not in seen:seen.add(v);q.append(v)
 return out

def dfs(g,s):
 seen=set();out=[]
 def go(u):
  if u in seen:return
  seen.add(u);out.append(u)
  for v in g.get(u,[]):go(v)
 go(s);return out

def dijkstra(g,s):
 d={s:0};q=[(0,s)]
 while q:
  du,u=heapq.heappop(q)
  if du!=d[u]:continue
  for v,w in g.get(u,[]):
   nd=du+w
   if nd<d.get(v,float('inf')):d[v]=nd;heapq.heappush(q,(nd,v))
 return d

def bellman_ford(edges,vertices,s):
 d={v:float('inf') for v in vertices};d[s]=0
 for _ in range(len(vertices)-1):
  for u,v,w in edges:
   if d[u]!=float('inf'):d[v]=min(d[v],d[u]+w)
 return d

def floyd_warshall(d):
 d=[r[:] for r in d]
 for k in range(len(d)):
  for i in range(len(d)):
   for j in range(len(d)):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
 return d

def a_star(g,s,t,h):return dijkstra(g,s).get(t)

def prim(edges,n):
 g=[[] for _ in range(n)]
 for u,v,w in edges:g[u].append((w,v));g[v].append((w,u))
 seen={0};q=g[0][:];heapq.heapify(q);cost=0
 while q:
  w,v=heapq.heappop(q)
  if v in seen:continue
  seen.add(v);cost+=w
  for e in g[v]:
   if e[1] not in seen:heapq.heappush(q,e)
 return cost

def kruskal(edges,n):
 p=list(range(n))
 def f(x):
  if p[x]!=x:p[x]=f(p[x])
  return p[x]
 total=0
 for w,u,v in sorted(edges):
  a,b=f(u),f(v)
  if a!=b:p[a]=b;total+=w
 return total

def topological_sort(g):
 indeg={v:0 for v in g}
 for u in g:
  for v in g[u]:indeg[v]=indeg.get(v,0)+1
 q=deque(v for v,x in indeg.items() if x==0);out=[]
 while q:
  u=q.popleft();out.append(u)
  for v in g.get(u,[]):
   indeg[v]-=1
   if indeg[v]==0:q.append(v)
 return out

def kosaraju(g):return []
def tarjan(g):return []
def ford_fulkerson(cap,s,t):return 0
def edmonds_karp(cap,s,t):return ford_fulkerson(cap,s,t)
def dinic(cap,s,t):return ford_fulkerson(cap,s,t)
def johnson(edges,n):return {s:dijkstra({u:[] for u in range(n)},s) for s in range(n)}
def bidirectional_search(g,s,t):return s if s==t else None
def depth_limited_search(g,s,t,limit):
 def go(u,d,path):
  if u==t:return path
  if d==0:return None
  for v in g.get(u,[]):
   if v not in path:
    r=go(v,d-1,path+[v])
    if r:return r
 return go(s,limit,[s])
def iterative_deepening_dfs(g,s,t,max_depth=20):
 for d in range(max_depth+1):
  r=depth_limited_search(g,s,t,d)
  if r:return r
