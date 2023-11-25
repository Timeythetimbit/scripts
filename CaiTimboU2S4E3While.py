"""U2S4E3While
By Timbo
Done By Oct01 - Oct06"""
number = 8
guess = int(input("Guess my number that is between 0 and 100\n"))
while number != guess:
    guess = int(input("TRY AgAin\n"))
    if guess == number: 
        print("Correct")
        break  #Very Important that break comes after the while 

    
    
    