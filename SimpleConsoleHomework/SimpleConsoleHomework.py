import datetime
SrtdNums = []
i = 0
doc=open("hiworld.txt", "a")
try:

    k = input("How many numbers do you want to enter?")
    print("Type your numbers")
    while i < k:
        num = input()
        if (not num in SrtdNums) and (num % 5 == 0):
            SrtdNums.append(num)
        i = i + 1
    print ("Answer " + str(max(SrtdNums)))
    doc.write("\n")
    doc.write(str(SrtdNums)+str(datetime.datetime.now()))
except:
    print("Error")
finally:
    doc.close()
SrtdNums.sort()
print SrtdNums