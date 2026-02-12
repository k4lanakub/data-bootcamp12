import random
def paoyingchub():

  score = 0
  hands = ("hammer" , "scissors" , "paper")

  while True:
      user_hand = input("Choose Your hand: ").lower()
      if user_hand == 'exit':
        print(f"Your final score is: {score}. Good Bye")
        break

      if user_hand not in hands:
        print("Your input is invalid, Choose again Only 'hammer', 'scissors', 'paper' ")
        continue
      com_hand = random.choice(hands)
      print(f"Your opponent hand: {com_hand}")
      if user_hand == com_hand:
          print("Draw")
      elif (user_hand == "hammer" and com_hand == "scissors") or \
           (user_hand == "scissors" and com_hand == "paper") or \
           (user_hand == "paper" and com_hand == "hammer"):
          print("You Win")
          score += 1
      else:
          score -= 1
          print("You Lose")  

      print(f"Your score is: {score}")  
    
      


paoyingchub()