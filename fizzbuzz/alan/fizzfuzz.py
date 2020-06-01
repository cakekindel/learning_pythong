#input of some number, for some given number if its divisible by 3, then we want to print fizz, if it's divisible by 5 we want to print fuzz, if its divisible by both we want to print fizzfuzz
#define a function named fizzfuzz, who takes a number(n)
def fizz_fuzz (n):
    print ("dummy thicc")
    if n % 3 ==0 and n % 5 ==0: #if its divisible by 3 and 5, print fizzfuzz
        print ("fizzfuzz")
    elif n % 3 ==0: #if its divisible by 3, print fizz, else/if
        print ("fizz")
    elif n % 5 ==0: #if its divisible by 5, print fuzz, else/if/otherwisae
        print ("fuzz")
    
fizz_fuzz (120) 