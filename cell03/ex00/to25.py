num = int(input("Enter a number less than 25\n"))

if num >= 25:
    print("Error")
for num in range(num, 26):
    print("Inside the loop, my variable is", num)