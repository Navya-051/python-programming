num = int(input("Enter a number: "))

if num < 0:
    num = -num

if num < 10:
    print("Number of digits: 1")
elif num < 100:
    print("Number of digits: 2")
elif num < 1000:
    print("Number of digits: 3")
elif num < 10000:
    print("Number of digits: 4")
else:
    print("Number has 5 or more digits")
