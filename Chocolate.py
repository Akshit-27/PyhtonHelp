mystr = input("Enter Money,Cost :")
mylst = mystr.split(",")

money = int(mylst[0])
cost  = int(mylst[1])

choco = money//cost
wrapper = money//cost

while wrapper//3 != 0 :
    choco = choco + wrapper//3
    wrapper = wrapper//3 + wrapper%3

print(choco)


#Enter Money,Cost :15,2
#10

