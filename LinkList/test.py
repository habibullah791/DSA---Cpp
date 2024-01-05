# Based on given number, print even or odd. No if else or ternary operator.


# def print_even_odd(num):
#     if (num & 1):
#         return 'Odd'
#     else:
#         return 'Even'


# print(print_even_odd(2))

# "Flatten a nested array. e.g Input: [1, 2, [3, 4, 5, [6]], 7, 8]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]"


# # write a function such that if we pass 100 it returns 101 and if we pass 101 it returns 100 without if else and ternary operator
# def count_characters_frequency(s):
#     # Assuming the string only contains ASCII characters (you can adapt this for Unicode if needed)
#     char_frequency = [0] * 128  # 128 is the number of ASCII characters

#     for char in s:
#         char_frequency[ord(char)] += 1

#     # Printing the frequencies
#     for i in range(128):
#         if char_frequency[i] > 0:
#             print(f"Character '{chr(i)}' occurs {char_frequency[i]} times.")


# # Example usage
# input_string = "examplestring"
# count_characters_frequency(input_string)


# Write a function foo(x) which get an integer (it can be 12 or 18 just),
# return 12 if 18 passed and 18 if 12 passed, don't use if else ...


def count_occurrences(arr):
    occurrences = {}

    for num in arr:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1

    for num, count in occurrences.items():
        print(f"Number {num} occurs {count} times.")


# Example usage:
numbers = [4, 2, 8, 3, 4, 2, 8, 4, 5, 6, 2, 8, 7, 9, 2, 1, 8, 4, 3, 5]
count_occurrences(numbers)
