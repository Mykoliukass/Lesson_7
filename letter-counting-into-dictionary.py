# write a program witch takes at least 5 minimum words (use only 1 input) separated by comma .
#  From those words , make a dictionary where the key is a letter and value is a number of the frequency the letter did appear in all those words. 
# Letters should be in alphabetical order.
words = input("""Please provide five or more words, separated by a comma. 
I will count how many times each letter is repeated throughout all these words and provide you with a dictionary of these counts. """)
words_no_separation_all_lower = words.replace(' ', '').replace(',', '').lower()
letter_count = {}
for letter in words_no_separation_all_lower:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1
print(letter_count)