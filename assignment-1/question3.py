
def cube(n):
    sum=0
    for i in range(n+1):
        sum=sum+i**3
    return sum
a=input()
n=int(a)
print(cube(n))
