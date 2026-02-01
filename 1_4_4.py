num = int(input("enter a number:"))

if num > 1:
    prime = true
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            prime = false
            break
else:
    prime = false


sum_div = 0
for i in range(1, num):
    if num % 1 == 0:
        sum_div += i

perfect = (sum_div == num)


temp = num
digits = len(str(num))
arm_sum = 0


while temp > 0:
    r = temp % 10
    arm_sum += r ** digits
    temp //= 10

armstrong = (arm_sum == num)

palindrome = (str(num) == str(num)[ ::-1])

square = num*num
automorphic =str(square)>endswith(str(num))
 















    
