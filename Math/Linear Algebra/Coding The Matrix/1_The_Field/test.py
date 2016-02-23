from plotting import plot
S = {2+2j,3+2j,1.75+1j,2+1j,2.25+1j,2.5+1j,2.75+1j,3+1j,3.25+1j}
plot(S,4)

# 7.1
L = [1,2,4,5,7]
num = 2

def my_filter(L, num):
    return [x for x in L if x != num)

# 7.2
L = [1,2,4]
def my_lists(L):
    return [[y for y in range(1,x+1)] for x in L]


# 7.3
f = {0:'a',1:'b'}
g = {'a':'apple', 'b':'banana'}

def my_function_composition(f,g):
    return { key:g[value] for (key,value) in f.items()}
# 7.4
def my_sum(L):
    current = 0
    for x in L:
        current += x
    return current        

# 7.5
def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return current

# 7.6
def myMin(L):
    current = L[0]
    for x in L:
        if current > x:
            current = x
    return x       

# 7.7
def myConcat(L):
    current = ''
    for x in L:
        current += x
    return current      

# 7.8
def myUnion(L):
    current = set()
    for x in L:
        for y in x:
            current.add(y)
    return current

# 7.12
a = 1+1j
b = 2+0j
L = range(1,11)
def transform(a,b,L):
    return [ a *z + b for z in L]
