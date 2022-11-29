def simson2(f,x_val,y_val,a,b):
    return (b-a)*(f(a,x_val,y_val)+4*f(((a+b)/2),x_val,y_val)+f(b,x_val,y_val))/6
    

def simson(f,x_val,y_val,n,a,b):
    h=(b-a)/n
    sum=0
    
    for i in range(n):
        # print(sum)
        sum+=simson2(f,x_val,y_val,a+h*i,a+h*(i+1))
        
    return sum
    