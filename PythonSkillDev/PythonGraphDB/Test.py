import csv

lista = ["chandan", "sharma", "34", "65"]


with open("Names.csv", 'w', newline='') as file:
    write = csv.writer(file)
    write.writerows(lista)


def run():
    lista = [1, 1, 2, 3, 4]
    # seta = {1, 1, 1, 1, 2, 3, 4}
    seta = set(lista)

    print(seta)


if __name__ == '__main__':
    run()
