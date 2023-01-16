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


#Program to print Left Half Pyramid
# num_rows = int(input("Enter the number of rows"));
# k = 1
# for i in range(0, num_rows):
#     for j in range(0, k):
#         print("* ", end="")
#     k = k + 1
#     print()


num_rows = int(input("Enter the number of rows "))
k = 0
for i in range(1, num_rows + 1): 
    for j in range (1, (num_rows - i) + 1): 
        print(end = " ")          
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
    k = 0   
    print()  
 
k = 2
m = 1
for i in range(1, num_rows): 
    for j in range (1, k):
        print(end = " ") 
    k = k + 1	  
    while m <= (2 * (num_rows - i) - 1): 
        print("*", end = "") 
        m = m + 1
    m = 1	
    print()

# aaar = [12, 34, 25, 62, 12, 13, 37, 88, 44]

# smallest = None
# for num in aaar:
#     if(smallest == None):
#         smallest = num
#     elif(num < smallest):
#         smallest = num
# print(smallest, 'smallest')