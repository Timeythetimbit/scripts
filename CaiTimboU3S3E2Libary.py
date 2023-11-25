"""
U3S3E2Libary
By Timbo
Done By Oct 24
"""
import random
import time

roll = 0

begin = time.perf_counter

playersroll = 0
computersroll = 1

while playersroll<computersroll:
    input("Roll the dice\n")
    roll += 1
    playersroll = random.randint(1,12)
    computersroll = random.randint(1,12)

    if playersroll<computersroll:
        print("Try again")

    else:
        print("You win, you rolled", roll, "time/s")
        break
