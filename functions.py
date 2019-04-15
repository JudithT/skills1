"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################


# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

   # 1.  Write a function that takes a town name as a string and returns
   #     `True` if it is your hometown, and `False` otherwise.
def print_town_name(hometown):
   return  hometown == "Chicago"

print(print_town_name("a"))



# 2.  Write a function that takes a first and last name as arguments and
#     returns the concatenation of the two names in one string.
def print_firstname_lastname(firstname,lastname):
   return  f" My name is {firstname} {lastname}"

print(print_firstname_lastname("Judith", "T"))

# 3.  Write a function that takes a home town, a first name, and a last name
#     as arguments, calls both functions from part (a) and (b) and prints
#     "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#     here', I'd like to visit 'town name here'!" depending on what the function
#     from part (a) evaluates to.
def print_person_introduction(firstname, lastname, hometown):
   if print_town_name(hometown) == True:
      return f"Hi, {firstname} {lastname} here, we're from the same place"
   else:
      return f"Hi, {firstname} {lastname} here, I'd like to visit {hometown}"

print(print_person_introduction("Miki", "ketcha", "Nyalla"))
print(print_person_introduction("cedric", "ketcha", "Chicago"))

# 4.  Write a function, `is_berry()`, which takes a fruit name as a string
#     and returns a boolean if the fruit is a "strawberry", "raspberry",
#     "blackberry", or "currant."
def is_berry(fruit):
   return  fruit == "strawberry" or fruit == "raspberry" or fruit == "blackberry" or fruit == "currant."
   
print(is_berry("pineapple"))
print(is_berry("blackberry"))

# 5.  Write another function, shipping_cost(), which calculates shipping
#     cost by taking a fruit name as a string and calling the `is_berry()`
#     function within the `shipping_cost()` function. Your function should
#     return 0 if is_berry() == True, and 5 if is_berry() == False.
def shipping_cost(fruit):
   if is_berry(fruit):
      return 0
   else:
      return 5

print(shipping_cost("banana"))


# 6.  Make a function that takes in a fruit name and a list of fruits. It should
#     return a new list containing the elements of the input list, along with
#     given fruit, which should be at the end of the new list.

def adding_a_new_fruit_to_list(fruit,list):
    list.append(fruit)
    return list

print(adding_a_new_fruit_to_list("banana", ["mango","pear","avocado"]))

# 7.  Write a function calculate_price to calculate an item's total cost by
#     adding tax and any fees required by state law.

def calculate_price(base_price,state,tax=.05):
   if state == "CA":
      total_cost = base_price + base_price * .03
   elif state == "PA":
      total_cost = (base_price +  base_price * tax) + 2 
   elif state == "MA":
      if base_price < 100:
         total_cost = (base_price + base_price * tax) + 1
      else:
         total_cost = (base_price + base_price * tax) + 3
   return total_cost

print(calculate_price(100, "CA"))
print(calculate_price(100, "MA", .05))
print(calculate_price(100, "PA"))

#     Your function will take as parameters (in this order): the base price of
#     the item, a two-letter state abbreviation, and the tax percentage (as a
#     two-digit decimal, so, for instance, 5% will be .05). If the user does not
#     provide a tax rate it should default to 5%.

#     CA law requires stores to collect a 3% recycling fee, PA requires a $2
#     highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#     items with a base price of $100 or less and $3 for items over $100. Fees are
#     added *after* the tax is calculated.

#     Your function should return the total cost of the item, including tax and
#     fees.