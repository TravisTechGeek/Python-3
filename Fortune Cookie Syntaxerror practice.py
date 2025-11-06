# Fortune Cookie Program 🥠
 # 1. In script.py, your coworker Carolyn wrote a Fortune Cookie program that is supposed to print out a possible fortune based on a random number and an if/elif/else statement.
  # Run the program to check it out. There are 4 syntax errors, find them and fix them
import random

fortune = random.randint(0, 4)

if fortune == 0:
  print("May you one day be carbon neutral")
elif fortune == 1:  
  print("You have rice in your teeth")
elif fortune == 2:
  print("No snowflake feels responsible for an avalanche")
elif fortune == 3:
  print("You can only connect the dots looking backwards")
elif fortune == 4:
  print("The fortune you seek is in another cookie")
else:
  print()


  # Line 9 no colon after 0
  # Line 12 missing f in elif
  # line 18 missing closing bracket
  # missing else statement and print commnd 