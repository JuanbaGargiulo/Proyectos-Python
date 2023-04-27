# Two Sum: Given an array of integers, find 
# two numbers such that they add up to a specific target number. 
# Return the indices of the two numbers as an array

def TwoSum(Target):
	List = [1,2,3,4,5,6,7,8,9]
	List2 = [1,2,3,4,5,6,7,8,9]
	for j in List:
		for i in List2:
			if j+i == Target:
				print(f"Los numeros que dan {Target} son: {j}, {i} ")
				print("Cuyos indices son: ",List.index(j)," , ", List2.index(i))
				
				


Target = int(input("Ingrese el numero target: "))

TwoSum(Target)
