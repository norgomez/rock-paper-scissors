import random

 user_score = []
 ai_score = []

 game = 5
 options = ['Rock', 'Paper', 'Scissors']


 while game > 0:
     user_option = input('Input your choice: ')
     ai_option = random.choice(options)
     if user_option == 'Rock':
         game = game - 1
         if ai_option == 'Rock':
             print("its a tie both rock")
         elif ai_option == "Paper":
             print('You lose rock loses to paper')
             ai_score.append(1)
         elif ai_option == 'Scissors':
             print('You win, rock beats scissors')
             user_score.append(1)
     elif user_option == 'Paper':
         game = game - 1
         if ai_option == 'Scissors':
             print('Paper loses to scissors')
             ai_score.append(1)
         elif ai_option == 'Rock':
             print('paper beat rock')
             user_score.append(1)
         elif ai_option == 'Paper':
             print('its a tie ')
     elif user_option == 'Scissors':
         game = game - 1
         if ai_option == 'Paper':
             print('Scissors beats paper')
             user_score.append(1)
         elif ai_option == 'Rock':
             print('scissors loses to rock')
             ai_score.append(1)
         elif ai_option == "Scissors":
             print('Its a tie')
     else:
         print('error')

 print(f"Your score is: {user_score}")
 print(f"AI score is: {ai_score}")

 if user_score > ai_score:
     print('You win the game!')
 elif user_score < ai_score:
     print('You lost the game!')
 else:
     print("its a tie game!")
