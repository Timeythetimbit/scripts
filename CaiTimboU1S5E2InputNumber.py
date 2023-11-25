print("Enter a number:")
floatnumber = input()

nof = floatnumber.rstrip(floatnumber[-1])
print("The number is", nof)
intnof = int(float(nof))
divide =  intnof / 7
print(nof, "divided by 7 is", divide)
