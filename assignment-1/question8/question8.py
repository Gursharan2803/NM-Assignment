import sys
sys.path.insert(0,'/home/gursharan/Assignment1/question5/')
from  fibo import fibo0
import matplotlib.pyplot as plt
def ratioFn(n):
    return fibo0(n+1)/fibo0(n)
list=[]
x=ratioFn(1)
for i in range(3,100):

    x1=ratioFn(i)
    if(abs(x-x1)<1e-6):
        print(i)
        break
    list.append(ratioFn(i))
    x=x1

print(list)
plt.plot(list)
plt.xlabel('n')
plt.ylabel('ratio f(n+1)/f(n)')
plt.title('plot')
plt.show()
