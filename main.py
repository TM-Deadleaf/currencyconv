with open("currenncy.txt") as f:
    lines=f.readlines()
currentDict={}
for line in lines:
    parsed=line.split("\t")
    currentDict[parsed[0]]=parsed[1]# adding values to the dictionary
amount=float(input("enter the amount:\n"))
print("enter the currency  to which you want to convert to?")
for item in currentDict.keys():
    print(item)
cur=input("enter the currency from above options:\n")
print("{} INR is equal to {} {}".format(amount,amount*float(currentDict[cur]),cur))

