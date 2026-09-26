def fib_dp(n):
 a,b=0,1
 for _ in range(n):a,b=b,a+b
 return a

def knapsack_01(weights,values,W):
 dp=[0]*(W+1)
 for w,v in zip(weights,values):
  for c in range(W,w-1,-1):dp[c]=max(dp[c],dp[c-w]+v)
 return dp[W]

def unbounded_knapsack(weights,values,W):
 dp=[0]*(W+1)
 for c in range(W+1):
  for w,v in zip(weights,values):
   if w<=c:dp[c]=max(dp[c],dp[c-w]+v)
 return dp[W]

def lcs(a,b):
 dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]
 for i,x in enumerate(a,1):
  for j,y in enumerate(b,1):dp[i][j]=dp[i-1][j-1]+1 if x==y else max(dp[i-1][j],dp[i][j-1])
 return dp[-1][-1]

def lis(a):
 import bisect
 d=[]
 for x in a:
  i=bisect.bisect_left(d,x)
  if i==len(d):d.append(x)
  else:d[i]=x
 return len(d)

def matrix_chain(d):
 n=len(d)-1;dp=[[0]*n for _ in range(n)]
 for L in range(2,n+1):
  for i in range(n-L+1):
   j=i+L-1;dp[i][j]=min(dp[i][k]+dp[k+1][j]+d[i]*d[k+1]*d[j+1] for k in range(i,j))
 return dp[0][-1]

def coin_change(coins,a):
 dp=[a+1]*(a+1);dp[0]=0
 for x in range(1,a+1):
  for c in coins:
   if c<=x:dp[x]=min(dp[x],dp[x-c]+1)
 return -1 if dp[a]>a else dp[a]

def rod_cut(prices,n):
 dp=[0]*(n+1)
 for i in range(1,n+1):dp[i]=max(prices[j]+dp[i-j-1] for j in range(i))
 return dp[n]

def edit_distance(a,b):
 dp=list(range(len(b)+1))
 for i,x in enumerate(a,1):
  old=dp[0];dp[0]=i
  for j,y in enumerate(b,1):
   cur=dp[j];dp[j]=old if x==y else 1+min(dp[j],dp[j-1],old);old=cur
 return dp[-1]

def subset_sum(a,target):
 possible={0}
 for x in a:possible|={v+x for v in possible if v+x<=target}
 return target in possible

def min_path_sum(g):
 dp=[float('inf')]*(len(g[0])+1);dp[1]=0
 for row in g:
  for j,x in enumerate(row,1):dp[j]=x+min(dp[j],dp[j-1])
 return dp[-1]

def kadane(a):
 best=cur=a[0]
 for x in a[1:]:cur=max(x,cur+x);best=max(best,cur)
 return best

def partition_equal(a):return sum(a)%2==0 and subset_sum(a,sum(a)//2)
def word_break(s,words):
 dp=[False]*(len(s)+1);dp[0]=True
 for i in range(1,len(s)+1):dp[i]=any(dp[j] and s[j:i] in words for j in range(i))
 return dp[-1]
def egg_drop(e,f):
 dp=[[0]*(f+1) for _ in range(e+1)]
 for x in range(1,e+1):dp[x][1]=1
 for x in range(1,f+1):dp[1][x]=x
 for x in range(2,e+1):
  for y in range(2,f+1):dp[x][y]=1+min(max(dp[x-1][k-1],dp[x][y-k]) for k in range(1,y+1))
 return dp[e][f]
