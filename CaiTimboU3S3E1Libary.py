"""
U3S3E1Libary
By Timbo
Done By Oct 20
"""
import time
def questions():
    print("You have to answer the three questions in 30 sec")
    begin = time.perf_counter()
    question1 = int(input("What is 3 + 3?\n"))
    question2 = input("Is chess a sport?\n")
    question3 = input("What is the atomic weight of Carbon Dixiode\n")
    end = time.perf_counter()
    if begin - end == 30:
        questions()
    elif question1 != 6:
        questions()
    elif question2 != "yes":
        questions()
    elif question3 != "around 12":
        questions()
    else:
        print("WOW")
questions()
