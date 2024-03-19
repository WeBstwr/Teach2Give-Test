# Question 4: Capitalize Words
# Write a program that accepts a string as input, capitalizes the first letter of each word in the
# string, and then returns the result string.
# Examples:
# "hi"=> returns "Hi"
# "i love programming"=> returns "I Love Programming"

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())
print(capitalize_words("my name is webster ifedha safala"))
