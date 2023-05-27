import datetime
def array_unique(array):
	unique = []
	for i in range(len(array)):
		if array[i] not in unique:
			unique.append(array[i])
	return unique 

var = 0

while var!=3:
	try:
		var = int(input("Выбери номер задачи(1 или 2) или введите 3 для выхода:"))
	except ValueError:
   		print("Это не число")
	if var!=0 and (var>3 or var<1):
		print("Число находится вне диапазона")
	else:
		if var == 1:
			new = 1
			arr = []
			print("Вводите значения для добавления в список по одному, для окончания ввода введите 0")
			while new!='0':
				new = input()
				if new!='0':
					arr.append(new)
			print("Исходный список: " + str(arr) + "\nСписок без повторений: " + str(array_unique(arr)))
		if var == 2:
			with open("group.txt", encoding="utf8") as file:
    				file = [line.rstrip() for line in file]
			students = []
			for line in file:
				students.append([line.split()[0], line.split()[1], datetime.datetime.strptime(line.split()[2], '%d.%m.%Y').date()])
			students = sorted(students, key = lambda x: x[2])
			for student in students:
				print(str(student[1]) + " " + str(student[0]) + " " + str(student[2]))