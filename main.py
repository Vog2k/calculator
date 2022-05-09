'''When ready insert the number - eventually

Below this line is all the juicy stuff involving the code to multiply and subtract ect .... '''

# String of words that display as the programme run's

#Writing this line below made me realise that arrays exisit and i should use them instead of trying to write new vars for each symbol
array = ("Addition", "Subtraction", "Multiply", "Divide")

Addition = "+"
# This line adds to the equation
Subtraction = "-"
# This line subtracts from the equation
Divide = "÷"
# This line divides two numbers also I had to Google how to write the divide sign and its (alt + 0247)
Multiply = "×"
# alt + 0215 to get the multiply sign. This multiplies the current number


first_number = input("first number :")
# first number is the start of this equation

Symbol = input(array)
#'-'='+'='×'='÷'='array'
# This should bring up an array of different symbols for the user to chose from

second_number = input("second number :")
# Second number is the start of this equation
''' I have discovered that putting int in front of first and second makes this function know it's a plus or minus ect.
doing this made me run into errors with decimal points we just learned about float today so i will try replace int for float'''

result = float(first_number) + type(array) + float(second_number)

'''running into an error i had to write a str in front of result because it wouldn't recognise the float'''
print("result" + str(result))

'''print("#1 Plus")
print("#2 Minus")
print("#3 Times")
print("#4 Divide")'''

'''
Below this line is my little cheat sheet.

(Int) or integer, is a whole number, positive or negative, without decimals, of unlimited length.
(Ranges) returns a sequence of numbers starting from zero and increment by 1 by default and stops before the given number.
(Variable) symbolic name that is a reference or pointer to an object
(Array) collection of common type of data structures having elements with same data type

unfinished code
Input = input("Please enter an equation  ")
Equals = input("")
num_input = ('0') - int(Equals)
float('inf')

Numbers, Strings, Boolean'''
