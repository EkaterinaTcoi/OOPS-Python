number = int(input("Enter the number: "))
factorial = 1

if (number < 0):
    print("Can't Comput factorial for negative number!")
elif (number <2):
    print("{}! = {}".format (number, factorial))
else:
    for num in range (number,1,-1):
        factorial = factorial * num
    print("{}! = {}".format (number, factorial))