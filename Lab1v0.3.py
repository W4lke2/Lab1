while var!=3:
	try:
		var = int(input("Выбери номер задачи(1 или 2) или введите 3 для выхода:"))
	except ValueError:
   		print("Это не число")
	if var>3 or var<1:
		print("Число находится вне диапазона")
	else:
		if var == 1:
			print("Здесь будет первое задание")
		if var == 2:
			print("А тут второе")