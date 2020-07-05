s = {'banana', 'apple', 'orange'}
s.add('banana')
print(s)

print("=====================================")

l = [1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 7, 'abc', 'abc', 'cba']
no_duplicate_set = set(l)
print(no_duplicate_set)

# Venn Diagram

# Union
print("=====================================")
library_1 = {'Harry Potter', 'Hunger Games', 'Lord Of The Rings'}
library_2 = {'Harry Potter', 'Hunger Games', 'Transformers', 'Resident Evil'}

all_book_in_town = library_1.union(library_2)
print(all_book_in_town)

# Intersection
print("=====================================")
library_1 = {'Harry Potter', 'Hunger Games', 'Lord Of The Rings'}
library_2 = {'Harry Potter', 'Hunger Games', 'Transformers', 'Resident Evil'}

at_both_libraries = library_1.intersection(library_2)
print(at_both_libraries)

# Diff
print("=====================================")
library_1 = {'Harry Potter', 'Hunger Games', 'Lord Of The Rings'}
library_2 = {'Harry Potter', 'Hunger Games', 'Transformers', 'Resident Evil'}

diff1 = library_1.difference(library_2)
diff2 = library_2.difference(library_1)
print(diff1, diff2)
