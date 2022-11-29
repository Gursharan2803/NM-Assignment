def rootFind(f,df,x,x_val,y_val,eps):
    value=0
    while(True):
        value=f(x,x_val,y_val)
        x=x-value/df(x,x_val,y_val,)
        if(abs(value)<abs(eps)):
            break
 
    return x

def rootFind2(f,df,x,eps):
    value=0
    while(True):
        x=x-f(x)/df(x)
        if(abs(value)<abs(eps)):
            break
 
    return x