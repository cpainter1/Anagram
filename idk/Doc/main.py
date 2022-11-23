import enchant
dictionary = enchant.Dict("en_US")


print("Anagram Checker:\n")

Str1Input = input(str("What is your first string?\n")) # first string, allows you to try different strings without editing the code
Str2Input = input(str("What is your second string?\n")) # second string allows you to try different strings without editing the code

Str1 = Str1Input.lower() # converts the string to all lowercase
Str2 = Str2Input.lower()

sortedstr1 = sorted(Str1)
sortedstr2 = sorted(Str2)
print(sortedstr1)
