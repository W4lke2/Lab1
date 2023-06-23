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
	if var>3 or var<1:
		print("Число находится вне диапазона")
	else:
		if var == 1:
			new = 1
			arr = []
			print("Вводите числа для добавления в список по одному, для окончания ввода введите 0")
			while new!=0:
				try:
					new = int(input())
				except ValueError:
   					print("Это не число")
				if new!=0:
					arr.append(new)
			print("Исходный список: " + str(arr) + "\nСписок без повторений: " + str(array_unique(arr)))
		if var == 2:
			print("А тут второе")