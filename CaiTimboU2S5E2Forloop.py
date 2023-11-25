"""U2S5E2Forloop
By Timbo
Done By Oct10"""
for i in range(100,0,-int(input())):
    print(i)
    if i % 13 == 0:
        continue
    if i == 20:
        break