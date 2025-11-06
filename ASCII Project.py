# Travis Paul Pyle
# I aspire to become a full stack developer
# In the code below I have created a few lines of simple python print commands to display my first, middle, and last initial.
print("T T T T T     P P P P        P P P P")
print("    T         P       P      P       P")
print("    T         P       P      P       P")
print("    T         P P P P        P P P P")
print("    T         P              P")
print("    T         P              P")
print("    T         P              P")
# but, How can I make this even easier to reproduce or modify in the future?
# The easiest way to reproduce this would be to store each letter as a multi-line string

# T string
t = '''
T T T T T
    T
    T
    T
    T
    T
    T
'''
# P String 
p = '''
P P P P
P      P
P      P
P P P P
P
P
P
'''
print(t) # Displays "T"
print(p) # Displays "P"
print(p) # Displays "P"

# This is looking pretty good.  There is only one problem. 
# Instead of printing the letters together in line with each other, the code is printing the initials vertically.
# What can be done to have each initial show in a horizontal format?
# By using String Concatenation, We can simply add the strings together.
print(t + p + p)