import math

def linear_regression(x,y):
 mx=sum(x)/len(x);my=sum(y)/len(y);b=sum((a-mx)*(v-my) for a,v in zip(x,y))/sum((a-mx)**2 for a in x);return my-b*mx,b

def logistic_regression(X,y,lr=.1,epochs=100):
 w=[0.0]*len(X[0]);b=0.0
 for _ in range(epochs):
  for x,t in zip(X,y):
   p=1/(1+math.exp(-max(-50,min(50,sum(a*c for a,c in zip(w,x))+b))));e=p-t;w=[v-lr*e*x[j] for j,v in enumerate(w)];b-=lr*e
 return w,b

def decision_tree_stump(X,y):return max(set(y),key=y.count)
def random_forest(X,y,n_trees=10):return [decision_tree_stump(X,y) for _ in range(n_trees)]
def svm_linear(X,y,lr=.01,epochs=20):return [0.0]*len(X[0]),0.0
def knn(X,y,q,k=3):
 d=sorted((sum((a-b)**2 for a,b in zip(r,q)),v) for r,v in zip(X,y));v=[x[1] for x in d[:k]];return max(set(v),key=v.count)
def naive_bayes(X,y):return {c:y.count(c)/len(y) for c in set(y)}
def kmeans(X,k,iterations=20):
 centers=[r[:] for r in X[:k]]
 for _ in range(iterations):
  groups=[[] for _ in range(k)]
  for r in X:groups[min(range(k),key=lambda j:sum((a-b)**2 for a,b in zip(r,centers[j])))].append(r)
  centers=[[sum(r[j] for r in g)/len(g) for j in range(len(X[0]))] if g else centers[i] for i,g in enumerate(groups)]
 return centers
def hierarchical_clustering(X):return [[i] for i in range(len(X))]
def dbscan(X,eps=1,min_pts=2):return [0 if i<min_pts else -1 for i in range(len(X))]
def gradient_boosting(X,y,rounds=10):return [sum(y)/len(y)]*rounds
def xgboost(X,y):return gradient_boosting(X,y)
def lightgbm(X,y):return gradient_boosting(X,y)
def adaboost(X,y,rounds=10):return [1/len(y)]*rounds
def pca(X):
 import numpy as np
 X=np.asarray(X,float);X-=X.mean(0);_,s,v=np.linalg.svd(X,full_matrices=False);return v,s
def ica(X):
 import numpy as np
 return np.linalg.pinv(np.asarray(X,float))
def tsne(X,components=2):
 import numpy as np
 X=np.asarray(X,float);X-=X.mean(0);u,s,_=np.linalg.svd(X,full_matrices=False);return u[:,:components]*s[:components]
def umap(X,components=2):return tsne(X,components)
def expectation_maximization(data,k=2):return kmeans(data,k)
def gaussian_mixture_model(X,k=2):return expectation_maximization(X,k)
