def most_frequent_character(input_string):
#     #Finds the most frequent character in a string.
#     Returns:
#         str: the most frequent character , or None if the input string is empty.
    if not input_string:
        return None
    char_counts ={}
    for char in input_string:
        char_counts[char] = char_counts.get(char,0)+1
        max_count=0
        most_frequent =''
    for char, count in char_counts.items():
        if count> max_count:
            max_count=count
            most_frequent=char
    return most_frequent
#print(most_frequent_character("banana"))  
word = input("enter a word to find the most frequent letter in that word: ")
result = most_frequent_character(word)

print(f"the most frequent letter in the word {word} is {result}")