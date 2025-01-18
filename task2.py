# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

while True:
	n = input("n=")

	try:
		n = float(n)
	except ValueError:
		print("Пожалуйста, введите одно число цифрами.")
		continue

	if n > 100_000:
		print("Введите число, не превышающее 100 000")
		continue;
	if n < 0:
		print("Введите не отрицательное число")
		continue;
	if n % 1 != 0:
		print("Результат будет показан для ближайшего целого числа, которое меньше введенного Вами")

	n = int(n)

	if n == 0 or n == 1:
		print("0 и 1 уж точно не составные")
	else:
		simple_numbers=[2]
		for i in range(3, n+1, 2):
			if (i > 10) and (i%10==5):
				continue
			for j in simple_numbers:
				if j*j-1 > i:
					simple_numbers.append(i)
					break
				if (i % j == 0):
					break
			else:
				simple_numbers.append(i)
		if simple_numbers[len(simple_numbers)-1] == n:
			print("Число простое")
		else:
			print("Число составное")