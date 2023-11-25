"""
U3S2E2ReturnFunctions
By Timbo
Done By Oct14
"""

def initals(fullname):
    print("Here is your initals")
    fullname = fullname.split()
    return fullname[0][0] + fullname[1][0]


print(initals(input("Enter Your Full Name\n")))
