'''

Exclamation marks series #11: Replace all vowel to exclamation mark in the sentence (8kyu)
https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed

Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"

'''
def replace_exclamation(s):
    formatted_word = []
    for char in s:
        formatted_word.append("!") if char.lower() in "aeiou" else formatted_word.append(char)

    return "".join(formatted_word)


print(replace_exclamation("!Hi! Hi!"))
