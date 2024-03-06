import random

top_range_number =input('Type a number: ')

if top_range_number.isdigit():
    top_range_number=int(top_range_number)
    if top_range_number < 0 :
        print('please type a number lager than 0 next time.')
        quit()
else:
    print('please type a number next time.')
    quit()

random_number= random.randint(0,top_range_number)
print(random_number)
guesses=0

while True:
    guesses += 1
    user_guess=input('Make a guess: ')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('please enter number next time')
        continue
    
    if user_guess==random_number:
        print("you got right ")
        break
    elif user_guess > random_number:
        print("your guess was too big")
    elif user_guess < random_number:
        print("your guess was too small")
        # print("you got worng..!")
print("you got it in "+str(guesses)+" guesses")