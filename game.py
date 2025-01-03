def game(a):
  n=int(input("Enter a number : "))
  if(a==n):
    print("Your guess is correct")
  elif(a<n):
    print("Try a small number")
    game(a)
  else:
    print("Try a big number")
    game(a)
import random
a=random.randint(1,100)
game(a)
