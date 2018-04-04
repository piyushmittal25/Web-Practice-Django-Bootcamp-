import random
computer_generated_number=random.sample(range(1,10),3)
sort=sorted(computer_generated_number)
print("Welcome to code breaker game!!!\n A three digit number is genrated just try to guess it:)")
gameon=True
while gameon:
    guess=list(map(int,list(input("I want to know your guess?"))))
    guess_sort=sorted(guess)
    #print(guess,computer_generated_number)
    if guess== computer_generated_number:
        print("Congrats you get me")
        gameon=False
    elif guess[0]==computer_generated_number[0] or guess[1]==computer_generated_number[1] or guess[2]==computer_generated_number[2]:
        print("You find digit at correct position")
    elif guess_sort[0]==sort[0] or guess_sort[1]==sort[1] or guess_sort[2]==sort[2]:
        print("You are close")
    else:
        print("You are far away from me")
