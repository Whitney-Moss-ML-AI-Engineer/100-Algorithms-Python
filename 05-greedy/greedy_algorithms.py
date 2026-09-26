def activity_selection(intervals):
 out=[];end=float('-inf')
 for s,e in sorted(intervals,key=lambda x:x[1]):
  if s>=end:out.append((s,e));end=e
 return out

def fractional_knapsack(items,W):
 value=0
 for w,v in sorted(items,key=lambda x:x[1]/x[0],reverse=True):
  take=min(W,w);value+=take*v/w;W-=take
  if not W:break
 return value

def huffman_coding(freq):return sorted(freq.items(),key=lambda x:x[1])
def job_scheduling(jobs):return sorted(jobs,key=lambda x:x[2],reverse=True)
def prim_greedy(edges,n):
 from heapq import heapify,heappop,heappush
 g=[[] for _ in range(n)]
 for u,v,w in edges:g[u].append((w,v));g[v].append((w,u))
 seen={0};q=g[0][:];heapify(q);cost=0
 while q:
  w,v=heappop(q)
  if v in seen:continue
  seen.add(v);cost+=w
  for e in g[v]:
   if e[1] not in seen:heappush(q,e)
 return cost

def kruskal_greedy(edges,n):return sum(w for w,_,_ in sorted(edges)[:n-1])
def dijkstra_greedy(g,s):
 import heapq
 d={s:0};q=[(0,s)]
 while q:
  du,u=heapq.heappop(q)
  if du!=d[u]:continue
  for v,w in g.get(u,[]):
   if du+w<d.get(v,float('inf')):d[v]=du+w;heapq.heappush(q,(d[v],v))
 return d

def gas_station(gas,cost):
 if sum(gas)<sum(cost):return -1
 start=total=0
 for i in range(len(gas)):
  total+=gas[i]-cost[i]
  if total<0:start=i+1;total=0
 return start

def min_coins_greedy(coins,amount):
 n=0
 for c in sorted(coins,reverse=True):q,amount=divmod(amount,c);n+=q
 return n if amount==0 else -1

def interval_scheduling(intervals):return activity_selection(intervals)
