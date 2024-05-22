Secret_Number = 9
Guess_number = 0
Guess_Count = 3
while Guess_number < Guess_Count:
    Guess = int(input("Guess: "))
    Guess_number += 1
    if Guess == Secret_Number:
        print('You Won!')
        break
else:
    print("Sorry you Lost!")