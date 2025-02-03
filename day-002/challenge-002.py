# Variable declaration
age = int(input("Enter your age: "))
name = input("Enter your name: ")
height = float(input("Enter your height: "))
is_machine_learning_engineer = True
phrase = 'Learning Python in the 100 days challenge!' 
word_python = phrase[9:15]
modified_phrase = phrase.replace('Python', 'Machine Learning')

# Arithmetic operators
sum_result = age + 2
sub_result = age - 2
mul_result = age * 0.8
div_result = age / 2
mod_result = age % 2
exp_result = age ** 2

# Relational operators
is_major = age > 18

# Display values
print(f'My name is {name}, I am {age} years old and {height} meters tall, and I am learning Python to become a Machine Learning Engineer.')
print('------------Arithmetic Operators------------')
print(f'Age + 2 = {sum_result}')
print(f'Age - 2 = {sub_result}')
print(f'Age * 0.8 = {mul_result}')
print(f'Age / 2 = {div_result}')
print(f'Age % 2 = {mod_result}')
print(f'Age ** 2 = {exp_result}')
print('------------Relational Operators------------')
print(f'Age > 18 = {is_major}')
print('------------Challenge Phrases------------')
print('Phrase in uppercase: ', phrase.upper())
print(f'Modified phrase: {modified_phrase}')
