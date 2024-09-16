#asking the dog's name and assigning it to "name".
name = str.capitalize(input("What is your dog's name? "))

#asking the gender until a valid gender is entered.
while True:
    
    #asking the dog's gender and assigning it to "gender".
    gender = str.capitalize(input("Is it a he or she? "))
    
    #praise the dog if gender is a valid input.
    if gender == str.capitalize("he"):
        print("Good boy", str.capitalize(name) + "!")
        #loop breaks when gender "he" entered.
        break
    elif gender == str.capitalize("she"):
        print("Good girl", str.capitalize(name) + "!")
        #loop breaks when gender "she" entered.
        break
    else:
        print("Please enter 'he' or 'she'.")

# asking a dog's age until a valid number is entered.        
while True:
    try:
        age = int(input("How old is " + name + "? " ))
        break
    except ValueError:
        print("Please enter a valid number.")
        
#printing result.        
print("Your dog", str.capitalize(name), "is", age * 7, "years old in human years.")
    
