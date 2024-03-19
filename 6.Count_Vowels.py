# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.
# eg " Hello World " => returns 2

def count_vowels(s):
    vowels =  'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count
print(count_vowels("What a world we live in")) 