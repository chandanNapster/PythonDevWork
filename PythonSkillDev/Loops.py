# DEFINING VARIOUS VARIABLES AND USING CONDITIONALS
color = 'Red'
weight = 9

# if color == 'Red' and weight <= 10:
#     print("Red box with weight less than 10")
# elif color == 'Blue' and weight > 10:
#     print("Blue box with weight more than 10")
# else:
#     print("Box is neither Red nor Blue")

# ANOTHER WAY TO WRITE THE BOX SORT PROGRAM
# if color == 'Red' and (weight > 10 or weight <= 10):
#     print("Red box")
# elif color == 'Blue' and (weight > 10 or weight <= 10):
#     print("Blue box")
# else:
#     print("The box in neither Blue nor Red")

# SHORTHAND NOTATIONS
# Box = ""
# Box = "Red box" if color == 'Red' and (weight > 10 or weight <= 10) else "Blue box" if color == 'Blue' and (
#     weight > 10 or weight <= 10) else "Neither Blue nor Red"
# print(Box)

# NESTED CONDITIONAL STATEMENTS
# Box = ''
# if color == 'Blue':
#     if weight > 10:
#         Box = 'Blue box with weight greater than 10'
#     else:
#         Box = 'Blue box with weight less than 10'
# elif color == 'Red':
#     if weight > 10:
#         Box = 'Red box with weight greater than 10'
#     else:
#         Box = 'Red box with weight less than 10'
# else:
#     if weight > 10:
#         Box = 'Neither Red nor blue box with weight greater than 10'
#     else:
#         Box = 'Neither Red nor blue box with weight less than 10'

# print(Box)

# NESTED CONDITIONALS STATEMENTS PLUS THE TERNARY OPERATOR
# Box = ''
# if color == 'Blue':
#     Box = 'Blue box with weight greater than 10' if weight > 10 else 'Blue box with weight less than 10'
# elif color == 'Red':
#     Box = 'Red box with weight greater than 10' if weight > 10 else 'Red box with weight less than 10'
# else:
#     Box = 'Neither Red nor blue box with weight greater than 10' if weight > 10 else 'Neither Red nor blue box with weight less than 10'

# print(Box)

# Boxes = []
# Boxes.append('Box1')
# Boxes.append('Box2')
# Boxes.append('Box3')
# Boxes.append('Box4')
# Boxes.append('Box5')
# Boxes.append('Box6')

# count = 0
# while count < len(Boxes):
#     print(Boxes[count])
#     count = count + 1

# for box in Boxes:
#     print(box)

# for i in range(10):
#     print(i)

# for i in range(2, 10, 3):
#     print(i)

# for i in range(1, 20, 5):
#     print(i)


# for i in range(100):
#     if i >= 10 and i < 95:
#         continue
#     elif i == 96 or (i >= 3 and i <= 6):
#         pass
#     else:
#         print(i)
# else:
#     print("Loop ends")

# i = 0
# while i < 100:
#     i = i + 1
#     if i >= 10 and i < 95:
#         continue
#     elif i == 96 or (i >= 3 and i <= 6):
#         pass
#     else:
#         print(i)
# else:
#     print("Loop ends")


# print("Red box") if color == 'Red' and (weight > 10 or weight <= 10) else print(
#     "Blue Box") if color == 'Blue' and (weight > 10 or weight <= 10) else print("Neither Blue nor Red")

# color = ''
# weight = 40
# color = input("Enter color: ")
# weight = int(input("Enter weight: "))

# print(color is 'red')

# if (color.casefold() == 'red' and weight >= 40) or color == "Blue":
#     print("Red box weight 40")
# else:
#     print("Color is neither Red nor Blue")
