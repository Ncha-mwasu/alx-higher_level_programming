#!/usr/bin/python3
for letters in range (122, 96, -1):
  if letters % 2 == 0:
    print(f"{chr(letters)}", end="")
  else:
    print(f"{chr(letters - 32)}", end="")

