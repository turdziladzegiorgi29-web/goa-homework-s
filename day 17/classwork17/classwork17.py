# lists are a type of "variable" that holds more than 1 word/number
# lists can also hold multiple data types for example it can hold a string and a integer in the same list :)
# list1=["walmart bag", "croissiant", "rickroll guy"]
# print(list1[2])
# list2=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
# for i in list2:
#     if i % 3 == 0:
#         print(str(i) + " is divisible by 3")

list3=["giga", "lasha",  "giorgi", "daviti"] 
count=0
username=input()
for i in list3:
    if username == i:
        print(username)
        count += 1 
print(count)