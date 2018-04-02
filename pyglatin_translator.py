"""
for python3
https://www.codecademy.com/learn/learn-python
PygLatin
raw_input -
boolean, if...else
errors:
(flake8 rules) Indentation is not a multiple of four (E111)
https://www.python.org/dev/peps/pep-0008/#indentation
"""
pyg = 'ay'

original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print("empty or contains invalid characters")

word = original.lower()
first = word[0]
new_word = word[1:len(original)] + first + pyg
print(new_word)
