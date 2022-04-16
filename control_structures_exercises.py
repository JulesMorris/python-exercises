
#1)
# a) prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input('Enter the day of the week: ')

if day_of_week.startswith('Mon'):
    print('The day of the week is Monday.')  
else:
    print('That day is not a Monday.')

# a) review:

day = input('Please enter the day of the week: ')
day = day.lower()

if day in ['monday', 'mon']:
    print('Today is Monday.')
else:
    print(f'Today is {day.capitalize()}')


# b) prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input('Please enter a day of the week: ')

if day_of_week.lower().startswith('s'): #can chain together lower() and startswith(), 's' for Saturday or Sunday
    print(f'{day_of_week}, the weekend is here!')
else:
    print(f'{day_of_week}, it is not the weekend.')

# b) review:

day = input('Please enter the day of the week: ')

#while day is not valid weekday:
    #keep prompting for an input
while day.lower() not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
    print('Invalid input. Please enter full name of day.')
    day = input('Please enter the day of the week: ')
    
if day.lower() in ['sunday', 'saturday']:
    print('Today is the weekend.')
else:
    print('Today is a weekday.')

 # c) create variables and make up values for
        #the number of hours worked in one week
        #the hourly rate
        #how much the week's paycheck will be

    #write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
    
num_hours_worked = 47
hourly_pay = 120


if num_hours_worked > 40:
    ot_hours = num_hours_worked - 40
    ot_pay = ot_hours * hourly_pay * 0.5
else:
    ot_pay = 0

weekly_pay = num_hours_worked * hourly_pay + ot_pay
print(weekly_pay)

# c) review:

hours_worked = 45
hourly_rate = 50
overtime_rate = hourly_rate = 1.5

if hours_worked <= 0:
    total_pay = hours_worked * hourly_rate
    
else:
    regular_pay = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * overtime_rate
    total_pay = regular_pay + overtime_pay
    
print(total_pay)

# 2)

#  a1. Loop Basics While
        # Create an integer variable i with a value of 5.
        # Create a while loop that runs so long as i is less than or equal to 15
        # Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(f"i = {i}") #In Python source code, an f-string is a literal string, prefixed with f , which contains expressions inside braces. The expressions are replaced with their values.
    i += 1

#    a2. Create a while loop that will count by 2's starting with 0 and ending at 100. 
#Follow each number with a new line.
i = 0
while i <= 100:
    print(i)
    i += 2 #this is the same as i = i + 2

 #   a3. Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print( f" i = {i}")
    i -= 5 #this is the same as i = i - 5

#   a4. Create a while loop that starts at 2, 
# and displays the number squared on each line while the number is less than 1,000,000. 

i = 2

while i < 1000000:
    print(f" i = {i}")
    i **= 2
   
#   a5. Create a while loop to count backwards from 100 using increments of 5.

i = 100

while i >= 5:
    print(f" i = {i}")
    i -= 5

# 2) 
#   2a. Loops
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number
x = int(input("Enter a number:"))

for i in range(1, 11): #this gives the range of 10 needed to multiply a number to ten.
    print(f'{x} x {i} = {x * i}')

#   2b. Create a for loop that uses print to create the output shown below. 1, 22, 333, 444, as a pyramid up til 9

for i in range(1, 10):
    print(str(i) * i) #must make a string to put them together without an arithmetic function

#   2c. 
# 2) 3a) break and continue. Prompt the user for an odd number between 1 and 50. Use a loop and a break statement 
#to continue prompting the user if they enter invalid input. 
#(Hint: use the isdigit method on strings to determine this). 
#Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
#except for the number the user entered.


while True: #this creates an infinite loop until the condition is met
    x = input("Enter an odd number between 1 and 50: ") 
    if x.isdigit():
        x = int(x)
        if x % 2 == 0:
            continue
        break
        #need to keep prompting user input but not sure how/where it goes...

        
i = 1
while i <= 50:
    if i == x:
        print(f"Skipping number: {i}")
        i += 2
        continue
    print(f"This number is odd: {i}")
    i += 2


 #More succinct from review:
#isdigit = False
# > 50
# <= 0
# num % 2 == 0
#keep asking for input

num = input('Please enter an odd number between 1 and 50: ')
    
while True:
    if (num.isdigit == False or int(num) > 50 or int(num) < 1 or int(num % 2 == 0)):
        print('Invalid input')
        num = input('Please enter an odd number between 1 and 50: ')
    else:
        break
        
#convert input string to an interger        
num = int(num)

 #2) 3b. The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the input 
# function returns a string, so you'll need to convert this to a numeric type.)

while True:
    x = input("Enter a positive number: ")
    if x.isdigit(): #have to use isdigit() to determine if it is a digit
        x = int(x) #must convert to int
        if x <= 0: #to ensure positive number, check to see if input is <= 0
            continue #continues loop 
        break
        
for i in range(0, x + 1): #used to create the count starting at 0 and the range is x + 1 to stop count at x
    print(i) #print user input

#from review:
#while
#isdigit == False
# > 0
#keep asking for input

while True:
    if (num.isdigit() == False or int(num < 0)):
        print('Invalid input')
        num = int(num)
    else:
        break
        
num = int(num) #convert str to int

for i in range(0, num + 1):
    print(i)

# 2) e. Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
    x = input("Enter a positive interger: ")
    if x.isdigit():
        x = int(x)
        if x <= 0:
            continue
    break
    
for i in range(x, 0, -1): #x is the starting place, 0 is exclusive thus stops at 1, -1 is the increment (countdown) by one
    print(i)

#from review:
num = input('Please enter a positive number greater than 0: ')

while True:
    if (num.isdigit() == False or int(num) < 0):
        print('Invalid input')
        num = input('please enter a positive number greater than 0: ')
    else:
        break
num = int(num)

#countdown using reverse range, the default increment (third arg in range, is 1)
for i in reversed(range(1, num + 1)):
    print(i)

# 3)Fizzbuzz

#One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
#Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

    #Write a program that prints the numbers from 1 to 100.
    #For multiples of three print "Fizz" instead of the number
    #For the multiples of five print "Buzz".
    #For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0: #this has to be first or you don't ever get "fizzbuzz"
        print("Fizzbuzz")
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print(i)

    
# 4) Display a table of powers.

    #Prompt the user to enter an integer.
    #Display a table of squares and cubes from 1 to the value entered.
    #Ask if the user wants to continue.
    #Assume that the user will enter valid data.
    #Only continue if the user agrees to.
    
x = int(input("Enter an interger: "))

print() #for some reason doesn't run w/o a print statement here
print("number | squared | cubed") #headers
print("______ | _______ | _____") # bottom border


for i in range(1, x + 1):
    print("%6d | %7d | %5d" % (i, i**2, i**3)) #the modulo here in %6d creates column at least 6 spaces wide
    #the % that separates the column dimensions allows the columns to be filled accordingly separated by comma

#solution from review
num = input("Please enter a positive interger: ")

print("Here is your table!")
print("number | squared | cubed") #headers
print("______ | _______ | _____") # bottom border

num = int(num)
for i in range (1, num + 1):
    print(f' {i} | {i **2} | {i ** 3}') #formatted string to match the column req's
    #print('{:^6} | {:^7} | {:^5}'.format (i, i ** 2, i ** 3)) #'^'followed by number is the number of spaces mid aligned
    #print('{:6} | {:7} | {:5}'.format (i, i **2, i ** 3)) #right aligned -default
    #print('{:<6} | {:<7} | {:<5}'.format (i, i ** 2, i ** 3)) # left aligned

#solution from review centered
num = input("Please enter a positive interger: ")

print("Here is your table!")
print("number | squared | cubed") #headers
print("______ | _______ | _____") # bottom border

num = int(num)
for i in range (1, num + 1):
    print('{:^6} | {:^7} | {:^5}'.format (i, i ** 2, i ** 3)) #'^'followed by number is the number of spaces mid aligned

#solution from review right-aligned
num = input("Please enter a positive interger: ")

print("Here is your table!")
print("number | squared | cubed") #headers
print("______ | _______ | _____") # bottom border

num = int(num)
for i in range (1, num + 1):
    print('{:6} | {:7} | {:5}'.format (i, i **2, i ** 3)) #right aligned -default

#solution from review left-aligned
num = input("Please enter a positive interger: ")

print("Here is your table!")
print("number | squared | cubed") #headers
print("______ | _______ | _____") # bottom border

num = int(num)
for i in range (1, num + 1):
    print('{:<6} | {:<7} | {:<5}'.format (i, i ** 2, i ** 3)) # left aligned

# 5) #Convert given number grades into letter grades.

    #Prompt the user for a numerical grade from 0 to 100.
    #Display the corresponding letter grade.
    #Prompt the user to continue.
    #Assume that the user will enter valid integers for the grades.
    #The application should only continue if the user agrees to.

    #Grade Ranges:
        #A : 100 - 88
        #B : 87 - 80
        #C : 79 - 67
        #D : 66 - 60
        #F : 59 - 0

#Bonus

    #Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).
    


while True:
    
    x = int(input("Enter numerical grade: "))
    x = int(x)
    
    if x >= 88:
        print("A")
    elif x >= 80:
        print("B")
    elif x >= 67:
        print("C")
    elif x >= (60):
        print("D")
    else:
        print("F")
#from review        
    choice = input("Do you want to continue? Please enter yes or y to continue:")
    if choice.lower() in ['yes', 'y']:
        continue
    else:   
        break
    
