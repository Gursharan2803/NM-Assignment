def polylagi(x,x_val,p,i):
    for j in range(len(x_val)):
        if i!=j:
            p*=(x-x_val[j])/(x_val[i]-x_val[j])
            
    return p

def polylag(x,x_val,y_val):
    sum=0
    for i in range(len(x_val)):
        sum+=polylagi(x,x_val,y_val[i],i)
    return sum
