str=input("enter the value of ur string:")

vowels="aeiouAEIOU"

count=0
for ch in str:
    if ch in vowels:
            count+=1
            print(f"the num of vowels in the {str} are {count}")
