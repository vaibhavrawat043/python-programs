
def CheckPalindrome(inputString):
    reverseString = "" 
    for s in inputString: 
        reverseString = s + reverseString
    if (inputString==reverseString): 
        print("String is palindrome") 
    else:
        print("String is not a palindrome")

inputString = "palindrome"
inputString = inputString.lower()
CheckPalindrome(inputString)
