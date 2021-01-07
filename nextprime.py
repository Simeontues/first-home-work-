from prime import Prime
np = int(input("Enter a number: "))
def nextprime(np): 

    if (np <= 1): 
        return 2
  
    prime = np 
    found = False

    if(Prime(prime) == True):
        return np

    while(not found): 
        prime += 1
        
        if(Prime(prime) == True): 
            found = True
        
    return prime 
        
print(nextprime(np)) 