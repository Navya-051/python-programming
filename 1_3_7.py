s = input("Enter a string: ")

length = 0
vowels = 0
consonants = 0

for ch in s:
    length = length + 1
    if ch.lower() in 'aeiou':
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1

print("Total length:", length)
print("Vowels:", vowels)
print("Consonants:", consonants)
