first_name = "Julie"
last_name = "Blevins"
# Copeland’s Corporate Company has realized that their policy of using the first five letters of an employee’s last name as a user name isn’t ideal when they have multiple employees with the same last name. Write a function called account_generator() that takes two inputs, first_name and last_name and concatenates the first three letters of each and then returns the new account name.

def account_generator(first_name, last_name):
  account_name = first_name[:3] + last_name[:3]
  return account_name
# Test your function on the first_name and last_name provided in script.py and save it to the variable new_account.
new_account = account_generator(first_name, last_name)

print(new_account)