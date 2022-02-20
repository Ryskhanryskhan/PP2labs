def solve(numheads, numlegs): 
    a = ((numlegs // 2) - numheads) 
    b = numheads - a 
    print("number of chikens:", b, "number of rubbits:", a) 
 
heads, legs = 35, 94 
print(solve(heads, legs))