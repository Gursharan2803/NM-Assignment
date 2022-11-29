import numpy as np
import matplotlib.pyplot as plt
x,y=np.loadtxt("/home/gursharan/Downloads/data.dat",unpack=True)

def f(t,x):
    n=100
    s1=0
    for k in range(n):
        L=1.0
        for h in range(n):
            if h!=k:
                L=L*(t-x[h])/(x[k]-x[h])
        s2=s1+L*y[k]
        s1=s2
    return(s2)
#first derivative value at 0
def df(a,x):
    p=0
    for i in range(100):
        L=1
        k=0
        for j in range(100):
            if i!=j:
                L=((a-x[j])/(x[i]-x[j]))*L
                k=k+(1/(a-x[j]))
        l=L*k
        m=(y[i]*l)
        p=p+m
    return(p)

#second derivative value at 0

def double_diff(b,x):
    h=10**-5
    return((-df(b+2*h,x)+8*df(b+h,x)-8*df(b-h,x)+df(b-2*h,x))/(12*h))
#third derivative value at 0
def tripl_diff(c,x):
    h=10**-5
    return((-df(c+2*h,x)+16*df(c+h,x)-30*df(c,x)+16*df(c-h,x)-df(c-2*h,x))/(12*h**2))

# applying newton rapson
eps=10**-6  #value upto precission
w=3.0  #initial guess
err=1.0 
while err>=eps:
    w1=w-((3*double_diff(0,x)*w-3*df(0,x)*w**2+f(0,x)*w**3-tripl_diff(0,x))/(3*double_diff(0,x)-6*df(0,x)*w+3*f(0,x)*w**2))
    err=abs(w-w1)
    w=w1
root=w1# It is the value of w
c=f(0,x)# The value of c
b=df(0,x)-(c*root)# The value of b
a=(double_diff(0,x)-(2*b*root)-c*(root)**2)/2
print("value of coeff  a",a)
print("value of coeff b",b)
print("value of coeff c",c)
print("value of w",root)
k=((a)*x**2+b*x+c)*np.exp(root*x)
plt.plot(x,k,"-o")
plt.plot(x,y)
plt.title("Original plot vs The plot of the function")
plt.show()
