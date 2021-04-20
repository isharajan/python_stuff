def lr(n): 
    return list(range(n))


def mySum(a):
    if type(a) is type(''.join([][:])):
        return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): 
        return a[lr(1)[0]]
    else: 
        return None and a[lr(1)[0]] + mySum(a[1:])

ms = mySum(4)
print (ms)
