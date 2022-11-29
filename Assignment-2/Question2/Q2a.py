import numpy as np
import lagpoly as lp
import Q2c as qc
import newtonrapson as nr
from matplotlib import pyplot as plt
a=np.loadtxt("/home/gursharan/Downloads/data.dat")
x=a[:,0]
y=a[:,1]
plt.plot(x,y)
def Lag(x0,x,y):
    n=len(x)
    yp=0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (x0 - x[j])/(x[i] - x[j])
        yp = yp + p * y[i]
    return yp    

 

def df_i(x,x_val,p,i):
    sum=0
    for j in range(len(x_val)):
        if i!=j:
            sum+=1/(x-x_val[j])
            
    return sum*lp.polylagi(x,x_val,p,i)
    
def df(x,x_val,y_val):
    sum=0
    for i in range(len(x_val)):
        sum+=df_i(x,x_val,y_val[i],i)
    return sum

print("value of function at x=2.5")
print(Lag(2.5,x,y))
print("the two roots are")
r1=nr.rootFind(lp.polylag,df,1,x,y,10**-6)
r2=nr.rootFind(lp.polylag,df,3.5,x,y,10**-6)
print(r1 , r2)
print("value of integration using simpson method from 0 to 4 ")
print(qc.integral(Lag,x,y))
 
# now we have to find x where integral 0 to x  function goes to zero.
# so just apply simpsonrule from 0 to x then,
# apply newtonrapson to find the root 


def f(x,x_val,y_val):
    return qc.indefinite(Lag,x_val,y_val,50,0,x)

r=nr.rootFind(f,Lag,1,x,y,10**-6)
print("value where the integral of function goes to zero is :")
print(r)

