"""List Assessment

Fill in the following functions according to the directions in the 
docstrings.

"""


def get_indexed_items(items):
    """Given a list of items, get a list of items with their indices.

	Each item should be included in a tuple, formatted like::

	    (item, index) 

	So, the return value should be a list of tuples.


	Examples:
    
    If you got this list as input: ["Toyota", "Jeep", "Volvo"]
    You should return: [(Toyota, 0), (Jeep, 1), (Volvo, 2)]
    
    
    Another example input: ["Toyota", "Jeep", "Toyota", "Volvo"]
    Return value should be: [(Toyota, 0), (Jeep, 1), (Toyota, 2), (Volvo, 3)]

    """


def words_in_common(words1, words2):
    """Find words in common.
    
    Given 2 lists of words, return the words that are in common
    between the two, sorted alphabetically.
    
    **NOTE**: for this problem, you're welcome to use any of the
    Python data structures you've been introduced to (not just
    lists).
    
    For example, if you got these two lists as arguments:

    
    	["Python", "Ruby", "R", "C++", "Haskell"],
    	["Lizard", "Turtle", "Python"]
    
	Your return value should be:

    	['Python']


    The returned list should not have any duplicates.
        
        ["cheese", "bagel", "cake", "cheese"],
        ["hummus", "cheese", "beets", "kale", "bagel", "cake"]
        
	Would return

        ['bagel', 'cake', 'cheese']

    If there are no words in common, return an empty list::
        
        ["lamb", "chili", "cheese"],
        ["cake", "ice cream"]
    
    Would return    

        []

    If a duplicate exists in the original lists, the result will
    contain the value only once::
      
      ["Python", "Ruby", "R", "C++", "Haskell"]
      ["Lizard", "Turtle", "Python", "Python"]
    
    Would return    
    
        ['Python']

    """


def every_other_item(items):
    """Return every other item in `items`, starting at first item.
    
    For example, if you got this list as your argument:

        ['a', 'b', 'c', 'd', 'e', 'f']
    
    You would return:

        ['a', 'c', 'e']
    

	If you got this list as your argument:

    	["pickle", "pickle", "juice", "pickle", "juice", "pop"])
    
    You would return:

        ['pickle', 'juice', 'juice']
    


    Last example: 
    

    	["you", "z", "are", "z", "good", "z", "at", "x", "code"]
    
    Would return:

       ['you', 'are', 'good', 'at', 'code']
    """


def smallest_n_items(items, n):
    """Return the `n` smallest integers in list, in descending order.
    
    You can assume that `n` will be less than the length of the list.
    
    
    For example, if you got the following two arguments:
    
        [2, 6006, 700, 42, 6, 59], 3

    You would return

        [42, 6, 2]

    
    If n is 0, return an empty list:

        [3, 4, 5], 0

    Return:

    	[]

    
    If there are duplicates in the list, they should be counted
    separately:

    	[3, 1, 3, 2, 1, 1], 2
    
    Return:
    	[1, 1]

    """


def get_unique_characters(word):
	"""Given a string, return a sorted LIST of the unique letters.

	For example, if you got the string "olives" as the argument, 
	you should return the list ['e', 'i', 'l', 'o', 's', 'v']

	If you got the string "tissue" as the argument, you should return
	the list ['e', 'i', 's', 't', 'u']

	"""







