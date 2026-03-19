# Find all occurrences of the word "hello" in a given string and print their positions.
def find_hello_positions(input_string):
    positions = []
    word = "hello"
    index = input_string.find(word)
    
    while index != -1:
        positions.append(index)
        index = input_string.find(word, index + 1)
    
    return positions
# Example usage
input_string = "hello world, hello everyone!"
positions = find_hello_positions(input_string)
print(f"The word 'hello' is found at positions: {positions}")

# Reverse string

# option 1: using slicing
def reverse_string(input_string):
    return input_string[::-1]
# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")

# option 2: using a loop
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string
# Example usage
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")

# check if a string is a palindrome
def is_palindrome(input_string):
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]
# Example usage
input_string = "madam"
print("is Palindrome:", is_palindrome(input_string))

# count the frequency of each character in a string
#option 1: Actual logic
def character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency
# Example usage
input_string = "hello world"
frequency = character_frequency(input_string)
print("Character frequency:", frequency)

# option 2: using collections.Counter
from collections import Counter
def character_frequency(input_string):
    return Counter(input_string)
# Example usage
input_string = "hello world"
frequency = character_frequency(input_string)
print("Character frequency:", frequency)

# Find the first non-repeating character in a string and return its index.
def first_non_repeating_character(input_string):
    frequency = Counter(input_string)
    print("Character frequency:", frequency)
    for index, char in enumerate(input_string):
        if frequency[char] == 1:
            return index
    return -1
# Example usage
input_string = "hello world"
index = first_non_repeating_character(input_string)
if index != -1:
    print(f"The first non-repeating character is '{input_string[index]}' at index {index}.")

