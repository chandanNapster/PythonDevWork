import csv
csv_file = "D:\\UPES\Semester 1 2022\\Online Python Training\\PythonDevWork\\PythonSkillDev\\Product.csv"

# READ A CSV FILE AND OUTPUT THE CONTENTS AS A DICTIONARY
with open(csv_file, 'r') as file:
    c_file = csv.DictReader(file)
    for row in c_file:
        print(row)

# WE USE THIS CODE TO DELETE THE CONTENTS OF THE FILE
with open(csv_file, 'w') as file:
    file.truncate


# NEXT WE HAVE THE csv.DictWriter() class
# The objects of csv.DictWriter() class can be used

with open(csv_file, 'w', newline='') as file:
    fieldnames = ['Product Name', 'Product ID',
                  'In Stock', 'Price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Product Name': 'Banana',
                    'Product ID': 'X345',
                     'In Stock': 'Yes', 'Price': 45})
    writer.writerow({'Product Name': 'Apple',
                    'Product ID': 'X356',
                     'In Stock': 'Yes', 'Price': 25})
    writer.writerow({'Product Name': 'Pineapple',
                    'Product ID': 'X343',
                     'In Stock': 'Yes', 'Price': 67})
    writer.writerow({'Product Name': 'Orange',
                    'Product ID': 'Y256',
                     'In Stock': 'Yes', 'Price': 15})


# READ A CSV FILE AND OUTPUT THE CONTENTS AS A DICTIONARY
with open(csv_file, 'r') as file:
    c_file = csv.DictReader(file)
    for row in c_file:
        print(row)
