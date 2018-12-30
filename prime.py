# n=input("Enter the value of n")
# for x in range(n):
# 	if x % 2==0:
# 		print(x)
# 
i=2
n=int(input("Enter the value "))
for i in range(2,n+1):
	for x in range(2,i+1):
		if i%x==0 and x!=i:
			break
		elif i%x==0 and i==x:
			print(i)
		
			




