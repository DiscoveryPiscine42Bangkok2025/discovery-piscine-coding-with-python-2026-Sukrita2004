f = int(input("Enter the first number:\n"))
s = int(input("Enter the second number:\n"))
result = f * s

print(f"{f} x {s} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")