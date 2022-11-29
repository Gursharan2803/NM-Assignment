import generalsimsonrule as gs


#gs.simson(f,xv,yv,n,a,b)

def integral(f,x,y):
    return gs.simson(f,x,y,1000,0,4)

def indefinite(f,x,y,n,a,b):
    return gs.simson(f,x,y,n,a,b)