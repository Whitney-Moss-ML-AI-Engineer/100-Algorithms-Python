import numpy as np

def perceptron(X,y,epochs=10,lr=.1):
 w=np.zeros(len(X[0]));b=0
 for _ in range(epochs):
  for x,t in zip(X,y):
   if t*(w@x+b)<=0:w+=lr*t*x;b+=lr*t
 return w,b

def mlp(X,y):
 X=np.asarray(X);return X.T@np.asarray(y).reshape(-1,1)
def cnn(image,kernel):
 return np.array([[np.sum(image[i:i+kernel.shape[0],j:j+kernel.shape[1]]*kernel) for j in range(image.shape[1]-kernel.shape[1]+1)] for i in range(image.shape[0]-kernel.shape[0]+1)])
def rnn(sequence,W,U,b):
 h=np.zeros(U.shape[0])
 for x in sequence:h=np.tanh(W@x+U@h+b)
 return h
def lstm_cell(x,h,c,W,U,b):
 z=W@x+U@h+b;i,f,o,g=np.split(1/(1+np.exp(-z)),4);c=f*c+i*g;return o*np.tanh(c),c
def gru_cell(x,h,Wz,Wr,Wh):
 z=1/(1+np.exp(-(Wz@x)));r=1/(1+np.exp(-(Wr@x)));return (1-z)*h+z*np.tanh(Wh@x+r*h)
def transformer_attention(Q,K,V):
 s=Q@K.T/np.sqrt(Q.shape[-1]);s=np.exp(s-s.max(-1,keepdims=True));s/=s.sum(-1,keepdims=True);return s@V
def autoencoder(X,latent=2):
 X=np.asarray(X,float);X-=X.mean(0);u,s,v=np.linalg.svd(X,full_matrices=False);return u[:,:latent]*s[:latent]
def vae_sample(mu,logvar):return mu+np.exp(.5*logvar)*np.random.randn(*mu.shape)
def gan_step(real,noise,generator,discriminator):return discriminator(real),discriminator(generator(noise))
