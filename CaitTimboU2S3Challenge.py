"""U2S3Challenge
By Timbo
Done By Oct01 - Oct06"""
category = input("Please choose a category:\nSports\nScience\nAnimals\nHistory\n\n")

if category == "Sports":
    print("Is Chess a Sport?\nA. Yes\nB. No\nC. What is Chess?")
    chose1 = input()
    if chose1 == "A":
        print("Correct")
    else:
        print("Wrong")


if category == "Science":
    print("What is the Atomic Weight of Carbon Dioxide?\nA.2\nB.200\nC.Around 12")
    chose2 = input()
    if chose2 == "C":
        print("Correct")
    else:
        print("Shouda Payed Attention in Science Class")

if category == "Animals":
    print("What is the Biggest Dog Breed?\nA. Corgi\nB. UR MOM\n C. The English Mastiff")
    chose3 = input()
    if chose3 == "C":
        print("Correct")
    else:
        print("Wrong get some help")

if category == "History":
    print("What did Hitler do to finish off France?\nA. Bomb Them\nB. Encircle them in Dunkirk\nC. Both")
    chose4 = input()
    if chose4 == "C":
        print("Correct")
    else:
        print("AND?")