# Algoritmo que pida dos números
# Y muestre todos los números que van desde el primero al segundo
# Se debe controlar que los valores son correctos

###############################################################################

# Copyright (c) 2018 Kevin Leal <jordi.222@hotmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

###############################################################################

print("This program will take two numbers, and display all numbers between them")

number1 = 0 
number2 = 0
top = 0  # It can be either number1 + 1 or number2 - 1 depending of which is higher
string = ""
count = 0

while True:
    try:
        number1 = int(input("Enter your first number: "))
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try the first number again") 

while True:  
    try:
        number2 = int(input("Enter your second number: "))
        break   	
    except ValueError:
        print("Oops!  That was not a valid number.  Try the second number again")
    

if number1 == number2:
	print("Number are equal, no other numbers to show")

else:
	if number1 < number2:
		count = number1
		top = number2 - 1
		while count != top:
			count = count + 1
			string = string + str(count) + ", "
		
		print("The numbers between " + str(number1) + " and " + str(number2) + " are: " + string)
	
	else:
		count = number1
		top = number2 + 1
		while count != top:
			count = count - 1
			string = string + str(count) + ", "
		
		print("The numbers between " + str(number1) + " and " + str(number2) + " are: " + string)

