# with open('test.txt', mode='a') as myFile:
#     myFile.write("\nFIFTH")
# with open('test.txt', mode='r') as myFile:
#     text = myFile.read()
#     print(text)
# with open('test.txt', mode='w') as myFile:
#     myFile.write("FIRST\nSECOND\nTHIRD")
# with open('test.txt', mode='r') as myFile:
#     text = myFile.read()
#     print(text)

# items = ['q', 'w', 'e', 'r', 'y']
items = [1, 2, 3, 4, 5]

sum = 0
for item in items:
    sum = sum+item
    # print(sum)
print(sum)

dictionery = {
    "apple": 10,
    "banana": 21,
    "orange": 16,
    "grapes": 14,
}

for key, value in dictionery.items():
    print(key + " Price is : " + str(value))
