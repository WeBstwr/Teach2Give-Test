# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.
# Examples:
# 8=> returns true
# 6=> returns false

def power_of_two(n):
    return (n != 0) and (n & (n - 1)) == 0
print(power_of_two(30))
# "Expected Output : True if it's a power of 8")