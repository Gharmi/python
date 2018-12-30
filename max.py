numbers=[18,23,31,2313,4,9]
p=len(numbers)
max=numbers[0]
for x in range(1,p):
	if(max<numbers[x]):
		max=numbers[x]
print(max)

