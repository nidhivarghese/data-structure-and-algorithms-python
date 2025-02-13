# Create a function that reverses a string
# 'Hello' should be:
# 'olleH'

def reverseString(text):
    splitText = list(text)
    j = len(splitText) - 1
    for i in range(0, len(splitText) // 2):
        temp = splitText[i]
        splitText[i] = splitText[j]
        splitText[j] = temp
        j -= 1

    return "".join(splitText)



text = "Hello Goodbye!"
print(reverseString(text))