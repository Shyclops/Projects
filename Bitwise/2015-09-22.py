def doubleUp(x,y):
    return (x<<y)

def doubleDown(x,y):
    return(x>>y)

def bitAnd(x,y):
    return (x&y)

def bitOr(x,y):
    return (x|y)

def bitExOr(x,y):
    return (x^y)

def comp(x):
    return ~x

def doubleUpDoubles(x,y,z):
    return doubleUp(x,doubleUp(y,z))


