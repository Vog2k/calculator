'''When ready insert the number - eventually

Below this line is all the juicy stuff involving the code to multiply and subtract ect
Writing this line below made me realise that arrays exisit and i should use them instead of trying to write new vars for each symbol'''
while True:
    array = "Addition", "Subtraction", "Multiply", "Divide"
    Addition = "+"
    # This line adds to the equation
    Subtraction = "-"
    # This line subtracts from the equation
    Divide = "/"
    # This line divides two numbers also I had to Google how to write the divide sign and its (alt + 0247)
    Multiply = "*"
    # alt + 0215 to get the multiply sign. This multiplies the current number

    first_number = input("first number :")
    # first number is the start of this equation

    Symbol = input(array)
    # This should bring up an array of different symbols for the user to chose from

    second_number = input("second number :")
    # Second number is the start of this equation
    ''' I have discovered that putting int in front of first and second makes this function know it's a plus or minus ect.
    doing this made me run into errors with decimal points we just learned about float today so i will try replace int for float'''

    # Original code: result = float(first_number) + float(second_number)
    '''This line below took me at least two hours to understand,
    but as i add an if statement and the variable this sets up my demand telling the system if '==' this is equal to the symbol from
    the array i created "+" then tell the system to print the first number and plus the second number aswell giving the results for your equation
    then pretty much from there i just copy and past the same code for the other symbols'''
    if first_number == "Q" or first_number == "q":
        break

    if Symbol == "+":
        print(first_number, "+", second_number, "=", (int(first_number) + int(second_number)))
    elif Symbol == "*":
        print(first_number, "*", second_number, "=", (int(first_number) * int(second_number)))
    elif Symbol == "-":
        print(first_number, "-", second_number, "=", (int(first_number) - int(second_number)))
    elif Symbol == "/":
        print(first_number, "/", second_number, "=", (float(first_number) / float(second_number)))
    print("Press Q or q to exit")

print("Application ended thank you")

''' I kept running into a wall while doing these elif statements because i didn't set up float in front of the
numbers that will equal to a decimal or have int in front of the whole numbers'''

# print("result" + str())

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

Numbers, Strings, Boolean

Comparison operators
< less than
< less than or equal to
> grater than
>= grater than or equal to
== equal
!= not equal 





'''
