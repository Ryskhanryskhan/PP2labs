def guess_the_number(): 
    import random 
    n = random.randint(1, 20) 
    print("Hello! What is your name?") 
    name = input() 
    print("Well, " + name + ", I am thinking of a number between 1 and 20.") 
 
    
    
    for i in range(3): 
        print("Take a guess.") 
        a = int(input()) 
        if a > n: 
            print("Your guess is too high") 
        elif a < n: 
            print("Your guess is too low") 
        else: 
            print("Yes!") 
            break 
        if i == 2: 
            print("Good job, " + name + "! You guessed my number in 3 guesses!") 
 

guess_the_number()