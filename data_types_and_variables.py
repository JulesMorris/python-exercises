# You have rented some movies for your kids: 
# The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), 
# and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, 
# how much will you have to pay?

def movie_cost(num):
    return num * 3

little_mermaid = movie_cost(3)
print (little_mermaid)

brother_bear = movie_cost(5)
print(brother_bear)

hercules = movie_cost(1)
print(hercules)

total_movie_cost = print(little_mermaid + brother_bear + hercules)

    #variables
l_m_days = 3
b_b_days = 5
h_days = 1 
total_cost = "$" + str(3 * (l_m_days + b_b_days + h_days))
print(total_cost)

# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. 
# How much will you receive in payment for this week? You worked 10 hours for Facebook, 
# 6 hours for Google and 4 hours for Amazon.

def gaf_pay (num1, num2, num3):
    g = 400 * num1
    a = 380 * num2
    f = 350 * num3
    return g + a + f

consulting_pay = gaf_pay(6, 4, 10)

print("I made $" + str(consulting_pay) + " in consulting work this week.")
    #variables
g_pay = 6 * 400
a_pay = 4 * 380
f_pay = 10 * 350

tech_comp = "I was paid $" + str(g_pay + a_pay + f_pay) + " in consulting fees this week."
print(tech_comp)


# A student can be enrolled to a class only if the class is not full and the class schedule 
# does not conflict with her current schedule.

room_in_class = True
has_conflict = False

enrollment_possible = room_in_class and has_conflict

print(enrollment_possible)



#A product offer can be applied only if people buys more than 2 items, and the offer has not expired. 
# Premium members do not need to buy a specific amount of products.

#def product_offer(num):
#has_expired = True
#    if has_expired == True:
#        print("Product offer unavailable.") #literally no idea what I'm going for here
#    elif has_expired = False and num > 2:
#        print("Product offer available")


promo_not_expired = True
premium_member = False
buy_two_or_more = True

get_promo = promo_not_expired and (premium_member or buy_two_or_more)
print(get_promo)



# Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:

    # the password must be at least 5 characters
    # the username must be no more than 20 characters
    # the password must not be the same as the username
    # bonus neither the username or password can start or end with whitespace
five_characters_or_more = len(password) >= 5
username_twenty_or_less = len(username) <= 20
user_pass_not_same = username != password
bonus_no_whitespace_user =  username == username.strip()
bonus_no_whitespace_pass = password == password.strip()

