# Boolean Statements are either true or false
# Opinions are neither true or false

# Statement: The Earth revolves around the Sun.
first_statement = "Yes" # this boolean statement can be determined to be true

# Statement: The Moon is made of cheese.
second_statement = "Yes" # this boolean statement can be determined to be false.

# Statement: Chocolate ice cream tastes better than vanilla.
third_statement = "No" # this statement is an opinion and is neither true or false

# Set the variables 'statement_one' and 'statement two' equal to the results of the following boolean expressions:
# Statement One: not (4 + 5 <= 9)
# Statement Two: not (8 * 2) != 20 - 4

statement_one = not (4 + 5 <= 9) # False, why? 4+5=9<=9.which is true, but because we have used the not function, the opposite of the result is the answer.

statement_two = not (8 * 2) != 20 - 4 #True, why? 8*2=16!=20-4=16 or to simplify the equation with the answers 16 != !6. Remember != means not equal to.
#So if the statement actually is false and the not function takes the opposite of a false statement, the answer is actually true

# The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you.
# They want you to return to a previous if statement and add in several checks using and and not statements:

# If a student’s credits is not greater or equal to 120, it should print: "You do not have enough credits to graduate."
# If their gpa is not greater or equal to 2.0, it should print: "Your GPA is not high enough to graduate."
# If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0, it should print:"You do not meet either requirement to graduate!"

credits = 120
gpa = 1.8

if not credits >= 120:
  print('You do not have enough credits to graduate.')

if not gpa >= 2.0:
  print('Your GPA is not high enough to graduate.')

if not (credits >= 120) and not (gpa >= 2.0):
  print('You do not meet either requirement to graduate!')
