x = input()
y = ""
for i in range(len(x)):
    if x[i] == x[i].upper():
        y+=x[i].lower()
    else:
        y+=x[i].upper()

print(y)