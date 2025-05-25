def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
def genfibonacci(n):
    l=[0,1]
    for i in range(2,n):
        l.append(l[-1]+l[-2])
    return(l)
