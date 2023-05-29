def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False

    # Create dictionaries to store character frequencies
    char_count1 = {}
    char_count2 = {}

    # Count the occurrences of characters in str1
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1

    # Count the occurrences of characters in str2
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Compare the dictionaries
    return char_count1 == char_count2

# Example usage
string1 = "listen"
string2 = "sssss"
result = are_anagrams(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {result}")



