user_input_a = False
while user_input_a == False:
    try:
        a = int(input("num1: "))
        user_input_a = True
    except ValueError:
        print("Enter mfoking number")

user_input_b = False
while user_input_b == False:
    try:
        b = int(input("num2: "))
        user_input_b = True
    except ValueError:
        print("Enter mfoking number")

print('result', a + b)


