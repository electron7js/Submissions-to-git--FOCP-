#gets a number from the user
number = input("Enter a number: ")

#typecasts the number variable to an integer
number = int(number)

#outputs the number entered to the screen
print("The numbered entered was", number)

#if the number is even prints even else odd
if (number % 2) == 0:
	print("That is an even number")
	if (number%10) == 0:
		print("And it is also divisible by 10")
else:
	print("That is an odd number")
