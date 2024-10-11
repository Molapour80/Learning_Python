###qusetion1:
import random
def getss():
    random_number = str(random.randrange(100,999))
    guessing = 6
    print("Welcom to game:))))")
    print("YOu have 6 guesses")

    #####input user:
    for i in range(guessing):
        number = input(f"gusssing{i+1}:")
        if not number.isdigit() or len(number)!=3:
            print("please try  again .The number must be three digits")
            continue
        
        
        if number < random_number:
            print(f"Enter a larger number.{guessing-i-1} gusses left.")
        elif number > random_number:
            print(f"Enter a smaller number.{guessing-i-1} guesses left. ")
        elif number in random_number:
            print(f"YOU WON:).{guessing-i-1} guesses left.")
            break
    else:
        print("You could not guess correctly.")

getss()




       

    




    


    

    
    















   