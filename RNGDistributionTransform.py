import numpy as np
from matplotlib import pyplot as plt

n=5000
UnifR=np.random.uniform(size=(1,n))
DistR=np.array([1,n])
UnifT=2*np.pi*np.random.uniform(size=(1,n))
x=np.arange(0,10,0.1)
y=np.ones([100,1])/10

def ExpCDFinv (x, L):
    return -np.log(1-x)*L
def BellCDFinv (x, s, m):
    return (np.log((1/x)-1)*s)-m
def InvSqCDFinv (x, k):
    return ((1/x)-1)/k

fig0=plt.figure()
plt.scatter(UnifR*np.cos(UnifT),UnifR*np.sin(UnifT),marker=".")
plt.show()

fig0=plt.figure()
plt.plot(x,y)
plt.show()

DistR=BellCDFinv(UnifR,1,0)
y=(1/(1 + np.exp(-x)))*(1- 1/(1 + np.exp(-x)))

fig1=plt.figure()
plt.scatter(DistR*np.cos(UnifT),DistR*np.sin(UnifT),marker=".")
plt.show()

fig1=plt.figure()
plt.plot(x,y)
plt.show()

DistR=ExpCDFinv(UnifR,1)
y=np.exp(-x)

fig2=plt.figure()
plt.scatter(DistR*np.cos(UnifT),DistR*np.sin(UnifT),marker=".")
plt.show()

fig2=plt.figure()
plt.plot(x,y)
plt.show()

DistR=InvSqCDFinv(UnifR,1)
y=1/(1+x)

fig3=plt.figure()
plt.scatter(DistR*np.cos(UnifT),DistR*np.sin(UnifT),marker=".")
plt.show()

fig3=plt.figure()
plt.plot(x,y)
plt.show()