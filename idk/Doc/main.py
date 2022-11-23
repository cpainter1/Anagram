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
print(sortedstr2)

class Answer:
    def checkIfAnagram(self, Str1, Str2):
        if sorted(Str1) == sorted(Str2):
            return True
        else:
            return False

if dictionary.check(Str1) == True or dictionary.check(Str2) == True:
    if(Answer().checkIfAnagram(Str1, Str2)):
        if Str1 == Str2: # Check if String2 and String 2 are identical
            print(f'You realize the strings {Str1} and {Str2} are identical... right?')
        else: # If the strings are not identical but are anagrams:
            print(f'The strings {Str1} and {Str2} are anagrams.')
        
    else: # If the strings are not anagrams
        print(f'The strings {Str1} and {Str2} are not anagrams.')

else:
    if dictionary.check(Str1) == False and dictionary.check(Str2) == False:
        print(f'The strings {Str1} and {Str2} are not valid English words.')
    elif dictionary.check(Str1) == False:
        print(f'The string {Str1} is not a valid English word.')
    elif dictionary.check(Str2) == False:
        print(f'The string {Str2} is not a valid English word.')

        

#easter egg
if Str1 == "caleb" or Str2 == "caleb":
    print("Hey... you found my name!")

