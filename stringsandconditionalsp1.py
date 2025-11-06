def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  else:
    return False
print(letter_check("strawberry", "a"))
print(letter_check("strawberry",  "o"))