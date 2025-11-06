# Relational Operators 
# equal to operator: ==
# not equal to operator: !=

# 2 * 2 == 2 + 2
first_expression = True # this statement is true, as 2*2=4 and 2+2=4 also. Therefore 4 == 4.

# 3 + 3 != 3 * 3
second_expression = True # this statement is true, as 3+3=6 and 3*3=9. Therefore 6 != 9

# 3 * 3 == '9'
third_expression = False # this statement is false as '9' is a string. 3*3=9, nine is a integer and integers are not equal to a string  
# More Practice
x = 20
y = 20

# Create an if statement that checks if 'x' and 'y' are equal, print the string below if so: 'These numbers are the same'
# Write the first if statement here:
if x == y:
  print('These numbers are the same')

credits = 120

# The nearby college, Calvin Coolidge's Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate.
# Write an if statement that checks if the student has enough credits to graduate.  If they do, print the following string: 'You have enough credits to graduate!'
# Write the second if statement here:
if credits >= 120:
  print('You have enough credits to graduate!')

# Set the variables 'statement_one' and 'statement_two' equal to the results of the following boolean expressions:
# Statement One: (2 + 2 + 2 >= 6) and (-1 *-1 < 0)
# Statement Two: (4 * 2 <= 8) and (7 - 1 == 6)

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

# Let's return to Calvin Coolidge's Cool College. 120 credits aren't the only graduation requirement, you also need to have a GPA of 2.0 or higher.
# Rewrite the if statement so that it checks to see if a student meets both requirements using an and statement.
# If they do, print the string: 'You meet the requirements to graduate!'
credits = 120
gpa = 3.4

# Set the variables 'statement_one' and 'statement_two'  equal to the results of the following boolean expressions:

# Statement One: (2 - 1 > 3) or (-5 *2 == -10)
# Statement Two:(9 + 5 <= 15) or (7 != 4 + 3)

statement_one = (2 - 1 > 3) or (-5 *2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

# The registrar’s office at Calvin Coolidge’s Cool College has another request. They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).

# Write an if statement that checks if a student either has 120 or more credits or a GPA 2.0 or higher, and if so prints: 'You have met at least one of the requirements.'

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print('You have met at least one of the requirements.')


if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")
