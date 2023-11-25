"""U2S2E2ElifStatment
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

elif opinion <59 and opinion>50:
    print("D")

elif opinion <50:
    print("F")