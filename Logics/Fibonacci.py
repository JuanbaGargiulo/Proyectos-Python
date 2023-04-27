
def Fibonacci():
	#FN = FN-1 + FN-2
	num1 = 0
	num2 = 1
	print(num1)
	print(num2)
	while True:
		total=num1+num2
		num1=num2
		num2=total
		print(total)
		if total >120:
			break
		

Fibonacci()
