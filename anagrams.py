'''
Python program to check if two given strings are anagram.

Anagrams are two which consists same characters with same number of iterations.
'''


def are_anagrams(str1, str2):
    '''
    Arguments : string1 and string2
    Returns : Boolean Value
    '''
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character frequencies
    char_count1 = {}
    char_count2 = {}

    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    return char_count1 == char_count2

# Example usage
string1 = "listen"
string2 = "tisslne"
result = are_anagrams(string1, string2)
print(f"Are '{0}' and '{string2}' anagrams? {result}")

