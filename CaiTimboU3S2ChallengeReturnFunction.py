"""
U3S2ChallengeReturnFunctions
By Timbo
Done By Oct14
"""
def pname(n):
    
    if n %3 == 0:
        return("pomplamouse")
    else:
        return n
    
def pnam(n):
    inttostring = str(n)
    for i in range(len(inttostring)):
        if inttostring[n] == "3":
            return("pomplamouse")
        
print(pname(int(input("Enter in a number\n"))))
print(pnam)