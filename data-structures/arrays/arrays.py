strings = ['a', 'b', 'c', 'd', 'e']
print(strings)

# Access - O(1)
print("Element at 4th position:", strings[3])

# Insert - O(1)
strings.append('f')
print("After Appending: ", strings)

# Insert at a given position
strings.insert(0, 'x')  # Unshift - O(n)
print("After Inserting at the 1st position: ", strings)

strings.insert(3, 't') # Splice - O(n)
print("After inserting at the 4th position: ", strings)

# Delete - O(1)
popped_element = strings.pop()

print('Popped Element: ', popped_element)
print("After Popping: ", strings)
