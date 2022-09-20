#!!/usr/bin/python3
# print_last_digit - prints the last digit of ints
# number: parameter description
# Return: last digit
def print_last_digit(number):
  if number < 0:
    last_digit = (-1 * number) % 10
  
  else:
    last_digit = number % 10
  
  print(f"{last_digit}", end="")
  return last_digit
