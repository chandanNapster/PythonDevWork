import csv

try:
    file = open("Product.csv", encoding='utf-8')
    reader = csv.reader(file)
    for row in reader:
        print(row)
finally:
    file.close()

# THE BEST WAY TO CLOSE A FILE IS BY THE WITH STATEMENT
with open('Product.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# WE DO NOT NEED TO USE THE CLOSE METHOD WITH THE
# WITH STATEMENT WRITING TO A FILE

with open('Product.csv', 'a') as file:
    file.write("Chandan \t")
    file.write("is testing\n")
    file.write("The code\n")

with open('Product.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('Product.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["This", "is", "Just"])
    writer.writerow(["For", "Testing", "Purpose"])
    writer.writerow(["Hello", "There", "mate"])

with open('Product.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# WRITING MULTIPLE ROWS WITH writerows()
# writerow() and writerows() are two separate methods

csv_rowlist = [["SN", "This", "Is", "a", "Test"],
               [1, 2, 3, 4]]
with open('Product.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)

with open('Product.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# READING A CSV FILE AS A DICTIONARY
with open('Product.csv', 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(row)

# We can observe that entries of the first row
# are dict keys.
# While entries of other rows are dictionary values

# NEXT WE HAVE THE csv.DictWriter() class
# The objects of csv.DictWriter() class can be used

with open('Product.csv', 'a', newline='') as file:
    fieldnames = ['Product Name', 'Product ID',
                  'In Stock', 'Price']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # writer.writeheader()
    writer.writerow({'Product Name': 'Banana',
                    'Product ID': 'X345',
                     'In Stock': 'Yes', 'Price': 45})


with open('Product.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
