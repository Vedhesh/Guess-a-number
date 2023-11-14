import random

n = random.randint(1, 10)
guess = int(input("Guess a number from 1 to 10: "))
chances = 0
while chances != 4:
  if guess > n:
    print("Try guessing lower than", guess)
  elif guess == n:
    print("You guessed it!")
    for i in range(10):
      print("🎊" * i)
    for i in range(10):
      print("🎊" * (10 - i))
    break
  else:
    print("Try guessing higher than", guess)
  guess = int(input("Try again from 1 to 10: "))
  chances += 1
  
if chances == 4:
  print("You Lose!! 😂 it was", n)
