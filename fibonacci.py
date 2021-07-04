fib_terms=int(input("enter the no of terms"))
n1=0
n2=1
count=0
if fib_terms<=0:
	print("Enter the positive numbers greater than 1")
elif fib_terms==1:
	print(f"fibonacci series of {fib_terms} is {n1}")
else:
	print("The fibonacci series")
	while count<fib_terms:
		print(n1)
		nth=n1+n2
		n1=n2
		n2=nth
		count+=1