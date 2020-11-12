string = str(input("Enter a string: "))
count = 0 
vowel = set("AaEeIiOoUuАаЪъОоУуЕеИи") 

for alphabet in string: 
    if alphabet in vowel: 
            count = count + 1
      
print("Vowels = ",count) 