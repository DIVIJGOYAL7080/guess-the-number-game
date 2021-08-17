import random 
print ("number guessing game")
n = random. randint(1,9)

print ("guess a number between 1-9")
guess1=int(input("1st guess : "))



if(guess1==n):
    print("you won")
else:
    guess2=int(input("bad luck 2nd guess : "))
    
    if(guess2==n):
        print("you won")
    else:
        guess3=int(input("bad luck 3nd guess : "))
    
        if(guess3==n):
            print("you won")
        else:
            guess4=int(input("bad luck 4nd guess : "))
    
            if(guess4==n):
                print("you won")
            else:
                guess5=int(input("bad luck 5nd guess : "))
   
                if(guess5==n):
                    print("you won")
                else:
                    print("the number is : ",n)
    
