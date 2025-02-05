# Part 01 of the Challenge
exit_program = False

while not exit_program:
  user_input = input("Enter an integer or 'exit' to quit: ")
  if user_input.lower() == 'exit':
    exit_program = True
    print("Exiting the program.")
    continue
  try:
    integer_number = int(user_input)
    if integer_number > 0:
      print('The number is positive.')
    elif integer_number < 0:
      print('The number is negative.')
    else:
      print('The number is zero.')

    user_input_2 = input("Enter another integer to compare: ")
    if user_input_2 > user_input:
      print(f'{user_input_2} is greater than {user_input}.')
    elif user_input_2 < user_input:
      print(f'{user_input_2} is less than {user_input}.')
    else:
      print(f'{user_input_2} is equal to {user_input}.')
  except ValueError:
    print('Invalid number. Please enter an integer or "exit" to quit.')
