import csv

lista = ["chandan", "sharma", "34", "65"]


with open("Names.csv", 'w', newline='') as file:
    write = csv.writer(file)
    write.writerows(lista)
