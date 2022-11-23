
class Solution:
 
    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
 
        if sorted(a) == sorted(b):
            return True
        else:
            return False
 
# {
#  Driver Code Starts
 
a = "peek" 
b = "keep"
if(Solution().isAnagram(a, b)):
    print("The two strings are anagram of each other")
else:
    print("The two strings are not anagram of each other")
# } Driver Code Ends