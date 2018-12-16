
def addr(r,a,b,c): 
    r[c] = r[a] + r[b]
    return r
    
def addi(r,a,b,c): 
    r[c] = r[a] + b
    return r
    
def mulr(r,a,b,c): 
    r[c] = r[a] * r[b]
    return r
    
def muli(r,a,b,c): 
    r[c] = r[a] * b
    return r
    
def banr(r,a,b,c): 
    r[c] = r[a] & r[b]
    return r
    
def bani(r,a,b,c): 
    r[c] = r[a] & b
    return r
    
def borr(r,a,b,c): 
    r[c] = r[a] | r[b]
    return r
    
def bori(r,a,b,c): 
    r[c] = r[a] | b
    return r
    
def setr(r,a,b,c): 
    r[c] = r[a]
    return r
    
def seti(r,a,b,c): 
    r[c] = a
    return r
    
def gtir(r,a,b,c): 
    r[c] = 1 if a > r[b] else 0
    return r
    
def gtri(r,a,b,c): 
    r[c] = 1 if r[a] > b else 0
    return r
    
def gtrr(r,a,b,c): 
    r[c] = 1 if r[a] > r[b] else 0
    return r
    
def eqir(r,a,b,c): 
    r[c] = 1 if a == r[b] else 0
    return r
    
def eqri(r,a,b,c): 
    r[c] = 1 if r[a] == b else 0
    return r
    
def eqrr(r,a,b,c): 
    r[c] = 1 if r[a] == r[b] else 0
    return r
    

opcode_funs_list = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr
]