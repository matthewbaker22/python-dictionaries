"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict(far = "situated at a great distance in space or time.")

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for word in word_definitions:
    print("The definition of", word, "is:", word_definitions[word])