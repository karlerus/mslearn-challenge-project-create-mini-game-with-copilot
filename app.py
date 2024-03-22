
# import the random module
import random

# create a list of options that has rock, paper, and scissors
options = ['rock', 'paper', 'scissors']
# create a score variable and set it to 0
score = 0
# create a variable to store the number of rounds
rounds = 0

while True:
    # get the user's choice
    user_choice = input('Enter your choice (rock, paper, scissors): ')
    # make the user's choice lowercase
    user_choice = user_choice.lower()
    # if the user enters something other than rock, paper, or scissors, tell them choice is invalid and ask them to enter again
    while user_choice not in options:
        print('Invalid choice. Please enter rock, paper, or scissors.')
        user_choice = input('Enter your choice (rock, paper, scissors): ')
    # get the computer's choice
    computer_choice = random.choice(options)
    # print the computer's choice
    print(f'Computer choice: {computer_choice}')

    # check who won
    if user_choice == computer_choice:
        print('It\'s a tie!')
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('You win!')
        score += 1
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('You win!')
        score += 1
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('You win!')
        score += 1
    else:
        print('You lose!')

    # increment the number of rounds
    rounds += 1
    # print the score
    print(f'Score: {score}')
    # print the number of rounds
    print(f'Rounds: {rounds}')
    
    # ask the user if they want to play again
    play_again = input('Do you want to play again? (yes/no): ')
    # if the user input is not yes or no, tell them input is invalid and ask them to enter again
    while play_again != 'yes' and play_again != 'no':
        print('Invalid input. Please enter yes or no.')
        play_again = input('Do you want to play again? (yes/no): ')
    # if the user does not want to play again, print the final score and the totsl number of rounds then break out of the loop
    if play_again == 'no':
        print(f'Final score: {score}')
        print(f'Total number of rounds: {rounds}')
        break

    # if the user wants to play again, reset the score and rounds
    if play_again == 'yes':
        continue