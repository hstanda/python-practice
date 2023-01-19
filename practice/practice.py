# x = 0
# while x < 5:
#     print(f'Current vallue of x is {x}')
#     x = x + 1
# else:
#     print(f'Else x is {x}')

# def greet(lang):
#     if(lang== 'es'):
#         print("Holla")
#     elif(lang == 'fr'):
#         print('Bonjour')
#     else:
#         print('hello')

# greet('ss')


# x = 0
# while x < 5:
#     print('*', x)
#     x = x + 1


# num_rows = int(input("Enter the number of rows"));
# for i in range(0, num_rows):
# 	for j in range(0, num_rows-i-1):
# 		print(end=" ")
# 	for j in  range(0, i+1):
# 		print("*", end=" ")
# 	print()


# Program to print Left Half Pyramid
# num_rows = int(input("Enter the number of rows"));
# k = 1
# for i in range(0, num_rows):
#     for j in range(0, k):
#         print("* ", end="")
#     k = k + 1
#     print()


def print_stars(num_rows):
    import time
    if (num_rows > 15):
        num_rows = 15
    k = 0
    for i in range(1, num_rows + 1):
        time.sleep(1)
        for j in range(1, (num_rows - i) + 1):
            print(end=" ")
        while k != (2 * i - 1):
            print("*", end="")
            k = k + 1
        k = 0
        print()

    k = 2
    m = 1
    for i in range(1, num_rows):
        time.sleep(1)
        for j in range(1, k):
            print(end=" ")
        k = k + 1
        while m <= (2 * (num_rows - i) - 1):
            print("*", end="")
            m = m + 1
        m = 1
        print()


# def insert_into_datasbe(num):
#     import mysql.connector
#     mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="practice")
#     mycursor = mydb.cursor()
#     statement = ("INSERT INTO customers (name, address) VALUES ('John ' + {}, 'Highway ' + {})".format(num, num))
#     mycursor.execute(statement)
#     mydb.commit()

# data = [12, 34, 25, 62, 12, 13, 37, 88, 44]
# smallest = None
# for num in data:
#     if (smallest == None):
#         smallest = num
#     elif (num < smallest):
#         smallest = num
#     insert_into_datasbe(num)
#     # print_stars(num)

# print(smallest, 'smallest')


counts = dict()
names = ["Jack", "Michel", "Savrin", "Cherry", "Jack",
         "Michel", "Savrin", "Jason", "Alia", "Savrin"]
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] = counts[name]+1

# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# for key, value in counts.items():
#     print(key, 'is ', value, 'times')


# name = input("Enter the file name")
# handle = open(name)
handle = open("sample.txt")

times = dict()
for line in handle:
    words = line.split()
    for word in words:
        times[word] = times.get(word, 0)+1

bigCount = None
bigWord = None

for word, count in times.items():
    if bigCount is None or count > bigCount:
        bigCount = count
        bigWord = word

print(bigWord,bigCount)
