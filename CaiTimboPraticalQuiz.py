"""
Test
By Timbo
Done By Oct26
"""

#A)  Using a 'for loop' let a user guess the answer to the following question up to 10 times but exit the loop if they get it correct.
#B)  User must enter a number between 5 and 75. If the number entered is outside the loop the user gets a message that states: Please enter a number between 5 & 75. This counts as one of the users guesses.
#C)  Measure start time and check that the delta time has not exceeded 30 seconds after each user input. If the user exceeds 30 seconds print out that the: 'User exceeded 30 seconds' and exit the 'for loop'. Note: You do not need to check the time in real time). The correct answer for the guess should be my favorite number 25.
#D)  Marks will be assigned based on rubric (see google assignment)

import time 
number = 25
starttimer = time.perf_counter #Starting time
endtimer = time.perf_counter #Ending time

for i in range(10):  #How many times you can answer
    answer = int(input("Please Enter a Number Between 5 and 75:\n"))
    
    if answer == 25: # If the number 25 is choosen exit program
        print("Correct")
        break
    elif answer >= 5 or answer <=75: #If wrong answer it retries
        print("Try Again")
    elif answer >= 75 or answer <= 5: #If not in the range it warns the user
        print("Please enter a number between 5 & 75")

    if starttimer - endtimer == 30: #If the last input is 30 sec long it prints and exits for loop
            print('User exceeded 30 seconds')
            break
        




    
    
    
    
    