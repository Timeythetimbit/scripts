"""
U2S3Challenge
By Timbo
Done By Oct10
"""
number = 23
for i in range(10):
    guess = int(input("Guess the number between 10-50:\n"))
    if guess == number:
        break
    else:
        print("Try Again")