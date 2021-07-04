lst=[]
lst2=[]
n=int(input("Enter the no of terms "))
for i in range (0,n):
	nos=int(input(f"Enter the {i+1} th numbers"))
	lst.append(nos)
print("Created list",lst)

for n in lst:
	if n>0:
		lst2.append(n)
		
print("The positive numbers list is  ",lst2)

	
	