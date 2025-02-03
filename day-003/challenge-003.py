# Part 01 of the challenge
print('------------Part 01------------')
name = input("Enter your name: ")

while True:
  try:
    age = int(input("Enter your age: "))
    break
  except ValueError:
    print('Invalid age. Please enter an integer.')

city = input("Enter your city: ")
print(f'Hello, {name}! You are {age} years old and live in {city}.')

# Part 02 of the challenge
print('------------Part 02------------')
while True:
  try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    break
  except ValueError:
    print('Invalid number. Please enter an integer.')
  exit()

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print(f'The sum of {num1} and {num2} is {sum}.')
print(f'The subtraction of {num1} and {num2} is {sub}.')
print(f'The multiplication of {num1} and {num2} is {mul}.')
print(f'The division of {num1} and {num2} is {div}.')

# Part 03 of the challenge
print('------------Part 03------------')
if 0 <= age <= 12:
  print(f'{name}, you are {age} years old, so you are a child.')
elif 13 <= age <= 17:
  print(f'{name}, you are {age} years old, so you are a teenager.')
elif 18 <= age <= 59:
  print(f'{name}, you are {age} years old, so you are an adult.')
elif age >= 60:
  print(f'{name}, you are {age} years old, so you are a senior.')
else:
  print('Invalid age.')

# Extra challenge
print('------------Extra Challenge------------')
while True:
  try:
    Celsius = float(input("Enter the temperature in Celsius: "))
    Fahrenheit = Celsius * 1.8 + 32
    break
  except ValueError:
    print('Invalid temperature. Please enter a real number.')
  print('Invalid temperature. Please enter a real number.')
  exit()

print(f'The temperature of {Celsius}°C is equal to {Fahrenheit}°F.')