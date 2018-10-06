"""
This program prints out the numbers between 1 and 100, but
prints fizz if the number if the multiple of 3,
prints buzz if the number is the multiple of 5,
prints fizzbuzz if the number is the multiple of 3 and 5.
"""

for i in range(1,101):
	output = ""

	if ( i%3 == 0 ): output += "fizz"
	if ( i%5 == 0 ): output += "buzz"
	
	if ( output == ""): output += str(i)

	print(output)
