from sys import argv

work_hours, rate, bonus = float(argv[1]), float(argv[2]), float(argv[3])

salary = round((work_hours * rate + bonus), 2)
print(f'Заработная плата будет составлять: {salary}')
