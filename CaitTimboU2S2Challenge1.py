"""U2S2Challenge
By Timbo
Done By Oct01 - Oct06"""
print("Enter your grade")

opinion = int(input())

if opinion >= 80:
    print("A")

elif opinion <79 and opinion>=70:
    print("B")

elif opinion <69 and opinion>=60:
    print("C")

elif opinion <59 and opinion>=50:
    print("D")

elif opinion <50 and opinion>0:
    print("F")

elif opinion >100:
    print("WOW!")

elif opinion < 0:
    print("ERROR")