a = ["Adam", "Liam", "Ellie", "James", 10]
ages = [10 , 24, 21, 10, 11]

zipped = tuple(zip(a, ages))
print(zipped)

names, ages = zip(*zipped)

print("Name" + str(names) + "Ages" + str(ages))
