#Ask the user to enter two names and output the following:
#You entered the names alphabetically (true/false)
#You entered the same names (True/false)

firstname = input("Enter the first name:\n")
secondname = input("Enter the second name:\n")

print("You entered the names in alphabeticl order:"
      , firstname < secondname )
print("You entered the same name"
      , firstname == secondname)