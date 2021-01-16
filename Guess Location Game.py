#USING A WHILE LOOP FOR BUILDING A VERY SIMPLE GUESSING GAME.
answer_location = "HYDERABAD"
guess_count = 0
guess_limit = 3
#here we are using the while loop with the required condition
while guess_count < guess_limit:
    guess =input('Where is Charminar located in India? : ')
    #WE ARE USING THE BELOW LINE TO COUNT THE NUMBER OF ATTEMPTS
    guess_count += 1
    if guess.upper() == answer_location :
        print ('YOUR ANSWER WAS CORRECT')
        break
else :
    print('SORRY YOU FAILED TO ANSWER!!')
