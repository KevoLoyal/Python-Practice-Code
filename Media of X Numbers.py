# Algoritmo que calcule la media de X números.  
# Se dejará de solicitar números hasta que se introduzca el valor 0 cero. 


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

i = 0 # Just to track the quantity of numbers entered
total_sum = 0
exit = False

print ("This program will ask for numbers until 0 is entered")
print ("Once 0 is entered, it will calculate the average")

while exit == False:
	number = input("Enter a number, or enter 0 to exit: ")
	x = int(number)
	if x == 0:
		exit = True
	else:
		total_sum = total_sum + x
		i = i + 1

average = int(total_sum / 2)
print ("From the",i,"numbers entered, The average is: ", average)
print ("Thank you for playing")

