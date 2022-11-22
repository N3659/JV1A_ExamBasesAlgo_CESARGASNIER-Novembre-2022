myTable = [15, 95, 22, 19]
save = 0

for i in range (len(myTable)):
    for n in range (i-1):
        if myTable[n]>myTable[i]:
            save = myTable[i]
            myTable[i] = myTable[n]
            myTable[n] = save

print(myTable) 