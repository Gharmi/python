numbers=[10,3,33,214,142,100]
x=int(input("Enter the number you want to search "))
length=len(numbers)
for a in range(length):
	if(x==numbers[a]):
		print("The number is at "+ str(a)+ " index")
		break

	elif(x!=numbers[a] and a==length-1):
		print("No such number in the list")
			
	