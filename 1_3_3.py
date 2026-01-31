
s = input("Enter a string: ")

print("Characters in forward order:")
i = 0
while i < len(s):
    print(s[i], end=" ")
    i += 1

print("\n")

# Reverse order
print("Characters in reverse order:")
i = len(s) - 1
while i >= 0:
    print(s[i], end=" ")
    i -= 1
