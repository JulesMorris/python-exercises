# 1)
# Define a function named is_two. It should accept one input and return True if the passed input is either 
#the number or the string 2, False otherwise.
def is_two(x):
    if x == 2 or x == 'two'.lower():
        return True
    else:
        return False
    
is_two(4)

# 1) Review : -_- 

def is_two_rev(n):
    return n == 2 or n == '2'

is_two_rev(2)
is_two_rev('2')
is_two_rev(2.0)

# 2) 
# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(str):
    if str in 'aeiou'.lower():
        return True
    else:
        return False
    
is_vowel('y')

# 2) Review: -_-

def is_vowel_rev(somestring):
    if type(somestring) == str:
        result = somestring.lower() in ['a', 'e', 'i', 'o', 'u']
        return result
    else:
        return False
    
is_vowel_rev('aeiou') #returns false because not single character, as parsed out in list which more explicit


# 3) Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.

def is_consonant(str):
    if str not in 'aeiou'.lower():
        return True
    else:
        return False
    
is_consonant('thy')
    
# 3) Review:

def is_consonant_rev(somestring):
    if type(somestring) == str:
        only_letters = somestring.isalpha()
        return only_letters and not is_vowel_rev(somestring)
    return False

# 4) Define a function that accepts a string that is a word. The function should capitalize the first letter 
# of the word if the word starts with a consonant.

def cap_con(word):
    starts_with = word[0] #index of first letter
    if starts_with not in 'aeiou'.lower():
        return word.capitalize()
    else:
        return word
    
cap_con('apple')
cap_con('thy')

# 4) Review: -_-

def capitalize_starting_consonant(string):
    if type(string) != str:
        return False
    first_letter = string[0]
    if is_consonant(first_letter):
        string = string.capitalize()
    return string

capitalize_starting_consonant('apple')

# 5) Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and 
# the bill total, and return the amount to tip.

if __name__ == '__main__':
    def calculate_tip():
        bill = input("How much was the total bill? ")
        x = float(bill)
        tip_amts = [10, 15, 20, 25]
        for tip in tip_amts:
            print(f"If you want to leave a {tip}% tip, the tip amount will be ${x*tip/100:.2f}.")
        #total_tip = x * tip / 100         
        #print(f"Your total tip is ${total_tip:.2f}.")          
    
    
    
# calculate_tip()    

# 5) Alt:

def calculate_tip2(per, bill): # -_- why is this so simple?
    return per * bill

# 5) Review:

def calculate_tip_rev(bill, tip_percentage=0.2):
    if type(bill) != float:
        return False
    if tip_percentage < 0 or tip_percentage > 1:
            return 'the tip percentage must be between 0 and 1'
    return tip_percentage * bill



# 6) Define a function named apply_discount. It should accept a original price, and a discount percentage, 
# and return the price after the discount is applied.
if __name__ == '__main__':
    def apply_discount(price, discount):
        ds = price * (discount / 100)
        sp = price - ds
        sp = round(sp, 2)
        return sp

    ori_price = float(input("Original price: "))
    disc_percent = int(input("Discount percentage: "))
    disc_price = ori_price - disc_percent
    print(f"The discounted price is: ${disc_price:.2f}")

#6 Review:

def apply_discount_rev(price, discount_percentage):
    discount = price * discount_percentage
    return price - discount

# 7) Define a function named handle_commas. It should accept a string that is a 
# number that contains commas in it as input, and return a number as output.
def handle_commas(x):
    return (float(x.replace("," , ""))) #must change to float

handle_commas("1,000,000,000.00")

# 7) Review

def handle_commas_rev(somestring):
    if type(somestring) != str:
        return 'input must be a string'
    somestring = somestring.replace(',', '')
    if somestring.isdigit():
        return float(somestring)
    else:
        return 'input must be a string that is a number'

# 8) Define a function named get_letter_grade. It should accept a number and return the 
# letter grade associated with that number (A-F).

def get_letter_grade(num_grade):
    if num_grade > 90:
        return "A"
    elif num_grade > 80:
        return "B"
    elif num_grade > 70:
        return "C"
    else:
        return "F"
    
get_letter_grade(75)

# 8) Review


def get_letter_grade_rev(grade):
    if type(grade) == int or type(grade) == float:
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"
    else:
        return 'Input must be a number'
    

# 9) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    for i in 'aeiou'.lower():
        word = word.replace(i, "")
    return word

remove_vowels("banana")

# 9) Review

def remove_vowels_rev(somestring):
    if type (somestring) != str:
        return False
    output = ''
    for letter in somestring:
        if is_consonant_rev(letter):
            output += letter
    return output

# 10)Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:

    #anything that is not a valid python identifier should be removed
    #leading and trailing whitespace should be removed
    #everything should be lowercase
    #spaces should be replaced with underscores
    #for example:
        # Name will become name
        # First Name will become first_name
       # % Completed will become completed

    
def normalize_name(word):
    invalid_character = ['!', '@,', '#', '$', '%', '^', '&', '*', '(' ,')', '<', '>,' ,'?', ';', ':', '~', '`', '+', '=', '{', '}', '[', ']' , '-', " "]
    for i in invalid_character:
        word = word.replace(i, '_')
    word = word.strip()
    return word.lower()

normalize_name("First Name") 

# 10) My alt:

def normal_name (s):
    valid_chara = []
    for chara in s:
        if chara.isidentifier() or chara == ' ':
            #print(valid_chara)
            valid_chara.append(chara)
    valid_chara = ''.join(valid_chara)
    #print(valid_chara)
    valid_chara = valid_chara.strip()
    valid_chara = valid_chara.lower()
    valid_chara = valid_chara.replace(" ", "_")
    return valid_chara


normal_name("First Name")
normal_name("%fl!")

# 10) Review:

def normalize_name_rev(string):
    output = ''
    string = string.lower()
    for character in string:
        if character.isidentifier() or character == ' ':
            output += character
    output = output.strip()
    output = output.replace(' ', '_')
    return output
  
normalize_name_rev("@l!s 0n")  

# 11) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is 
# the cumulative sum of the numbers in the list.

    #cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    #cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]
    
def cumulative_sum(num_list):
    sum_of_list = [num_list[0]]
    for i in num_list [1:]:
            previous_sum = sum_of_list[-1]
            sum_of_list.append(previous_sum + i)
    return sum_of_list

cumulative_sum([1, 2, 3])

# 11) Review:

def culmulative_sum_rev(somenums):
    output = []
    for i, num in enumerate(somenums):
        sum_so_far = sum(somenums[:i + 1])
        output.append(sum_so_far)
    return output