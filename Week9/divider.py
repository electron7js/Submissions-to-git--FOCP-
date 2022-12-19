try:
    dividend = input("Enter the first number: ")
    divisor = input("Enter the second number: ")
    quotient = float(dividend)/float(divisor)

except ZeroDivisionError:
    print("The second value was 0 (cannot divide by 0)")

except ValueError:
    print("Entered values must be numbers")
else:
    print("First divided by second is", quotient)
finally:
    print("The divider program has finished")
