# Digits
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[-3])
print("=====================================")
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[:3])
print("=====================================")
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(digits[5:0:-2])

for i in range(len(digits)):
    print(digits[0:i])

for i in range(len(digits)):
    print(digits[i:i+3])


# Name
print("=====================================")
name = "Hello World"
print(name[:6])
