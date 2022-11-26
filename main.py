import csv
print('what kind of animal are you interested in?\n')
try:
    animal = input().lower()
    with open(F"./data/{animal}.csv") as csv_file:
        animal_file = csv.reader(csv_file, delimiter=",")
        next(animal_file)
        for attr in animal_file:
            print(F"{attr[0]} is a{attr[1]} year old{attr[2]}.")
except:
    print(F"Sorry, we don't have any {animal} here.")
