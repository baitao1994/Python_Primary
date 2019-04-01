def func(n,p):
    if n == 1:
        return p
    return func(n - 1,n * p)

def f(n):
    return func(n,1)
print(f(100))
