myTable = [15, 95, 17, 34]
save = 0
plusGrand = 0

for i in range (len(myTable)):
    if myTable[i]<myTable[i-1]:
            save = myTable[i]
            myTable[i]=myTable[i-1]
            myTable[i-1]=save
print(myTable)