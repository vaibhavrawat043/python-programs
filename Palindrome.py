
def CheckPalindrome(inputString):
    inputString = inputString.lower()
    reverseString = "" 
    for s in inputString: 
        reverseString = s + reverseString
    if (inputString==reverseString): 
        print("String is palindrome") 
    else:
        print("String is not a palindrome")

inputString = "redivideR"
CheckPalindrome(inputString)
