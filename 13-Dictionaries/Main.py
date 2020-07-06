from collections import OrderedDict

grocies = {'bananas': 5, 'oranges': 3}
print(grocies.get('bananas'))

print("=====================================")

contacts = {
    'Caam': {'phone': '123-4567', 'email': 'caam@email.com'},
    'Vilvact': {'phone': '456-7890', 'email': 'vilvact@email.com'}
}
print(contacts['Caam'])

print("=====================================")

sentence = "I like the name Caam , because the name Caam is the best."
word_counts = {
    'I': 1,
    'like': 1,
    'the': 3
}

word_counts['Caam'] = 2

# dict.items ()
# print(list(word_counts.items()))
# print("=====================================")
# dict.keys ()
# print(list(word_counts.keys()))
# print("=====================================")
# dict.values ()
# print(list(word_counts.values()))
# print("=====================================")
# dict.pop (key)
# print(word_counts)
# word_counts.pop('the')
# print(word_counts)
# print("=====================================")
# dict.popitem ()
# print(word_counts)
# word_counts.popitem()
# print(word_counts)
# print("=====================================")
# dict.clear ()
# print(word_counts)
# word_counts.clear()
# print(word_counts)
# print("=====================================")

# print(word_counts)
#word_counts['Caam'] = 2
# print(word_counts)
# print("=====================================")

print(sorted(list(word_counts.values())))
