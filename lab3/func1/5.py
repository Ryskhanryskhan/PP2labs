def perm(s): 
    from itertools import permutations 
 
    p = permutations(s) 
    print([''.join(i) for i in p]) 
 
s = input() 

perm(s)