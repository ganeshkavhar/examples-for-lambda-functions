# Sort list of tuples by second element
students = [("Alice", 22), ("Bob", 19), ("Charlie", 25)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# Output: [('Bob', 19), ('Alice', 22), ('Charlie', 25)]

# Sort strings by length
words = ["apple", "pie", "banana", "cherry"]
print(sorted(words, key=lambda x: len(x)))
# Output: ['pie', 'apple', 'banana', 'cherry']
