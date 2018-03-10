import numpy as np
from matplotlib import pyplot as plt

n=5000
#number of generated points
UnifR=np.random.uniform(size=(1,n))
#uniform array
DistR=np.array([1,n])
#output array radial
UnifT=2*np.pi*np.random.uniform(size=(1,n))
# output array angular
x=np.arange(0,10,0.1)
y=np.ones([100,1])/10
#x-y arrays currently unused

def ExpCDFinv (x, L):
    return -np.log(1-x)*L
def BellCDFinv (x, s, m):
    return (np.log((1/x)-1)*s)-m
def InvSqCDFinv (x, k):
    return ((1/x)-1)/k
#inverse CDF functions: exponential, "bell" (not a real Gaussian), and an inverse square law

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
#plots
