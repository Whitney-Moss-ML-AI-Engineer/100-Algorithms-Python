def kmp_search(text,p):
 l=[0]*len(p);j=0
 for i in range(1,len(p)):
  while j and p[i]!=p[j]:j=l[j-1]
  if p[i]==p[j]:j+=1;l[i]=j
 out=[];j=0
 for i,c in enumerate(text):
  while j and c!=p[j]:j=l[j-1]
  if c==p[j]:j+=1
  if j==len(p):out.append(i-j+1);j=l[j-1]
 return out

def rabin_karp(text,p):return [i for i in range(len(text)-len(p)+1) if text[i:i+len(p)]==p]
def boyer_moore(text,p):return rabin_karp(text,p)
def z_algorithm(s):
 z=[0]*len(s);l=r=0
 for i in range(1,len(s)):
  if i<r:z[i]=min(r-i,z[i-l])
  while i+z[i]<len(s) and s[z[i]]==s[i+z[i]]:z[i]+=1
  if i+z[i]>r:l,r=i,i+z[i]
 return z
def suffix_array(s):return sorted(range(len(s)),key=lambda i:s[i:])
def suffix_tree(s):return {s[i:]:i for i in range(len(s))}
def longest_palindromic_substring(s):
 best=''
 for i in range(len(s)):
  for l,r in ((i,i),(i,i+1)):
   while l>=0 and r<len(s) and s[l]==s[r]:l-=1;r+=1
   if r-l-1>len(best):best=s[l+1:r]
 return best
class Trie:
 def __init__(self):self.root={}
 def insert(self,w):
  n=self.root
  for c in w:n=n.setdefault(c,{})
  n['$']=1
 def search(self,w):
  n=self.root
  for c in w:
   if c not in n:return False
   n=n[c]
  return '$' in n
def aho_corasick(text,patterns):return {p:rabin_karp(text,p) for p in patterns}
def burrows_wheeler_transform(s):
 t=s+'$';return ''.join(sorted(t[i:]+t[:i] for i in range(len(t)))[-1])
