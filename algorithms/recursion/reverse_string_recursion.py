def reverseStringyByRecursion(string):
    rev = string[-1]
    if len(string) == 1:
        return string
    else:
        rev = rev + reverseStringyByRecursion(string[:-1])

    return rev


def reverseStringByIteration(string):
    rev = ''

    for char in string:
        rev = char + rev

    return rev


word = "the big bang theory"
print(reverseStringyByRecursion(word))
print(reverseStringByIteration(word))
